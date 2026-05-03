"""
Download .md paper files from Google Drive to a local directory.

The script looks up each paper's .md file in a Google Drive folder by matching
the DOI-based filename (e.g. 10.1016_j.jebo.2023.01.012.md), derived from the
PDF paths in the provided list.

─── One-time setup ───────────────────────────────────────────────────────────
1. Install dependencies:
     pip install google-api-python-client google-auth-oauthlib google-auth-httplib2

2. Create OAuth 2.0 credentials in Google Cloud Console:
     https://console.cloud.google.com
     → APIs & Services → Library → enable "Google Drive API"
     → APIs & Services → Credentials → Create Credentials
     → OAuth client ID → Desktop app → Download JSON
     → save as batch_processing/gdrive_credentials.json

   In the OAuth consent screen (Audience tab):
     → set User Type to "External"
     → add your Gmail as a test user

3. First run opens a browser for one-time login; token cached in
   batch_processing/gdrive_token.json (gitignored).

─── Usage ────────────────────────────────────────────────────────────────────
Download a hardcoded list (default):
  python batch_processing/download_papers_md.py

Download from a text file (one PDF path per line):
  python batch_processing/download_papers_md.py --pdf-list my_papers.txt

Custom output dir or Drive folder name:
  python batch_processing/download_papers_md.py \\
    --pdf-list my_papers.txt \\
    --output-dir PGG_papers/papers \\
    --drive-folder papers_markdown
"""

import argparse
from pathlib import Path

from googleapiclient.discovery import build

from gdrive_helpers import download_file, find_folder, get_credentials, list_folder_files

# ── Config ────────────────────────────────────────────────────────────────────

DEFAULT_OUTPUT_DIR = Path(__file__).parent.parent / "PGG_papers" / "papers"
DEFAULT_DRIVE_FOLDER = "papers_markdown"

# ── PDF paths provided by supervisor ─────────────────────────────────────────

PDF_PATHS = [
    "paper_collection/WoS_251029.Data/PDF/4049811782/10.1628_093245616x14500948554072.pdf",
    "paper_collection/WoS_251029.Data/PDF/1870725893/10.1016_j.ejpoleco.2022.102222.pdf",
    "paper_collection/WoS_251029.Data/PDF/2996877866/10.1007_s00355-017-1081-5.pdf",
    "paper_collection/WoS_251029.Data/PDF/4213631799/10.1016_j.neuroimage.2019.06.047.pdf",
    "paper_collection/WoS_251029.Data/PDF/0303351160/10.1016_j.joep.2017.03.007.pdf",
    "paper_collection/WoS_251029.Data/PDF/1581435800/10.1016_j.jeem.2023.102895.pdf",
    "paper_collection/WoS_251029.Data/PDF/1845001244/10.1016_j.evolhumbehav.2016.02.001.pdf",
    "paper_collection/WoS_251029.Data/PDF/3578882908/10.1016_j.ecolecon.2015.05.011.pdf",
    "paper_collection/WoS_251029.Data/PDF/3719349221/10.5751_es-07532-200228.pdf",
    "paper_collection/WoS_251029.Data/PDF/1069117832/10.1126_science.1178883.pdf",
    "paper_collection/WoS_251029.Data/PDF/3573318850/10.1016_j.amc.2020.125063.pdf",
    "paper_collection/WoS_251029.Data/PDF/3616822172/10.1287_mnsc.2013.1848.pdf",
    "paper_collection/WoS_251029.Data/PDF/0423401433/10.1080_0013791x.2011.650839.pdf",
    "paper_collection/WoS_251029.Data/PDF/1416023182/10.1007_s10551-020-04664-5.pdf",
    "paper_collection/WoS_251029.Data/PDF/1401943880/10.1007_s10458-025-09698-5.pdf",
    "paper_collection/WoS_251029.Data/PDF/3857693299/10.1016_j.chaos.2025.116591.pdf",
    "paper_collection/WoS_251029.Data/PDF/1278547491/10.1016_j.jebo.2025.107071.pdf",
    "paper_collection/WoS_251029.Data/PDF/2015831264/10.1016_j.jesp.2024.104695.pdf",
    "paper_collection/WoS_251029.Data/PDF/2066990816/10.1111_ecoj.12209.pdf",
    "paper_collection/WoS_251029.Data/PDF/3422857391/10.1371_journal.pone.0044747.pdf",
    "paper_collection/WoS_251029.Data/PDF/1683673949/10.1007_s00355-021-01363-6.pdf",
    "paper_collection/WoS_251029.Data/PDF/2985909918/10.1177_0190272519882389.pdf",
    "paper_collection/WoS_251029.Data/PDF/0752750471/10.1016_j.jebo.2019.03.007.pdf",
    "paper_collection/WoS_251029.Data/PDF/3439037746/10.3389_fnhum.2013.00252.pdf",
    "paper_collection/WoS_251029.Data/PDF/2097657371/10.1073_pnas.2508479122.pdf",
    "paper_collection/WoS_251029.Data/PDF/1925612439/10.1016_j.jecp.2022.105376.pdf",
    "paper_collection/WoS_251029.Data/PDF/1753744777/10.1093_jleo_ewy026.pdf",
    "paper_collection/WoS_251029.Data/PDF/3244173420/10.1257_mic.6.1.290.pdf",
    "paper_collection/WoS_251029.Data/PDF/2237886876/10.1016_j.obhdp.2012.06.007.pdf",
    "paper_collection/WoS_251029.Data/PDF/2489630238/10.1002_ejsp.793.pdf",
    "paper_collection/WoS_251029.Data/PDF/1080799831/10.1016_j.geb.2023.02.005.pdf",
    "paper_collection/WoS_251029.Data/PDF/0455843485/10.1080_00220388.2012.693169.pdf",
    "paper_collection/WoS_251029.Data/PDF/1349672635/10.1037_pspi0000389.pdf",
    "paper_collection/WoS_251029.Data/PDF/0704457236/10.1016_j.geb.2019.02.006.pdf",
    "paper_collection/WoS_251029.Data/PDF/3422319314/10.1016_j.jebo.2024.02.003.pdf",
    "paper_collection/WoS_251029.Data/PDF/1472933199/10.1037_npe0000011.pdf",
    "paper_collection/WoS_251029.Data/PDF/2219311236/10.1016_j.chaos.2022.112413.pdf",
    "paper_collection/WoS_251029.Data/PDF/1979629507/10.1038_s41598-024-81636-z.pdf",
    "paper_collection/WoS_251029.Data/PDF/2432382642/10.1016_j.cognition.2022.105215.pdf",
    "paper_collection/WoS_251029.Data/PDF/3590974891/10.1038_s41467-024-49779-9.pdf",
    "paper_collection/WoS_251029.Data/PDF/0764181562/10.1037_xge0001004.pdf",
    "paper_collection/WoS_251029.Data/PDF/0711645630/10.1371_journal.pone.0061458.pdf",
    "paper_collection/WoS_251029.Data/PDF/3719791986/10.1016_j.jpubeco.2016.09.001.pdf",
    "paper_collection/WoS_251029.Data/PDF/3455528526/10.1007_s10683-011-9272-x.pdf",
    "paper_collection/WoS_251029.Data/PDF/4139692590/10.1093_sf_sot015.pdf",
    "paper_collection/WoS_251029.Data/PDF/0741957620/10.1111_soin.12218.pdf",
    "paper_collection/WoS_251029.Data/PDF/2915677369/10.1016_j.euroecorev.2023.104659.pdf",
    "paper_collection/WoS_251029.Data/PDF/2939271808/10.1038_s41598-024-71106-x.pdf",
    "paper_collection/WoS_251029.Data/PDF/0782630773/10.1177_0022002708322361.pdf",
    "paper_collection/WoS_251029.Data/PDF/0446913970/10.1016_j.socec.2015.03.007.pdf",
    "paper_collection/WoS_251029.Data/PDF/3104910224/10.1371_journal.pone.0269523.pdf",
    "paper_collection/WoS_251029.Data/PDF/3428415413/10.1371_journal.pone.0175472.pdf",
    "paper_collection/WoS_251029.Data/PDF/2507461657/10.1038_s41562-022-01341-7.pdf",
    "paper_collection/WoS_251029.Data/PDF/3421344190/10.1177_1948550614527115.pdf",
    "paper_collection/WoS_251029.Data/PDF/0186737643/10.1016_j.jebo.2017.10.009.pdf",
    "paper_collection/WoS_251029.Data/PDF/1412017135/10.1007_s12110-003-1007-z.pdf",
    "paper_collection/WoS_251029.Data/PDF/1242608872/10.1007_s10683-013-9360-1.pdf",
    "paper_collection/WoS_251029.Data/PDF/2505467888/10.3389_fpsyg.2023.1198797.pdf",
    "paper_collection/WoS_251029.Data/PDF/2073088030/10.1016_j.jesp.2016.06.007.pdf",
    "paper_collection/WoS_251029.Data/PDF/3717339906/10.1016_j.socec.2011.04.001.pdf",
    "paper_collection/WoS_251029.Data/PDF/4034581302/10.1016_j.ecolecon.2011.05.011.pdf",
    "paper_collection/WoS_251029.Data/PDF/3975430280/10.1093_qje_qjy013.pdf",
    "paper_collection/WoS_251029.Data/PDF/3221265411/10.1523_jneurosci.1642-12.2013.pdf",
    "paper_collection/WoS_251029.Data/PDF/2388798977/10.1038_s41598-017-11580-8.pdf",
    "paper_collection/WoS_251029.Data/PDF/2866124618/10.1016_j.irle.2013.07.005.pdf",
    "paper_collection/WoS_251029.Data/PDF/1203013321/10.1038_s41598-020-67757-1.pdf",
    "paper_collection/WoS_251029.Data/PDF/2402540405/10.1038_s41467-020-14712-3.pdf",
    "paper_collection/WoS_251029.Data/PDF/2132885249/10.1016_j.jebo.2023.01.012.pdf",
    "paper_collection/WoS_251029.Data/PDF/0582513990/10.3390_ijerph192416578.pdf",
    "paper_collection/WoS_251029.Data/PDF/1170388403/10.1016_j.jpubeco.2019.104053.pdf",
    "paper_collection/WoS_251029.Data/PDF/3522114935/10.3389_fnbeh.2016.00053.pdf",
    "paper_collection/WoS_251029.Data/PDF/1549495354/10.1007_s12110-012-9136-x.pdf",
    "paper_collection/WoS_251029.Data/PDF/4005987940/10.1371_journal.pone.0110045.pdf",
    "paper_collection/WoS_251029.Data/PDF/3279520505/10.1523_jneurosci.0595-16.2016.pdf",
    "paper_collection/WoS_251029.Data/PDF/0093691606/10.1016_j.jebo.2008.09.007.pdf",
    "paper_collection/WoS_241106.Data/PDF/0304089172/10.1111_jssr.12045.pdf",
    "paper_collection/WoS_251029.Data/PDF/0242097408/10.1016_j.irle.2014.03.001.pdf",
    "paper_collection/WoS_251029.Data/PDF/3730853768/10.1098_rsbl.2012.0470.pdf",
    "paper_collection/WoS_251029.Data/PDF/2715492412/10.1038_s41598-024-77190-3.pdf",
    "paper_collection/WoS_251029.Data/PDF/3075409185/10.1016_j.jrp.2016.08.004.pdf",
    "paper_collection/WoS_251029.Data/PDF/3967525996/10.17583_hse.12426.pdf",
    "paper_collection/WoS_251029.Data/PDF/2555550623/10.1177_0146167216629123.pdf",
    "paper_collection/WoS_251029.Data/PDF/2844336349/10.1016_j.jebo.2025.107207.pdf",
    "paper_collection/WoS_251029.Data/PDF/2604135442/10.1017_s1355770x12000381.pdf",
    "paper_collection/WoS_251029.Data/PDF/0775056794/10.1007_s11031-014-9395-4.pdf",
    "paper_collection/WoS_251029.Data/PDF/0579028313/10.1016_j.jesp.2019.02.009.pdf",
    "paper_collection/WoS_251029.Data/PDF/0792378194/10.1016_s0167-2681(98)00121-8.pdf",
    "paper_collection/WoS_251029.Data/PDF/1644730116/10.1073_pnas.0908855106.pdf",
    "paper_collection/WoS_251029.Data/PDF/0219594302/10.1016_j.jpubeco.2021.104429.pdf",
    "paper_collection/WoS_251029.Data/PDF/1541787377/10.1007_s11558-025-09594-3.pdf",
    "paper_collection/WoS_251029.Data/PDF/2896556829/10.1016_j.jebo.2023.04.028.pdf",
    "paper_collection/WoS_251029.Data/PDF/1048536879/10.1177_09567976211054786.pdf",
    "paper_collection/WoS_251029.Data/PDF/3375498704/10.1016_s0167-2681(02)00098-7.pdf",
    "paper_collection/WoS_251029.Data/PDF/0089439146/10.1016_j.jebo.2023.09.007.pdf",
    "paper_collection/WoS_251029.Data/PDF/4044079270/10.3389_fpsyg.2018.01865.pdf",
    "paper_collection/WoS_251029.Data/PDF/2257451302/10.1111_ecin.12477.pdf",
    "paper_collection/WoS_251029.Data/PDF/2022337363/10.1063_5.0147226.pdf",
    "paper_collection/WoS_251029.Data/PDF/3811051759/10.2307_2667052.pdf",
    "paper_collection/WoS_251029.Data/PDF/3919361718/10.1093_sf_soad073.pdf",
    "paper_collection/WoS_251029.Data/PDF/3593016854/10.1016_j.evolhumbehav.2022.10.002.pdf",
    "paper_collection/WoS_251029.Data/PDF/0555099393/10.1016_j.jpubeco.2016.09.008.pdf",
    "paper_collection/WoS_251029.Data/PDF/3947212610/10.1016_j.joep.2018.09.006.pdf",
    "paper_collection/WoS_251029.Data/PDF/2399320402/10.1126_sciadv.aau5175.pdf",
    "paper_collection/WoS_251029.Data/PDF/2805478233/10.1016_j.jpubeco.2015.03.012.pdf",
    "paper_collection/WoS_251029.Data/PDF/2009726312/10.1257_aer.90.4.980.pdf",
    "paper_collection/WoS_251029.Data/PDF/2525825844/10.1080_15534510.2019.1641147.pdf",
    "paper_collection/WoS_251029.Data/PDF/2426206510/10.1257_aer.102.7.3317.pdf",
    "paper_collection/WoS_251029.Data/PDF/3936859996/10.1073_pnas.0710069105.pdf",
    "paper_collection/WoS_251029.Data/PDF/0108451979/10.1038_s41562-022-01457-w.pdf",
    "paper_collection/WoS_251029.Data/PDF/0863689917/10.1016_j.evolhumbehav.2015.12.003.pdf",
    "paper_collection/WoS_251029.Data/PDF/1097663793/10.1111_geer.12103.pdf",
    "paper_collection/WoS_251029.Data/PDF/1080502308/10.1111_ajps.12139.pdf",
    "paper_collection/WoS_251029.Data/PDF/2076532804/10.1016_j.chaos.2021.111183.pdf",
    "paper_collection/WoS_251029.Data/PDF/2504859690/10.1016_j.econlet.2017.05.022.pdf",
    "paper_collection/WoS_251029.Data/PDF/2614540763/10.1016_j.geb.2015.10.001.pdf",
    "paper_collection/WoS_251029.Data/PDF/2860839159/10.1371_journal.pone.0267153.pdf",
    "paper_collection/WoS_251029.Data/PDF/2965570242/10.1016_j.geb.2023.08.017.pdf",
    "paper_collection/WoS_251029.Data/PDF/0007047983/10.1371_journal.pone.0018050.pdf",
    "paper_collection/WoS_251029.Data/PDF/0951788018/10.1007_s11238-022-09897-6.pdf",
    "paper_collection/WoS_251029.Data/PDF/1253207672/10.1038_srep07470.pdf",
    "paper_collection/WoS_241106.Data/PDF/2787338331/10.1038_sdata.2016.99.pdf",
    "paper_collection/WoS_251029.Data/PDF/2407636607/10.1371_journal.pone.0017044.pdf",
    "paper_collection/WoS_251029.Data/PDF/2566361835/10.1098_rsos.192090.pdf",
    "paper_collection/WoS_251029.Data/PDF/2223870998/10.1111_jems.12570.pdf",
    "paper_collection/WoS_251029.Data/PDF/2124778828/10.1016_j.joep.2023.102657.pdf",
    "paper_collection/WoS_251029.Data/PDF/3540371892/10.1177_0022002714560349.pdf",
    "paper_collection/WoS_251029.Data/PDF/2288314078/10.1002_pchj.259.pdf",
    "paper_collection/WoS_251029.Data/PDF/0919214647/10.1016_j.euroecorev.2010.04.003.pdf",
    "paper_collection/WoS_251029.Data/PDF/3935659553/10.1111_spc3.12924.pdf",
    "paper_collection/WoS_251029.Data/PDF/0460467935/10.20350_digitalCSIC_16534.pdf",
    "paper_collection/WoS_251029.Data/PDF/1904612995/10.1016_j.socec.2015.12.002.pdf",
    "paper_collection/WoS_251029.Data/PDF/3494425132/10.1086_699547.pdf",
    "paper_collection/WoS_251029.Data/PDF/0968961127/10.1016_j.geb.2021.11.012.pdf",
    "paper_collection/WoS_251029.Data/PDF/4135663885/10.1093_qje_qjz001.pdf",
    "paper_collection/WoS_251029.Data/PDF/1578037126/10.1002_bdm.2208.pdf",
    "paper_collection/WoS_251029.Data/PDF/2144072703/10.1016_j.jpubeco.2015.12.012.pdf",
    "paper_collection/WoS_251029.Data/PDF/2102588474/10.1111_ecin.12713.pdf",
    "paper_collection/WoS_251029.Data/PDF/2507255882/10.1016_j.jebo.2013.04.001.pdf",
    "paper_collection/WoS_251029.Data/PDF/2403847589/10.1111_eth.12223.pdf",
    "paper_collection/WoS_251029.Data/PDF/3948550453/10.1016_j.econlet.2007.09.048.pdf",
    "paper_collection/WoS_251029.Data/PDF/1120630960/10.1371_journal.pone.0248599.pdf",
    "paper_collection/WoS_251029.Data/PDF/0378836593/10.1016_j.socec.2018.09.006.pdf",
    "paper_collection/WoS_251029.Data/PDF/4228432048/10.1628_093245607780182008.pdf",
    "paper_collection/WoS_251029.Data/PDF/2041984908/10.1038_s41598-021-89675-6.pdf",
    "paper_collection/WoS_251029.Data/PDF/2883858014/10.1016_j.geb.2025.01.011.pdf",
    "paper_collection/WoS_251029.Data/PDF/2583843202/10.1126_sciadv.aau7296.pdf",
    "paper_collection/WoS_251029.Data/PDF/1106418446/10.1111_jopy.12896.pdf",
    "paper_collection/WoS_251029.Data/PDF/3221365071/10.1002_bdm.1976.pdf",
    "paper_collection/WoS_251029.Data/PDF/1292413412/10.1371_journal.pone.0026922.pdf",
    "paper_collection/WoS_251029.Data/PDF/3650265134/10.1017_s0140525x05000142.pdf",
    "paper_collection/WoS_251029.Data/PDF/3982608892/10.1098_rstb.2020.0304.pdf",
    "paper_collection/WoS_251029.Data/PDF/0284327308/10.1007_s00199-018-1146-4.pdf",
    "paper_collection/WoS_251029.Data/PDF/1936526797/10.1016_j.ejpoleco.2022.102354.pdf",
    "paper_collection/WoS_251029.Data/PDF/1944442929/10.1038_s41562-025-02258-7.pdf",
    "paper_collection/WoS_251029.Data/PDF/2503798240/10.1016_j.socec.2023.102081.pdf",
    "paper_collection/WoS_251029.Data/PDF/4270948909/10.1016_j.joep.2012.10.004.pdf",
    "paper_collection/WoS_251029.Data/PDF/2674870098/10.1007_s11127-016-0319-6.pdf",
    "paper_collection/WoS_251029.Data/PDF/0525445259/10.1016_j.joep.2013.07.002.pdf",
    "paper_collection/WoS_251029.Data/PDF/0294987084/10.1016_j.actpsy.2024.104608.pdf",
    "paper_collection/WoS_251029.Data/PDF/4292963430/10.1098_rstb.2008.0275.pdf",
    "paper_collection/WoS_251029.Data/PDF/1062218704/10.1007_s12110-003-1003-3.pdf",
    "paper_collection/WoS_251029.Data/PDF/0637172784/10.1111_jpet.12384.pdf",
    "paper_collection/WoS_251029.Data/PDF/0475945128/10.1016_j.euroecorev.2024.104795.pdf",
    "paper_collection/WoS_251029.Data/PDF/3257145922/10.1016_j.evolhumbehav.2004.08.009.pdf",
    "paper_collection/WoS_251029.Data/PDF/1347795651/10.3389_fpsyg.2022.794953.pdf",
    "paper_collection/WoS_251029.Data/PDF/0772458889/10.1098_rspb.2012.0063.pdf",
    "paper_collection/WoS_251029.Data/PDF/2559310617/10.1162_rest.2009.10174.pdf",
    "paper_collection/WoS_251029.Data/PDF/3279774423/10.1016_j.isci.2020.101438.pdf",
    "paper_collection/WoS_251029.Data/PDF/0822514995/10.1111_jels.12042.pdf",
    "paper_collection/WoS_241106.Data/PDF/0376875057/10.1371_journal.pone.0085691.pdf",
    "paper_collection/WoS_251029.Data/PDF/2015196827/10.1080_00220485.2018.1551097.pdf",
    "paper_collection/WoS_251029.Data/PDF/2229907092/10.1016_j.jebo.2023.06.027.pdf",
    "paper_collection/WoS_251029.Data/PDF/0775218594/10.1016_j.jebo.2019.12.007.pdf",
    "paper_collection/WoS_251029.Data/PDF/1025020172/10.1016_j.ssresearch.2018.12.012.pdf",
    "paper_collection/WoS_251029.Data/PDF/0167793078/10.3390_su12198175.pdf",
    "paper_collection/WoS_251029.Data/PDF/4071258923/10.1038_s41598-021-88663-0.pdf",
    "paper_collection/WoS_251029.Data/PDF/0219976257/10.1086_730717.pdf",
    "paper_collection/WoS_251029.Data/PDF/1423524763/10.1111_j.1467-9779.2010.01472.x.pdf",
    "paper_collection/WoS_251029.Data/PDF/2569933614/10.1093_pnasnexus_pgad091.pdf",
    "paper_collection/WoS_251029.Data/PDF/3562926144/10.1016_j.euroecorev.2018.04.003.pdf",
    "paper_collection/WoS_251029.Data/PDF/0629248671/10.1016_j.joep.2019.102193.pdf",
    "paper_collection/WoS_251029.Data/PDF/1049783667/10.1016_j.jenvp.2020.101441.pdf",
    "paper_collection/WoS_251029.Data/PDF/0113658790/10.1007_s11238-023-09929-9.pdf",
    "paper_collection/WoS_251029.Data/PDF/1774809492/10.1037_npe0000099.pdf",
    "paper_collection/WoS_251029.Data/PDF/2676786091/10.1007_s00265-014-1741-8.pdf",
    "paper_collection/WoS_251029.Data/PDF/0906183458/10.1257_mic.20180336.pdf",
    "paper_collection/WoS_251029.Data/PDF/0122522636/10.1177_0022002714564426.pdf",
    "paper_collection/WoS_251029.Data/PDF/3935355897/10.1016_j.jesp.2019.103823.pdf",
    "paper_collection/WoS_251029.Data/PDF/1776808933/10.1257_mic.3.4.77.pdf",
    "paper_collection/WoS_251029.Data/PDF/2236123282/10.1002_hbm.21298.pdf",
    "paper_collection/WoS_251029.Data/PDF/1539942439/10.1007_s12110-009-9072-6.pdf",
    "paper_collection/WoS_251029.Data/PDF/0388146290/10.1371_journal.pone.0326564.pdf",
    "paper_collection/WoS_251029.Data/PDF/1028616614/10.1007_s11127-021-00925-7.pdf",
    "paper_collection/WoS_251029.Data/PDF/2424277288/10.1016_j.jesp.2018.06.009.pdf",
    "paper_collection/WoS_251029.Data/PDF/2858371637/10.1007_s11948-014-9575-3.pdf",
    "paper_collection/WoS_251029.Data/PDF/2551743279/10.1007_s10551-011-0795-z.pdf",
    "paper_collection/WoS_251029.Data/PDF/1047048267/10.1037_a0011381.pdf",
]

# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Download .md paper files from Google Drive."
    )
    parser.add_argument(
        "--pdf-list",
        type=Path,
        default=None,
        help="Text file with one PDF path per line. Defaults to the hardcoded list in this script.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help=f"Local directory to save .md files (default: {DEFAULT_OUTPUT_DIR})",
    )
    parser.add_argument(
        "--drive-folder",
        default=DEFAULT_DRIVE_FOLDER,
        help=f"Name of the Google Drive folder containing .md files (default: {DEFAULT_DRIVE_FOLDER})",
    )
    args = parser.parse_args()

    # Resolve PDF path list
    if args.pdf_list:
        pdf_paths = [l.strip() for l in args.pdf_list.read_text().splitlines() if l.strip()]
        print(f"Loaded {len(pdf_paths)} paths from {args.pdf_list}")
    else:
        pdf_paths = PDF_PATHS
        print(f"Using hardcoded list of {len(pdf_paths)} paths")

    # Derive target .md filenames
    target_filenames = {Path(p).stem + ".md" for p in pdf_paths}
    print(f"Target files: {len(target_filenames)}")

    # Authenticate
    print("Authenticating with Google Drive...")
    creds = get_credentials()
    service = build("drive", "v3", credentials=creds)

    # Find Drive folder
    print(f"Searching for '{args.drive_folder}' folder in Google Drive...")
    folders = find_folder(service, args.drive_folder)
    if not folders:
        print(f"ERROR: Could not find '{args.drive_folder}' folder in your Google Drive.")
        return
    if len(folders) > 1:
        print(f"Found {len(folders)} folders named '{args.drive_folder}'. Using the first one.")
    folder = folders[0]
    folder_id = folder["id"]
    print(f"Found folder: {folder['name']} (id={folder_id})")

    # List all files in the folder
    print("Listing files in Drive folder...")
    drive_files = list_folder_files(service, folder_id)
    print(f"Found {len(drive_files)} files in Drive folder.")

    # Download
    args.output_dir.mkdir(parents=True, exist_ok=True)
    downloaded, skipped, missing = [], [], []

    for md_filename in sorted(target_filenames):
        dest = args.output_dir / md_filename
        if dest.exists():
            skipped.append(md_filename)
            continue
        if md_filename in drive_files:
            print(f"  Downloading {md_filename}...")
            download_file(service, drive_files[md_filename], dest)
            downloaded.append(md_filename)
        else:
            missing.append(md_filename)

    # Summary
    print(f"\n{'='*60}")
    print(f"Downloaded : {len(downloaded)}")
    print(f"Skipped    : {len(skipped)} (already existed)")
    print(f"Not found  : {len(missing)}")
    if missing:
        print("\nFiles not found in Drive:")
        for f in missing:
            print(f"  {f}")


if __name__ == "__main__":
    main()
