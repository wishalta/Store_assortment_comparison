from Barbora import Barbora_Scrapper
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait



#Reikia su selenium pasiimti duomenys, is barboros
#Veliau siuos duomenys issiusti i mysql



def initGathering():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    wait = WebDriverWait(driver, 10)
    return driver, wait

def executeDataGathering():
    driver, wait = initGathering()
    barbora = Barbora_Scrapper(driver, 'https://www.barbora.lt/')
    barbora.Activiation()

executeDataGathering()