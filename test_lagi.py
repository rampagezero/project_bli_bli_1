<<<<<<< HEAD
import scrapy
class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        "https://quotes.toscrape.com/tag/humor/",
    ]

    def parse(self, response):
        for quote in response.css("div.quote"):
            yield {
                "author": quote.xpath("span/small/text()").get(),
                "text": quote.css("span.text::text").get(),
            }

        next_page = response.css('li.next a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
=======
import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.options import Options
import time
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from bs4 import BeautifulSoup
from datetime import datetime
from bs4 import BeautifulSoup
from lxml import etree
from alive_progress import alive_bar
options_1 =Options()
options_1.set_preference('permissions.default.stylesheet', 2)
options_1.set_preference('permissions.default.image', 2)
options_1.headless = True
driver = webdriver.Firefox()
>>>>>>> 69cdcec80fc08c9af3c1c163728d565f7be2f5e5
