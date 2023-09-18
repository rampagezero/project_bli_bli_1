from bs4 import BeautifulSoup 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from alive_progress import alive_bar
from selenium.webdriver.chrome.options import Options
list_link=["https://tokopedia.com/pgofficialstore/downy-pewangi-dan-pelembut-pakaian-konsentrat-mystique-650ml",
"https://tokopedia.com/pgofficialstore/downy-pewangi-dan-pelembut-pakaian-konsentrat-mystique-650ml-isi-3",
"https://www.tokopedia.com/pgofficialstore/downy-pelembut-pakaian-wangi-parfum-mewah-1350-ml-isi-1-3-packs-mystique-isi-1",
"https://tokopedia.com/pgofficialstore/downy-pelembut-pewangi-pakaian-sunrise-fresh-refill-700ml",
"https://www.tokopedia.com/unilever/molto-all-in-1-blue-pewangi-pelembut-konsentrat-pouch-720ml",
"https://tokopedia.com/pgofficialstore/downy-pewangi-pelembut-pakaian-sunrise-fresh-refill-700ml-x3",
"https://www.tokopedia.com/pgofficialstore/1400-ml-downy-pelembut-pakaian-wangi-tahan-lama-isi-1-3-packs-sunrise-fresh-isi-1",
"https://www.tokopedia.com/unilever/molto-all-in-one-pelembut-baju-refill-blue-1600ml-cairan-pewangi",
"https://tokopedia.com/pgofficialstore/pantene-shampoo-hair-fall-control-750-ml",
"https://tokopedia.com/pgofficialstore/pantene-shampoo-hair-fall-control-900ml",
"https://www.tokopedia.com/unilever/dove-shampoo-total-hairfall-treatment-680ml-shampoo-anti-rambut-rontok",
"https://tokopedia.com/pgofficialstore/pantene-shampoo-hair-fall-control-750-ml-paket-isi-2",
"https://tokopedia.com/pgofficialstore/pantene-shampoo-hair-fall-control-900ml-paket-isi-2",
"https://www.tokopedia.com/unilever/dove-shampoo-nutritive-solutions-total-hair-fall-treatment-680ml-twin",
"https://tokopedia.com/pgofficialstore/head-shoulders-shampoo-cool-menthol-680ml",
"https://www.tokopedia.com/unilever/clear-men-anti-dandruff-shampo-anti-ketombe-ice-cool-menthol-660ml?whid=0",
"https://tokopedia.com/pgofficialstore/head-shoulders-shampoo-cool-menthol-680ml-paket-isi-2",
"https://www.tokopedia.com/unilever/clear-anti-dandruff-shampoo-ice-cool-menthol-660ml-twin-pack",
"https://tokopedia.com/pgofficialstore/herbal-essences-shampoo-bio-renew-argan-oil-of-morocco-400-ml",
"https://www.tokopedia.com/unilever/love-beauty-and-planet-shampoo-coconut-water-mimosa-flower-400ml",
"https://tokopedia.com/pgofficialstore/herbal-essences-conditioner-bio-renew-argan-oil-of-morocco-400-ml",
"https://tokopedia.com/pgofficialstore/pampers-popok-bayi-celana-premium-soft-m-30-7-12-kg",
"https://tokopedia.com/pgofficialstore/pampers-popok-bayi-celana-premium-soft-m-30-7-12-kg-karton-isi-6",
"https://tokopedia.com/pgofficialstore/pampers-popok-bayi-celana-premium-soft-m-46-7-12-kg",
"https://tokopedia.com/pgofficialstore/pampers-popok-bayi-celana-premium-soft-m-46-7-12-kg-karton-isi-4",
"https://tokopedia.com/pgofficialstore/pampers-popok-bayi-celana-premium-soft-m-68-7-12-kg-karton-isi-3",
"https://www.tokopedia.com/unicharm/mamypoko-pants-royal-soft-m-64-boys-popok-celana-karton-isi-4",
"https://tokopedia.com/pgofficialstore/pampers-popok-bayi-celana-premium-soft-l-24-9-14-kg",
"https://tokopedia.com/pgofficialstore/pampers-popok-bayi-celana-premium-soft-l-24-9-14-kg-karton-isi-6",
"https://tokopedia.com/pgofficialstore/pampers-popok-bayi-celana-premium-soft-l-42-9-14-kg",
"https://tokopedia.com/pgofficialstore/pampers-popok-bayi-celana-premium-soft-l-42-9-14-kg-karton-isi-4",
"https://tokopedia.com/pgofficialstore/pampers-popok-bayi-celana-premium-soft-l-62-9-14-kg-karton-isi-3",
"https://tokopedia.com/pgofficialstore/pampers-popok-bayi-celana-premium-soft-xl-21-12-17-kg",
"https://tokopedia.com/pgofficialstore/pampers-popok-bayi-celana-premium-soft-xl-21-12-17-kg-karton-isi-6",
"https://tokopedia.com/pgofficialstore/pampers-popok-bayi-celana-premium-soft-xl-36-12-17-kg",
"https://tokopedia.com/pgofficialstore/pampers-popok-bayi-celana-premium-soft-xl-36-12-17-kg-karton-isi-4",
"https://tokopedia.com/pgofficialstore/pampers-popok-bayi-celana-premium-soft-xl-54-12-17-kg-karton-isi-3",
"https://www.tokopedia.com/unicharm/mamypoko-pants-royal-soft-xl-46-boys-popok-celana-karton-isi-4",
"https://tokopedia.com/pgofficialstore/pampers-popok-bayi-celana-premium-soft-xxl-28-15-25-kg",
"https://tokopedia.com/pgofficialstore/pampers-popok-bayi-perekat-premium-care-nb-26-up-to-5-kg",
"https://tokopedia.com/pgofficialstore/pampers-popok-bayi-perekat-premium-care-nb-52-up-to-5-kg",
"https://tokopedia.com/pgofficialstore/pampers-popok-bayi-perekat-premium-care-nb-52-up-to-5-kg-isi-2",
"https://tokopedia.com/pgofficialstore/pampers-popok-bayi-perekat-premium-care-nb-52-up-to-5-kg-isi-4",
"https://www.tokopedia.com/olayofficial/olay-regenerist-mircro-sculpting-cream-50gr?src=topads",
"https://tokopedia.com/pgofficialstore/olay-total-effects-7in1-day-cream-normal-50gr",
"https://www.tokopedia.com/lorealparis/l-oreal-paris-revitalift-day-cream-krim-anti-aging-siang",
"https://tokopedia.com/pgofficialstore/rejoice-shampoo-rich-halus-lembut-600-ml",
"https://tokopedia.com/pgofficialstore/rejoice-shampoo-rich-halus-lembut-600-ml-paket-isi-2"]
options = Options()
options.add_argument('--headless=new')
from selenium.webdriver.chrome.service import Service
driver=webdriver.Chrome(service=Service(r'D:\Python Scripts\project_scraping_blibli-Master\chromedriver.exe'),options=options)
# driver.set_page_load_timeout(10)
wait=WebDriverWait(driver,10)
list_price=[]
with alive_bar(len(list_link),title='gathering price') as bar:
    for i in list_link:
        driver.get(i)
        try:
            wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'.price')))
            price=driver.find_element(By.CSS_SELECTOR,'.price').text
            list_price.append(price)
        except:
            list_price.append(" ")
        bar()
driver.quit()
import pandas as pd
import datetime
y=datetime.date.today()
df=pd.DataFrame(data=[list_link,list_price]).T
df.to_excel(f'price_compe_tokped_{y}.xlsx')
