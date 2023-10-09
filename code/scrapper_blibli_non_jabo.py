import pandas as pd
df_osa=pd.read_excel(r"D:\Daily\OSA\Daily_OSA_ID_10.October'23.xlsx",sheet_name="OSA",header=2)
list_link=df_osa[(df_osa['eCustomer']=="Blibli Non Jabodetabek") & ((df_osa['Status']=="Active") | (df_osa['Status']=="Active (New Listing)"))]['SKU URL']

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
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--disable-notifications')
# options.add_argument('--headless=new')
# options.add_argument('no-sandbox')
# options.add_argument('--disable-dev-shm-usage')
# prefs = {"profile.managed_default_content_settings.images": 2}
# options.add_experimental_option("prefs", prefs)
from selenium.webdriver.chrome.service import Service
driver=webdriver.Chrome(service=Service(r"D:\Python Scripts\project_scraping_blibli-Master\chromedriver-win64(2)\chromedriver-win64\chromedriver.exe"),options=options)

# driver.set_page_load_timeout(10)
driver.set_window_size(400,300)
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
list_link=list_link.to_list()
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