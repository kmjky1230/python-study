from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class craiglist_crawler(object):
    def __init__(self, query):
        self.query = query
        self.url = "https://seoul.craigslist.org/search/sss?query=car&sort=rel&purveyor-input=all"
        self.driver = webdriver.Chrome("C:\Driver\chromedriver")
        self.delay = 5

    def laod_page(self):
        driver = self.driver
        driver.get(self.url)
        all_data = driver.find_elements_by_class_name("result-heading")
        for data in all_data:
            print(data.text) # price, title, date- text

query = "car"
crawler = craiglist_crawler(query)
crawler.laod_page()
