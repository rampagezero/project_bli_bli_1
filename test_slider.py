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
# options.add_argument('--headless=new')
# prefs = {"profile.managed_default_content_settings.images": 2}
# options.add_experimental_option("prefs", prefs)
from selenium.webdriver.firefox.service import Service
driver=webdriver.Edge(options=options)
# driver.set_page_load_timeout(10)
driver.get('https://jqueryui.com/slider/')
wait=WebDriverWait(driver,20)
wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="slider"]/span')))
slider=driver.find_element(By.XPATH,'//*[@id="slider"]/span')
action=ActionChains(driver)
action.drag_and_drop(slider,300,0).perform()
time.sleep(10)