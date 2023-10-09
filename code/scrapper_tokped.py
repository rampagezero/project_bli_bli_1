import pandas as pd
df_osa=pd.read_excel(r"D:\Daily\OSA\Daily_OSA_ID_10.October'23.xlsx",sheet_name="OSA",header=2)
list_tokped=df_osa[(df_osa['eCustomer']=="Tokopedia") & ((df_osa['Status']=="Active") | (df_osa['Status']=="Active (New Listing)"))]['SKU URL']
from bs4 import BeautifulSoup 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import datetime
from alive_progress import alive_bar
# capa = DesiredCapabilities.CHROME
# capa["pageLoadStrategy"] = "none"
from selenium.webdriver.chrome.options import Options
options = Options()
# options.add_argument('--headless=new')
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--disable-notifications')
# prefs = {"profile.managed_default_content_settings.images": 2}
# options.add_experimental_option("prefs", prefs)
# prefs = {"profile.managed_default_content_settings.images": 2}
# options.add_experimental_option("prefs", prefs)
from selenium.webdriver.chrome.service import Service
driver=webdriver.Chrome(service=Service(r'D:\Python Scripts\project_scraping_blibli-Master\chromedriver.exe'),options=options)
# driver.set_page_load_timeout(10)
wait=WebDriverWait(driver,10)
list_stock=[]

with alive_bar(len(list_tokped),title='gathering data....') as bar:
    for i in list_tokped:  
        driver.get(i)
        try:
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'.css-1yy88m3-unf-heading > b:nth-child(1)')))
        except:
            pass
        soup=BeautifulSoup(driver.page_source,'html.parser') 
        try:
            beli=soup.find('b').text
            list_stock.append(beli)
        except:
            list_stock.append(0)
        # print(list_stock)
        if len(list_stock)%100==0:
            print(list_stock)
        bar()
list_tokped=list_tokped.to_list()
with alive_bar(len(list_stock),title='validating data....') as bar:
    for i,j in enumerate(list_stock):
        if j=='Habis':
            print(list_tokped[i])
            driver.get(list_tokped[i])
            time.sleep(1)
            # soup=BeautifulSoup(driver.page_source,'html.parser')
            try:    
                beli=driver.find_element(By.XPATH,'//*[@id="pdpFloatingActions"]/div[1]/p/b').text
                list_stock[i]=beli
            except:
                pass
        bar()  
driver.quit()    
import pandas as pd
import datetime
y=datetime.date.today()
df=pd.DataFrame(data=[list_tokped,list_stock]).T
df.to_excel(f'tokped_{y}.xlsx')
