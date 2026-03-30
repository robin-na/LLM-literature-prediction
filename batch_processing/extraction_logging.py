from __future__ import annotations

from typing import Any, Sequence

try:
    import tiktoken
except ImportError:  # pragma: no cover - optional dependency
    tiktoken = None


DEFAULT_PRICE_INPUT_PER_1M = 2.0
DEFAULT_PRICE_OUTPUT_PER_1M = 8.0
DEFAULT_SIMPLE_OUTPUT_TOKENS = 3500
DEFAULT_AGENT_OUTPUT_TOKENS = 1200
DEFAULT_CRITIC_OUTPUT_TOKENS = 900


class LiveCostTracker:
    def __init__(
        self,
        *,
        model: str,
        price_input_per_1m: float = DEFAULT_PRICE_INPUT_PER_1M,
        price_output_per_1m: float = DEFAULT_PRICE_OUTPUT_PER_1M,
        simple_output_tokens: int = DEFAULT_SIMPLE_OUTPUT_TOKENS,
        agent_output_tokens: int = DEFAULT_AGENT_OUTPUT_TOKENS,
        critic_output_tokens: int = DEFAULT_CRITIC_OUTPUT_TOKENS,
    ) -> None:
        self.model = model
        self.price_input_per_1m = price_input_per_1m
        self.price_output_per_1m = price_output_per_1m
        self.simple_output_tokens = simple_output_tokens
        self.agent_output_tokens = agent_output_tokens
        self.critic_output_tokens = critic_output_tokens
        self.total_input_tokens = 0
        self.total_estimated_output_tokens = 0
        self.request_count = 0

    def start_paper(
        self,
        paper_id: str,
        *,
        simple_fields: Sequence[str] | None = None,
        agentic_fields: Sequence[str] | None = None,
    ) -> None:
        print("\n" + "=" * 80, flush=True)
        print(f"[paper] {paper_id}", flush=True)
        print("=" * 80, flush=True)
        if simple_fields is not None:
            print("[mode] simple  -> " + ", ".join(simple_fields), flush=True)
        if agentic_fields is not None:
            print("[mode] agentic -> " + ", ".join(agentic_fields), flush=True)
        if simple_fields is not None or agentic_fields is not None:
            print("-" * 80, flush=True)

    def log_simple_request(
        self,
        *,
        paper_id: str,
        system_prompt: str,
        user_prompt: str,
    ) -> None:
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ]
        self.log_request(
            label=f"{paper_id}:simple:all_non_agentic_fields",
            messages=messages,
            estimated_output_tokens=self.simple_output_tokens,
        )

    def callback(self, payload: dict[str, Any]) -> None:
        label = str(payload.get("label", "agent_call"))
        messages = payload.get("messages", [])
        estimated_output_tokens = (
            self.critic_output_tokens if "critic" in label else self.agent_output_tokens
        )
        self.log_request(
            label=label,
            messages=messages if isinstance(messages, list) else [],
            estimated_output_tokens=estimated_output_tokens,
        )

    def log_request(
        self,
        *,
        label: str,
        messages: list[dict[str, Any]],
        estimated_output_tokens: int,
    ) -> None:
        input_tokens = self.estimate_messages_tokens(messages)
        input_cost = (input_tokens / 1_000_000) * self.price_input_per_1m
        output_cost = (estimated_output_tokens / 1_000_000) * self.price_output_per_1m
        total_cost = input_cost + output_cost

        self.request_count += 1
        self.total_input_tokens += input_tokens
        self.total_estimated_output_tokens += estimated_output_tokens
        cumulative_cost = (
            (self.total_input_tokens / 1_000_000) * self.price_input_per_1m
            + (self.total_estimated_output_tokens / 1_000_000) * self.price_output_per_1m
        )

        print(f"[estimate {self.request_count:03d}] {self.pretty_label(label)}", flush=True)
        print(
            f"  input     ~ {input_tokens:>10,} tok   ~ ${input_cost:>8.4f}",
            flush=True,
        )
        print(
            f"  output    ~ {estimated_output_tokens:>10,} tok   ~ ${output_cost:>8.4f}",
            flush=True,
        )
        print(f"  call est. ~ ${total_cost:>8.4f}", flush=True)
        print(
            "  cumulative"
            f" ~ in {self.total_input_tokens:,} tok"
            f" | out {self.total_estimated_output_tokens:,} tok"
            f" | ${cumulative_cost:.4f}",
            flush=True,
        )

    def estimate_messages_tokens(self, messages: list[dict[str, Any]]) -> int:
        total = 0
        for message in messages:
            total += 4
            total += self.estimate_text_tokens(str(message.get("role", "")))
            total += self.estimate_text_tokens(self.flatten_message_content(message.get("content", "")))
            for tool_call in message.get("tool_calls", []) or []:
                function = tool_call.get("function", {})
                total += self.estimate_text_tokens(str(function.get("name", "")))
                total += self.estimate_text_tokens(str(function.get("arguments", "")))
            tool_call_id = message.get("tool_call_id")
            if tool_call_id:
                total += self.estimate_text_tokens(str(tool_call_id))
        return total

    def estimate_text_tokens(self, text: str) -> int:
        if tiktoken is not None:
            try:
                encoding = tiktoken.encoding_for_model(self.model)
            except Exception:
                encoding = tiktoken.get_encoding("cl100k_base")
            return len(encoding.encode(text))
        return max(1, len(text) // 4)

    def flatten_message_content(self, content: Any) -> str:
        if isinstance(content, str):
            return content
        if isinstance(content, list):
            parts: list[str] = []
            for item in content:
                if isinstance(item, dict):
                    parts.append(str(item.get("text", "")))
                else:
                    parts.append(str(item))
            return "\n".join(parts)
        return str(content)

    def pretty_label(self, label: str) -> str:
        parts = label.split(":")
        if len(parts) == 3 and parts[1] == "simple":
            return f"simple  | {parts[0]} | {parts[2].replace('_', ' ')}"
        if len(parts) >= 2:
            return f"agentic | {parts[0]} -> {':'.join(parts[1:]).replace('_', ' ')}"
        return label.replace("_", " ")
