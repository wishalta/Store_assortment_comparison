import time

from cffi.cffi_opcode import PRIM_FLOAT
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from Barbora_Find_Item import Barbora_Find_Item
from Barbota_item import Barbora_item


class Barbora_Scrapper():
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def activation(self):
        self.acceptCookies()
        hrefs = self.collect_products_url()
        self.collect_each_data(hrefs)

    def acceptCookies(self):
        self.driver.get("https://www.barbora.lt/")
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[5]/div[2]/a[1]").click()
        # def find_product(self):
        # self.driver.find_element(By.XPATH, '//*[@id="fti-desktop-category-4"]/a').click()
        # self.driver.find_element(By.XPATH, '//*[@id="fti-category-tree-child-4"]/a').click()
        # time.sleep(10)


    def collect_products_url(self):
        hrefs = []
        for i in range(1, 20):
            self.driver.get(f'{self.url}?page={i}')
            item = self.driver.find_element(By.XPATH, '//*[@id="category-page-results-placeholder"]/div/ul')
            lis = item.find_elements(By.TAG_NAME, 'li')
            print(len(lis))
            if len(lis) == 0:
                break
            for a in lis:
                href = a.find_element(By.TAG_NAME, 'a').get_attribute('href')
                hrefs.append(href)
        # self.collect_each_data(hrefs)
        # time.sleep(200)
        return hrefs



    def collect_each_data(self, hrefs):
       for link in hrefs:
           self.driver.get(link)
           item = Barbora_item(self.driver)
           item.fill()
           item.save()
           pass


