from selenium import webdriver
import pandas as pd
import time
from selenium.webdriver.common.action_chains import ActionChains
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
options=Options()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--disable-notifications')
# options.add_argument('--headless=new')
driver=webdriver.Chrome(options=options)

# full=driver.find_element(By.CSS_SELECTOR,'div.view-style-options-icon:nth-child(1) > svg:nth-child(1) > path:nth-child(1)')
# ac.move_to_element(full).click().perform()
# driver.refresh()
time.sleep(4)
list_nama=[]
list_id=[]
for page in range(0,21):
    if page==0:
        driver.get('https://www.blibli.com/brand/p-g-official-store?excludeProductList=false&promoTab=false&reqFlags=gridView&location=Jabodetabek')
    else:
        driver.get(f'https://www.blibli.com/brand/p-g-official-store?excludeProductList=false&promoTab=false&reqFlags=gridView&location=Jabodetabek&page={page}&start={40*page}')
    driver.maximize_window()
    time.sleep(3)
    ac=ActionChains(driver)
    bs=BeautifulSoup(driver.page_source,'html.parser')
    for i in range(0,10):
        ac.scroll_by_amount(0,500).perform()
    x=bs.find_all('img',{'class':'carousel-container__slide__content'})
    y=bs.find_all('div',{'class':'product__list product__list_grid-view'})
    for j in y:
        list_id.append(j.get('id'))
    for j in x:
        list_nama.append(j.get('alt'))
    set_list=set(list_nama)
    print(set_list)
    print(len(set_list))
    print(list_id)
    print(len(list_id))