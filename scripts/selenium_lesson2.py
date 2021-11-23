from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

from selenium.webdriver.common.by import By

my_service = Service('C:/Users/48721/Desktop/KURS PYTHON SELENIUM/chromedriver.exe')
driver = webdriver.Chrome(service=my_service)

driver.get('https://google.pl')

cookies_agr = driver.find_element(By.ID, "L2AGLb")
cookies_agr.click()

search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys('selenium python')

search_box.submit()

time.sleep(5)

driver.quit()

