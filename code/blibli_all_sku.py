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
driver.get('https://www.blibli.com/brand/p-g-official-store?excludeProductList=false&promoTab=false')
ac=ActionChains(driver)
for i in range(0,10):
    ac.scroll_by_amount(0,500)
    time.sleep(4)