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
from selenium.webdriver.common.action_chains import ActionChains
# capa = DesiredCapabilities.CHROME
# capa["pageLoadStrategy"] = "none"
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--disable-notifications')

from selenium.webdriver.chrome.service import Service
driver=webdriver.Chrome(service=Service(r'D:\Python Scripts\project_scraping_blibli-Master\chromedriver.exe'),options=options)
wait=WebDriverWait(driver,20)
list_stock=[]
driver.get('https://lookerstudio.google.com/u/0/reporting/fdb8f630-0743-4c08-835e-c25fc828518f/page/p_ur0mswz5qc')
time.sleep(10)
# wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/app-bootstrap/ng2-bootstrap/lego-router-outlet/reporting-view-manager/ng2-reporting-view/div/div[2]/div/ng2-reporting-plate/plate/div/div/div/div[1]/div[1]/div[2]/div/div/div/canvas-pancake-adapter/canvas-layout/div/div[1]/div/div/div/ng2-report/ng2-canvas-container/div/div[7]/ng2-canvas-component/div/div/div/div/ga-date-range-picker-wrapper/ng2-date-range-picker/lego-date-duration-control/control-layout-wrapper/button/div[1]/span[2]')))
drop_down=driver.find_element(By.CSS_SELECTOR,'.datepicker > button:nth-child(1) > div:nth-child(1) > span:nth-child(1)')
drop_down.click()
bulan_awal=wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[4]/div[1]/div[2]/div[2]/table/thead/tr[1]/th[2]/button")))
bulan_awal.click()
pilih_awal=wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[4]/div[1]/div[2]/div[2]/table/tbody/tr[1]/td[1]/button/span")))
pilih_awal.click()
tanggal_1=wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[4]/div[1]/div[2]/div[2]/table/tbody/tr[1]/td[1]/button")))
tanggal_1.click()
# bulan /html/body/div[4]/div[1]/div[2]/div[2]/table/thead/tr[1]/th[2]/button
# january /html/body/div[4]/div[1]/div[2]/div[2]/table/tbody/tr[1]/td[1]/button/span
# /html/body/div[4]/div[1]/div[2]/div[2]/table/tbody/tr[2]/td[1]/button/span
# /html/body/div[4]/div[1]/div[2]/div[2]/table/tbody/tr[2]/td[2]/button/span
# /html/body/div[4]/div[1]/div[3]/div[2]/table/tbody/tr[2]/td[1]/button
# /html/body/div[4]/div[1]/div[2]/div[2]/table/tbody/tr[2]/td[3]/button/span
# /html/body/div[4]/div[1]/div[2]/div[2]/table/tbody/tr[4]/td[1]/button
bulan_akhir=wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[4]/div[1]/div[3]/div[2]/table/thead/tr[1]/th[2]/button")))
bulan_akhir.click()
pilih_akhir=wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[4]/div[1]/div[3]/div[2]/table/tbody/tr[1]/td[1]/button/span")))
pilih_akhir.click()
tanggal_2=wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[4]/div[1]/div[3]/div[2]/table/tbody/tr[1]/td[1]/button/span")))
tanggal_2.click()
terapkan=wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[4]/div[2]/button[1]')))
terapkan.click()
time.sleep(6)
burger_menu=wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/app-bootstrap/ng2-bootstrap/lego-router-outlet/reporting-view-manager/ng2-reporting-view/div/div[2]/div/ng2-reporting-plate/plate/div/div/div/div[1]/div[1]/div[2]/div/div/div/canvas-pancake-adapter/canvas-layout/div/div/div/div/div/ng2-report/ng2-canvas-container/div/div[12]/ng2-component-header/div[2]/div/div[2]/ng2-chart-menu-button/button")))
burger_menu.click()
ekspor=wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[3]/div[2]/div/div/div/span[3]/button")))
ekspor.click()

button_csv=wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[3]/div[2]/div/mat-dialog-container/div/div/data-export-dialog/div/mat-dialog-actions/button[2]/span[2]")))
button_csv.click()
time.sleep(100)

# //*[@id="datepicker-85-4748-11"]/button

# bulan1=driver.find_element(By.XPATH,'/html/body/div[5]/div[1]/div[2]/div[2]/table/tbody/tr[2]/td[6]/button')
# # bulan2=driver.find_element(By.XPATH,'/html/body/div[6]/div[1]/div[3]/div[2]/table/thead/tr[1]/th[2]/button')
# time.sleep(4)
# ActionChains(driver).move_to_element(bulan1).click()
# time.sleep(10)

#datepicker-3780-1159-8 > button:nth-child(1)
#datepicker-3780-1159-10 > button:nth-child(1)
#datepicker-3779-8818-0
#datepicker-3779-8818-8 > button:nth-child(1) > span:nth-child(1)
#datepicker-3780-1159-11
#datepicker-3780-1159-title > strong:nth-child(1)