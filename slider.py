from bs4 import BeautifulSoup 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from alive_progress import alive_bar
from selenium.webdriver.common.action_chains import ActionChains
import undetected_chromedriver as uc
options = Options()
options.add_argument('--no-sandbox')
options.add_argument('--start-maximized')
# options.add_argument('--start-fullscreen')
# options.add_argument('--single-process')
# options.add_argument('--disable-dev-shm-usage')
# options.add_argument("--incognito")
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_argument("disable-infobars")
prefs = {"profile.managed_default_content_settings.images": 2}
options.add_experimental_option("prefs", prefs)
list_lazada=["https://www.lazada.co.id/products/pantene-sampo-total-damage-care-900ml-kondisioner-perawatan-rambut-halus-lembut-rambut-bercabang-rambut-rusak-i159992638-s181803655.html",
"https://www.lazada.co.id/products/pantene-shampo-anti-lepek-290ml-i171106862-s201501242.html",
"https://www.lazada.co.id/products/pantene-shampoo-anti-lepek-750ml-paket-isi-3-i805072640-s1137780990.html",
"https://www.lazada.co.id/products/pantene-shampoo-hair-fall-control-1800-ml-i4644788251-s8163000782.html"]
import requests
response=requests.get(list_lazada[0])
soup=BeautifulSoup(response.content,'html.parser')
print(soup)


