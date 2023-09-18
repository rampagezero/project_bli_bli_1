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
driver=uc.Chrome()
driver.get('https://www.lazada.co.id/products/downy-mystique-refill-720ml-paket-isi-3-i160034503-s181900786.html')