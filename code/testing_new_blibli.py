
import requests
from bs4 import BeautifulSoup 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from alive_progress import alive_bar
# capa = DesiredCapabilities.CHROME
# capa["pageLoadStrategy"] = "none"
list_link=["https://www.blibli.com/p/smg-jog-solo-pantene-shampoo-anti-dandruff-900-ml-2-pcs/ps--PGJ-60021-00033",
"https://www.blibli.com/p/surabaya-head-shoulders-clean-balanced-shampoo-400-ml/ps--PGS-60022-00205",
"https://www.blibli.com/p/surabaya-head-shoulders-cool-blast-shampoo-165-ml/ps--PGS-60022-00193",
"https://www.blibli.com/p/surabaya-head-shoulders-cool-blast-shampoo-450-ml/ps--PGS-60022-00191",
"https://www.blibli.com/p/surabaya-head-shoulders-cool-menthol-shampoo-850-ml/ps--PGS-60022-00499",
"https://www.blibli.com/p/surabaya-head-shoulders-smooth-or-silky-shampoo-300-ml/ps--PGS-60022-00219",
"https://www.blibli.com/p/surabaya-head-shoulders-smooth-or-silky-shampoo-400-ml/ps--PGS-60022-00217",
"https://www.blibli.com/p/surabaya-herbal-essences-colour-me-happy-colour-safe-kondisioner-300-ml/ps--PGS-60022-00477",
"https://www.blibli.com/p/surabaya-herbal-essences-colour-me-happy-colour-safe-shampo-300-ml/ps--PGS-60022-00480",
"https://www.blibli.com/p/surabaya-herbal-essences-hello-hydration-deep-moisture-kondisioner-300-ml/ps--PGS-60022-00478",
"https://www.blibli.com/p/surabaya-herbal-essences-moroccan-my-shine-restored-radiance-kondisioner-300-ml/ps--PGS-60022-00479",
"https://www.blibli.com/p/surabaya-oral-b-123-soft-sikat-gigi-3-pcs/ps--PGS-60022-00278",
"https://www.blibli.com/p/surabaya-oral-b-stages-2-sikat-gigi-anak/ps--PGS-60022-00280",
"https://www.blibli.com/p/surabaya-pantene-aqua-pure-shampoo-400-ml/ps--PGS-60022-00424",
"https://www.blibli.com/p/surabaya-pantene-long-black-shampoo-400-ml/ps--PGS-60022-00492",
"https://www.blibli.com/p/surabaya-pantene-nature-care-fullness-life-shampoo-290-ml/ps--PGS-60022-00290",
"https://www.blibli.com/p/surabaya-pantene-pro-v-anti-lepek-shampo-480-ml/ps--PGS-60022-00291",
"https://www.blibli.com/p/surabaya-pantene-shampoo-anti-lepek-900ml/ps--PGS-60022-00496",
"https://www.blibli.com/p/surabaya-pantene-smooth-silky-conditioner-290-ml/ps--PGS-60022-00448",
"https://www.blibli.com/p/surabaya-pantene-total-damage-care-quantum-shampoo-750-ml/ps--PGS-60022-00415",
"https://www.blibli.com/p/surabaya-rejoice-rich-conditioner-320-ml/ps--PGS-60022-00459",
"https://www.blibli.com/p/gillette-isi-ulang-fusion-proglide-pisau-cukur-2-pcs/ps--PGG-18081-00299",
"https://www.blibli.com/p/smg-jog-solo-gillette-pisau-cukur-wanita-daisy-plus-isi-2/ps--PGJ-60021-00089",
"https://www.blibli.com/p/smg-jog-solo-gillette-pisau-cukur-vector-razor/ps--PGJ-60021-00092",
"https://www.blibli.com/p/smg-jog-solo-oral-b-123-medium-sikat-gigi-3-pcs/ps--PGJ-60021-00094",
"https://www.blibli.com/p/smg-jog-solo-oral-b-123-soft-sikat-gigi-3-pcs/ps--PGJ-60021-00093",
"https://www.blibli.com/p/smg-jog-solo-head-shoulders-lemon-fresh-anti-dandruff-shampoo-300-ml/ps--PGJ-60021-00106",
"https://www.blibli.com/p/smg-jog-solo-oral-b-stages-4-sikat-gigi-anak/ps--PGJ-60021-00098",
"https://www.blibli.com/p/smg-jog-solo-oral-b-stages-3-sikat-gigi-anak/ps--PGJ-60021-00097",
"https://www.blibli.com/p/smg-jog-solo-head-shoulders-shampoo-anti-gatal-300-ml/ps--PGJ-60021-00142",
"https://www.blibli.com/p/smg-jog-solo-oral-b-stages-2-sikat-gigi-anak/ps--PGJ-60021-00096",
"https://www.blibli.com/p/smg-jog-solo-oral-b-stages-1-sikat-gigi-anak/ps--PGJ-60021-00095",
"https://www.blibli.com/p/smg-jog-solo-pantene-paket-shampoo-micellar-cleanse-and-hydrate-300-ml-conditioner-300-ml/ps--PGJ-60021-00153",
"https://www.blibli.com/p/smg-jog-solo-head-shoulders-shampoo-anti-gatal-400-ml/ps--PGJ-60021-00139",
"https://www.blibli.com/p/smg-jog-solo-gillette-pisau-cukur-blue-3-biru-isi-4/ps--PGJ-60021-00088",
"https://www.blibli.com/p/smg-jog-solo-pantene-paket-shampoo-micellar-cleanse-and-hydrate-530-ml-conditioner-530-ml/ps--PGJ-60021-00155",
"https://www.blibli.com/p/smg-jog-solo-pantene-shampoo-total-damage-care-400-ml/ps--PGJ-60021-00113",
"https://www.blibli.com/p/smg-jog-solo-pantene-shampoo-total-damage-care-quantum-750-ml/ps--PGJ-60021-00110",
"https://www.blibli.com/p/smg-jog-solo-pantene-shampoo-hairfall-control-quantum-750-ml/ps--PGJ-60021-00109",
"https://www.blibli.com/p/smg-jog-solo-pantene-shampoo-anti-lepek-900-ml/ps--PGJ-60021-00108",
"https://www.blibli.com/p/smg-jog-solo-downy-mystique-pewangi-dan-pelembut-pakaian-konsentrat-900-ml-kemasan-refill/ps--PGJ-60021-00134",
"https://www.blibli.com/p/smg-jog-solo-pantene-pro-v-gold-series-smooth-sleek-kondisioner-190-ml/ps--PGJ-60021-00084",
"https://www.blibli.com/p/smg-jog-solo-pantene-conditioner-micellar-cleanse-and-hydrate-300-ml/ps--PGJ-60021-00160",
"https://www.blibli.com/p/smg-jog-solo-pantene-shampoo-micellar-cleanse-and-hydrate-300-ml/ps--PGJ-60021-00151",
"https://www.blibli.com/p/smg-jog-solo-gillette-pisau-cukur-wanita-simply-venus-isi-4/ps--PGJ-60021-00091",
"https://www.blibli.com/p/smg-jog-solo-downy-pelembut-pakaian-mystique-botol-900-ml/ps--PGJ-60021-00063",
"https://www.blibli.com/p/smg-jog-solo-head-shoulders-anti-apek-charcoal-shampoo-300-ml/ps--PGJ-60021-00107",
"https://www.blibli.com/p/smg-jog-solo-head-shoulders-cool-menthol-shampoo-anti-dandruff-anti-ketombe-300-ml/ps--PGJ-60021-00104",
"https://www.blibli.com/p/smg-jog-solo-downy-sports-fresh-pelembut-pewangi-pakaian-680-ml/ps--PGJ-60021-00135",
"https://www.blibli.com/p/smg-jog-solo-downy-anti-apek-pelembut-dan-pewangi-pakaian-680-ml-kemasan-refill/ps--PGJ-60021-00055",
"https://www.blibli.com/p/smg-jog-solo-pantene-shampoo-total-damage-care-290-ml/ps--PGJ-60021-00138",
"https://www.blibli.com/p/smg-jog-solo-pantene-shampoo-anti-dandruff-290-ml/ps--PGJ-60021-00137",
"https://www.blibli.com/p/smg-jog-solo-pantene-shampoo-daily-moisture-repair-290-ml/ps--PGJ-60021-00130",
"https://www.blibli.com/p/smg-jog-solo-oral-b-pro-health-multi-protection-refreshing-clean-mint-rinse-500-ml/ps--PGJ-60021-00124",
"https://www.blibli.com/p/smg-jog-solo-pantene-conditioner-pro-v-anti-lepek-290-ml/ps--PGJ-60021-00116",
"https://www.blibli.com/p/smg-jog-solo-pantene-shampoo-smooth-silky-290-ml/ps--PGJ-60021-00114",
"https://www.blibli.com/p/smg-jog-solo-head-shoulders-lemon-fresh-anti-dandruff-shampoo-anti-dandruff-anti-ketombe-680-ml/ps--PGJ-60021-00100",
"https://www.blibli.com/p/smg-jog-solo-head-shoulders-cool-menthol-shampoo-680-ml/ps--PGJ-60021-00099",
"https://www.blibli.com/p/smg-jog-solo-head-shoulders-clean-balanced-shampoo-300-ml/ps--PGJ-60021-00103",
"https://www.blibli.com/p/smg-jog-solo-gillette-pisau-cukur-razor-wanita-daisy-classic-isi-5/ps--PGJ-60021-00090",
"https://www.blibli.com/p/smg-jog-solo-pantene-anti-dandruff-shampoo-900-ml/ps--PGJ-60021-00069",
"https://www.blibli.com/p/smg-jog-solo-gillette-isi-ulang-vector-2-pcs/ps--PGJ-60021-00031",
"https://www.blibli.com/p/smg-jog-solo-head-shoulders-shampoo-anti-apek-400-ml/ps--PGJ-60021-00148",
"https://www.blibli.com/p/smg-jog-solo-head-shoulders-shampoo-supreme-anti-hairfall-480-ml/ps--PGJ-60021-00145",
"https://www.blibli.com/p/smg-jog-solo-pantene-hair-fall-control-shampoo-900-ml/ps--PGJ-60021-00071",
"https://www.blibli.com/p/smg-jog-solo-pantene-shampoo-hair-fall-control-400-ml/ps--PGJ-60021-00077",
"https://www.blibli.com/p/smg-jog-solo-pantene-conditioner-micellar-cleanse-and-hydrate-530-ml/ps--PGJ-60021-00161",
"https://www.blibli.com/p/smg-jog-solo-pantene-shampoo-micellar-cleanse-and-hydrate-530-ml/ps--PGJ-60021-00152",
"https://www.blibli.com/p/smg-jog-solo-pantene-pro-v-gold-series-smooth-sleek-sampo-270-ml/ps--PGJ-60021-00085",
"https://www.blibli.com/p/smg-jog-solo-pantene-pro-v-gold-series-black-glossy-sampo-270-ml/ps--PGJ-60021-00083",
"https://www.blibli.com/p/smg-jog-solo-pantene-smooth-silky-control-shampoo-400-ml/ps--PGJ-60021-00078",
"https://www.blibli.com/p/smg-jog-solo-pantene-shampoo-anti-dandruff-400-ml/ps--PGJ-60021-00075",
"https://www.blibli.com/p/smg-jog-solo-pantene-pro-v-anti-lepek-shampoo-480-ml/ps--PGJ-60021-00074",
"https://www.blibli.com/p/smg-jog-solo-pantene-shampoo-total-damage-care-900-ml/ps--PGJ-60021-00070",
"https://www.blibli.com/p/smg-jog-solo-pantene-pro-v-gold-series-strong-thick-sampo-270-ml/ps--PGJ-60021-00087",
"https://www.blibli.com/p/surabaya-gillette-3-pisau-cukur-biru-2-pcs/ps--PGS-60022-00180",
"https://www.blibli.com/p/surabaya-gillette-3-pisau-cukur-biru-4-pcs/ps--PGS-60022-00183",
"https://www.blibli.com/p/surabaya-gillette-blue-2-disposable-pisau-cukur-isi-10/ps--PGS-60022-00157",
"https://www.blibli.com/p/surabaya-gillette-blue-2-pivot-disposable-pisau-cukur-isi-5/ps--PGS-60022-00169",
"https://www.blibli.com/p/surabaya-gillette-daisy-plus-pisau-cukur-wanita-isi-2/ps--PGS-60022-00173",
"https://www.blibli.com/p/surabaya-gillette-fusion-proglide-base-flexball-pisau-cukur/ps--PGS-60022-00177",
"https://www.blibli.com/p/surabaya-gillette-fusion-proglide-base-pisau-cukur/ps--PGS-60022-00155",
"https://www.blibli.com/p/surabaya-gillette-gel-shave-cool-fusion-proglide-195-g/ps--PGS-60022-00165",
"https://www.blibli.com/p/surabaya-gillette-gel-shave-moisture-195-ml/ps--PGS-60022-00166",
"https://www.blibli.com/p/surabaya-gillette-isi-ulang-fusion-proglide-2-pcs/ps--PGS-60022-00163",
"https://www.blibli.com/p/surabaya-gillette-isi-ulang-fusion-proglide-perlengkapan-cukur-pria-4-pcs/ps--PGS-60022-00162",
"https://www.blibli.com/p/surabaya-gillette-isi-ulang-vector-isi-2/ps--PGS-60022-00187",
"https://www.blibli.com/p/surabaya-gillette-mach3-turbo-cart-pisau-cukur-2-s/ps--PGS-60022-00176",
"https://www.blibli.com/p/surabaya-gillette-mach3-turbo-cart-pisau-cukur-4-s/ps--PGS-60022-00175",
"https://www.blibli.com/p/surabaya-gillette-pisau-cukur-vector/ps--PGS-60022-00188",
"https://www.blibli.com/p/surabaya-gillette-simply-venus-basic-pisau-cukur-2-pcs/ps--PGS-60022-00179",
"https://www.blibli.com/p/surabaya-gillette-vector-isi-ulang-4-pcs/ps--PGS-60022-00186",
"https://www.blibli.com/p/surabaya-head-shoulders-anti-apek-charcoal-shampoo-300-ml/ps--PGS-60022-00501",
"https://www.blibli.com/p/surabaya-head-shoulders-clean-balanced-shampoo-160-ml/ps--PGS-60022-00194",
"https://www.blibli.com/p/surabaya-head-shoulders-clean-balanced-shampoo-300-ml/ps--PGS-60022-00502",
"https://www.blibli.com/p/surabaya-head-shoulders-cool-blast-shampoo-315-ml/ps--PGS-60022-00192",
"https://www.blibli.com/p/surabaya-head-shoulders-cool-menthol-shampoo-400-ml/ps--PGS-60022-00227",
"https://www.blibli.com/p/surabaya-head-shoulders-cool-menthol-shampoo-400-ml/ps--PGS-60022-00212",
"https://www.blibli.com/p/surabaya-head-shoulders-lemon-fresh-anti-dandruff-shampoo-160-ml/ps--PGS-60022-00225",
"https://www.blibli.com/p/surabaya-head-shoulders-lemon-fresh-anti-dandruff-shampoo-300-ml/ps--PGS-60022-00221",
"https://www.blibli.com/p/surabaya-head-shoulders-lemon-fresh-anti-dandruff-shampoo-400-ml/ps--PGS-60022-00203",
"https://www.blibli.com/p/surabaya-head-shoulders-lemon-fresh-anti-dandruff-shampoo-680-ml/ps--PGS-60022-00200",
"https://www.blibli.com/p/surabaya-head-shoulders-lemon-fresh-shampoo-850-ml/ps--PGS-60022-00500",
"https://www.blibli.com/p/surabaya-herbal-essences-bio-renew-clean-white-strawberry-sweet-mint-kondisioner-400-ml/ps--PGS-60022-00486",
"https://www.blibli.com/p/surabaya-herbal-essences-bio-renew-hydrate-coconut-milk-kondisioner-400-ml/ps--PGS-60022-00484",
"https://www.blibli.com/p/surabaya-herbal-essences-bio-renew-hydrate-coconut-milk-shampo-400-ml/ps--PGS-60022-00488",
"https://www.blibli.com/p/surabaya-herbal-essences-bio-renew-repair-argan-oil-of-morocco-kondisioner-400-ml/ps--PGS-60022-00483",
"https://www.blibli.com/p/surabaya-herbal-essences-bio-renew-repair-argan-oil-of-morocco-shampo-400-ml/ps--PGS-60022-00487",
"https://www.blibli.com/p/surabaya-herbal-essences-bio-renew-smooth-golden-moringa-oil-kondisioner-400-ml/ps--PGS-60022-00485",
"https://www.blibli.com/p/surabaya-herbal-essences-bio-renew-smooth-golden-moringa-oil-shampo-400-ml/ps--PGS-60022-00489",
"https://www.blibli.com/p/surabaya-herbal-essences-hello-hydration-deep-moisture-shampo-300-ml/ps--PGS-60022-00481",
"https://www.blibli.com/p/surabaya-herbal-essences-hello-hydration-shampo-300-ml/ps--PGS-60022-00239",
"https://www.blibli.com/p/surabaya-herbal-essences-moisture-rosemary-herbs-conditioner-400-ml/ps--PGS-60022-00474",
"https://www.blibli.com/p/surabaya-herbal-essences-moisture-rosemary-herbs-shampoo-400-ml/ps--PGS-60022-00473",
"https://www.blibli.com/p/surabaya-herbal-essences-moroccan-my-shine-restored-radiance-shampo-300-ml/ps--PGS-60022-00482",
"https://www.blibli.com/p/surabaya-herbal-essences-volume-white-grapefruit-mosa-mint-conditioner-400-ml/ps--PGS-60022-00476",
"https://www.blibli.com/p/surabaya-herbal-essences-volume-white-grapefruit-mosa-mint-shampoo-400-ml/ps--PGS-60022-00475",
"https://www.blibli.com/p/surabaya-herbal-essenceshello-hydration-conditioner-300-ml/ps--PGS-60022-00251",
"https://www.blibli.com/p/surabaya-oral-b-complete-whitening-soft-sikat-gigi-2-pcs/ps--PGS-60022-00274",
"https://www.blibli.com/p/surabaya-oral-b-crossaction-pro-health-massage-sikat-gigi-medium/ps--PGS-60022-00263",
"https://www.blibli.com/p/surabaya-oral-b-123-soft-sikat-gigi-2-pcs/ps--PGS-60022-00277",
"https://www.blibli.com/p/surabaya-oral-b-stages-1-sikat-gigi-anak/ps--PGS-60022-00281",
"https://www.blibli.com/p/surabaya-oral-b-ultra-thin-compact-soft-sikat-gigi-3-pcs/ps--PGS-60022-00258",
"https://www.blibli.com/p/surabaya-oral-b-ultra-thin-pro-gum-care-sikat-gigi-1-pc/ps--PGS-60022-00259",
"https://www.blibli.com/p/surabaya-oral-b-ultrathin-green-tea-sikat-gigi/ps--PGS-60022-00255",
"https://www.blibli.com/p/surabaya-pantene-anti-dandruff-shampoo-290-ml/ps--PGS-60022-00330",
"https://www.blibli.com/p/surabaya-pantene-anti-dandruff-shampoo-900-ml/ps--PGS-60022-00339",
"https://www.blibli.com/p/surabaya-pantene-hair-fall-control-shampoo-400-ml/ps--PGS-60022-00399",
"https://www.blibli.com/p/surabaya-pantene-hair-fall-control-shampoo-900-ml/ps--PGS-60022-00324",
"https://www.blibli.com/p/surabaya-pantene-hairfall-shampoo-1200-ml/ps--PGS-60022-00497",
"https://www.blibli.com/p/surabaya-pantene-nature-care-fullness-life-shampoo-290-ml/ps--PGS-60022-00334",
"https://www.blibli.com/p/surabaya-pantene-pro-v-anti-lepek-shampo-290-ml/ps--PGS-60022-00292",
"https://www.blibli.com/p/surabaya-pantene-pro-v-anti-lepek-shampoo-750-ml/ps--PGS-60022-00314",
"https://www.blibli.com/p/surabaya-pantene-shampoo-anti-dandruff-400-ml/ps--PGS-60022-00491",
"https://www.blibli.com/p/surabaya-pantene-shampoo-anti-dandruff-900-ml-2-pcs/ps--PGS-60022-00403",
"https://www.blibli.com/p/surabaya-pantene-total-damage-care-shampoo-1200-ml/ps--PGS-60022-00498",
"https://www.blibli.com/p/surabaya-pantene-total-damage-care-shampoo-900-ml-3-pcs/ps--PGS-60022-00360",
"https://www.blibli.com/p/surabaya-pantene-total-damage-care-shampoo-900-ml/ps--PGS-60022-00354",
"https://www.blibli.com/p/surabaya-rejoice-3-in-1-shampoo-340-ml/ps--PGS-60022-00379",
"https://www.blibli.com/p/surabaya-rejoice-3-in-1-perfect-cool-shampoo-170-ml/ps--PGS-60022-00389",
"https://www.blibli.com/p/surabaya-rejoice-3-in-1-perfect-perfume-shampoo-170-ml/ps--PGS-60022-00370",
"https://www.blibli.com/p/surabaya-rejoice-moisture-smooth-shampoo-600-ml/ps--PGS-60022-00375",
"https://www.blibli.com/p/surabaya-rejoice-rich-shampoo-340-ml/ps--PGS-60022-00414",
"https://www.blibli.com/p/surabaya-rejoice-rich-shampoo-600-ml/ps--PGS-60022-00407",
"https://www.blibli.com/p/surabaya-rejoice-soft-smooth-shampoo-320-ml/ps--PGS-60022-00376",
"https://www.blibli.com/p/surabaya-whisper-regular-flow-wings-10-pads/ps--PGS-60022-00342",
"https://www.blibli.com/p/surabaya-whisper-regular-flow-wings-pembalut-20-pads/ps--PGS-60022-00343",
"https://www.blibli.com/p/surabaya-gillette-mach3-turbo-cart-pisau-cukur-4-s/pc--MTA-3814939",
"https://www.blibli.com/p/surabaya-rejoice-soft-smooth-shampoo-320-ml/pc--MTA-3832880",
"https://www.blibli.com/p/smg-jog-solo-pantene-micellar-detox-moisturizer-shampoo-300-ml-conditioner-300-ml/ps--PGJ-60021-00312",
"https://www.blibli.com/p/smg-jog-solo-pantene-hitam-glow-shampoo-750-ml/ps--PGJ-60021-00310",
"https://www.blibli.com/p/smg-jog-solo-pantene-hitam-glow-conditioner-290-ml/ps--PGJ-60021-00307",
"https://www.blibli.com/p/smg-jog-solo-herbal-essences-argan-oil-of-morocco-shampoo-240-ml/ps--PGJ-60021-00306",
"https://www.blibli.com/p/smg-jog-solo-herbal-essences-white-strawberry-mint-shampoo-240-ml/ps--PGJ-60021-00305",
"https://www.blibli.com/p/smg-jog-solo-herbal-essences-argan-oil-of-morocco-conditioner-240-ml/ps--PGJ-60021-00304",
"https://www.blibli.com/p/smg-jog-solo-baru-gillette-flexi-vibe-1-gagang-pisau-cukur-3-pisau-cukur-refill-isi-ulang/ps--PGJ-60021-00302",
"https://www.blibli.com/p/smg-jog-solo-baru-gillette-flexi-vibe-5-pisau-cukur-refill-isi-ulang/ps--PGJ-60021-00301",
"https://www.blibli.com/p/smg-jog-solo-baru-gillette-flexi-vibe-1-gagang-pisau-cukur-1-pisau-cukur-refill-isi-ulang/ps--PGJ-60021-00300",
"https://www.blibli.com/p/smg-jog-solo-baru-gillette-flexi-vibe-2-pisau-cukur-refill-isi-ulang/ps--PGJ-60021-00314",
"https://www.blibli.com/p/smg-jog-solo-gillette-foamy-shave-cream-menthol-175-gr/ps--PGJ-60021-00329",
"https://www.blibli.com/p/product-detail/ps--PGG-18081-00081",
"https://www.blibli.com/p/product-detail/ps--PGG-18081-00288",
"https://www.blibli.com/p/product-detail/ps--PGG-18081-00675",
"https://www.blibli.com/p/product-detail/ps--PGG-18081-00663",
"https://www.blibli.com/p/product-detail/ps--PGJ-60021-00300",
"https://www.blibli.com/p/product-detail/ps--PGJ-60021-00302",
"https://www.blibli.com/p/product-detail/ps--PGJ-60021-00301",
"https://www.blibli.com/p/product-detail/ps--PGJ-60021-00125",
"https://www.blibli.com/p/product-detail/ps--PGJ-60021-00055",
"https://www.blibli.com/p/product-detail/ps--PGJ-60021-00135",
"https://www.blibli.com/p/product-detail/ps--PGJ-60021-00323",
"https://www.blibli.com/p/product-detail/ps--PGJ-60021-00329",
"https://www.blibli.com/p/product-detail/ps--PGJ-60021-00091",
"https://www.blibli.com/p/product-detail/ps--PGJ-60021-00289",
"https://www.blibli.com/p/product-detail/ps--PGJ-60021-00287",
"https://www.blibli.com/p/product-detail/ps--PGJ-60021-00107",
"https://www.blibli.com/p/product-detail/ps--PGJ-60021-00143",
"https://www.blibli.com/p/product-detail/ps--PGJ-60021-00141",
"https://www.blibli.com/p/product-detail/ps--PGJ-60021-00146",
"https://www.blibli.com/p/product-detail/ps--PGJ-60021-00291",
"https://www.blibli.com/p/product-detail/ps--PGJ-60021-00292",
"https://www.blibli.com/p/product-detail/ps--PGJ-60021-00304",
"https://www.blibli.com/p/product-detail/ps--PGJ-60021-00306",
"https://www.blibli.com/p/product-detail/ps--PGJ-60021-00303",
"https://www.blibli.com/p/product-detail/ps--PGJ-60021-00305",
"https://www.blibli.com/p/product-detail/ps--PGJ-60021-00178",
"https://www.blibli.com/p/product-detail/ps--PGJ-60021-00320",
"https://www.blibli.com/p/product-detail/ps--PGJ-60021-00319",
"https://www.blibli.com/p/product-detail/ps--PGJ-60021-00321",
"https://www.blibli.com/p/product-detail/ps--PGJ-60021-00317",
"https://www.blibli.com/p/product-detail/ps--PGJ-60021-00318",
"https://www.blibli.com/p/product-detail/ps--PGJ-60021-00315",
"https://www.blibli.com/p/product-detail/ps--PGJ-60021-00326",
"https://www.blibli.com/p/product-detail/ps--PGJ-60021-00160",
"https://www.blibli.com/p/product-detail/ps--PGJ-60021-00241",
"https://www.blibli.com/p/product-detail/ps--PGJ-60021-00307",
"https://www.blibli.com/p/product-detail/ps--PGJ-60021-00310",
"https://www.blibli.com/p/product-detail/ps--PGJ-60021-00312",
"https://www.blibli.com/p/product-detail/ps--PGJ-60021-00251",
"https://www.blibli.com/p/product-detail/ps--PGJ-60021-00265",
"https://www.blibli.com/p/product-detail/ps--PGJ-60021-00248",
"https://www.blibli.com/p/product-detail/ps--PGJ-60021-00247",
"https://www.blibli.com/p/product-detail/ps--PGJ-60021-00080",
"https://www.blibli.com/p/product-detail/ps--PGJ-60021-00074",
"https://www.blibli.com/p/product-detail/ps--PGJ-60021-00083",
"https://www.blibli.com/p/product-detail/ps--PGJ-60021-00084",
"https://www.blibli.com/p/product-detail/ps--PGJ-60021-00085",
"https://www.blibli.com/p/product-detail/ps--PGJ-60021-00087",
"https://www.blibli.com/p/product-detail/ps--PGJ-60021-00137",
"https://www.blibli.com/p/product-detail/ps--PGJ-60021-00130",
"https://www.blibli.com/p/product-detail/ps--PGJ-60021-00151",
"https://www.blibli.com/p/product-detail/ps--PGJ-60021-00240",
"https://www.blibli.com/p/product-detail/ps--PGJ-60021-00114",
"https://www.blibli.com/p/product-detail/ps--PGJ-60021-00138",
"https://www.blibli.com/p/product-detail/ps--PGJ-60021-00113",
"https://www.blibli.com/p/product-detail/ps--PGJ-60021-00262",
"https://www.blibli.com/p/product-detail/ps--PGJ-60021-00331",
"https://www.blibli.com/p/product-detail/ps--PGJ-60021-00330",
"https://www.blibli.com/p/product-detail/ps--PGJ-60021-00298",
"https://www.blibli.com/p/product-detail/ps--PGJ-60021-00259",
"https://www.blibli.com/p/product-detail/ps--PGJ-60021-00255",
"https://www.blibli.com/p/surabaya-gillette-foamy-menthol-shave-cream-175-g/ps--PGS-60022-00178",
"https://www.blibli.com/p/surabaya-gillette-lemon-lime-foamy-shave-cream-175-gr/ps--PGS-60022-00172",
"https://www.blibli.com/p/surabaya-gillette-mach-3-turbo-pisau-cukur/ps--PGS-60022-00161",
"https://www.blibli.com/p/surabaya-gillette-mach3-turbo-cart-pisau-cukur-2-s/ps--PGS-60022-00536",
"https://www.blibli.com/p/surabaya-gillette-mach3-turbo-cart-pisau-cukur-4-s/ps--PGS-60022-00535",
"https://www.blibli.com/p/surabaya-oral-b-ultrathin-black-tea-sikat-gigi/ps--PGS-60022-00254",
"https://www.blibli.com/p/surabaya-pantene-anti-dandruff-quantum-shampoo-750-ml/ps--PGS-60022-00358",
"https://www.blibli.com/p/surabaya-pantene-smooth-silky-control-shampoo-400-ml/ps--PGS-60022-00494",
"https://www.blibli.com/p/gillette-pisau-cukur-wanita-daisy-plus-isi-2/pc--MTA-1010275",
"https://www.blibli.com/p/gillette-isi-ulang-vector-refill-pisau-cukur-razor-isi-2/ps--PGG-18081-00286",
"https://www.blibli.com/p/gillette-fusion-proglide-base-pisau-cukur/ps--PGG-18081-00295"]
import requests
from bs4 import BeautifulSoup 
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from alive_progress import alive_bar
# capa = DesiredCapabilities.CHROME
# capa["pageLoadStrategy"] = "none"

path_profile=r'C:\Users\BIJKT-ANDIKA\AppData\Roaming\Mozilla\Firefox\Profiles\t4qhc9e7.default-release'
profile=webdriver.FirefoxOptions(path_profile)
profile.set_preference("dom.webdriver.enabled", False)
profile.set_preference('useAutomationExtension', False)
# options.add_argument('no-sandbox')
# options.add_argument('--disable-dev-shm-usage')
# prefs = {"profile.managed_default_content_settings.images": 2}
# options.add_experimental_option("prefs", prefs)
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Firefox(profile=profile)
wait=WebDriverWait(driver,20)
list_stock=[]
with alive_bar(len(list_link),title='gathering data....') as bar:
    for i in list_link:
        driver.get(i)
        try:
            wait=WebDriverWait(driver,20)
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#pdp-gateway > div > section.pdp-action')))
        except:
            pass 
        soup=BeautifulSoup(driver.page_source,'html.parser')
        try:    
            beli=driver.find_element(By.CSS_SELECTOR,'div.text').text
            list_stock.append(1)
        except:
            list_stock.append(0)
    
        if len(list_stock)%80==0:
            print(list_stock) 
            driver.quit()
            driver=webdriver.Chrome(service=Service(r'D:\Python Scripts\project_scraping_blibli-Master\chromedriver.exe'),options=options)

        bar()
with alive_bar(len(list_stock),title='validating data....') as bar:
    for i,j in enumerate(list_stock):
        if j==0:
            print(list_link[i])
            driver.get(list_link[i])
            time.sleep(1)
            soup=BeautifulSoup(driver.page_source,'html.parser')
            try:    
                beli=soup.find('button',{'class':"blu-btn b-primary btn-checkout"}).text
                list_stock[i]=1
            except:
                pass
        bar()
driver.quit()             
import pandas as pd
import datetime
y=datetime.date.today()
df=pd.DataFrame(data=[list_link,list_stock]).T
df.to_excel(f'blibli_non_jabo_{y}.xlsx')
        

# driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})