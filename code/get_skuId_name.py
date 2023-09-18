import requests
from bs4 import BeautifulSoup 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from alive_progress import alive_bar
# capa = DesiredCapabilities.CHROME
# capa["pageLoadStrategy"] = "none"
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--disable-notifications')
# options.add_argument('--headless=new')
# prefs = {"profile.managed_default_content_settings.images": 2}
# options.add_experimental_option("prefs", prefs)
from selenium.webdriver.firefox.service import Service
driver=webdriver.Chrome(options=options)
wait=WebDriverWait(driver,20)
driver.get('https://www.blibli.com/brand/p-g-official-store?excludeProductList=false&promoTab=false')
time.sleep(3)
ac=ActionChains(driver)
for i in range(0,3):
    ac.scroll_by_amount(0,200).perform()
    time.sleep(3)
test=driver.find_element(By.CSS_SELECTOR,'#OLY-60021-00110 > label > div.product-outer > div > div.product__description > div')
ac.move_to_element(test).click().perform()
time.sleep(2)
# for i in range(1,5):
#     catalog=driver.find_elements(By.CLASS_NAME,f"seo-table-head-column{i}-link")
#     for i in catalog:
#         print(i.get_attribute('href'))
