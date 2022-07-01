from selenium import webdriver
from selenium.webdriver.chrome.service import Service

my_service = Service('C:/Users/48721/Desktop/KURS PYTHON SELENIUM/chromedriver.exe')
driver = webdriver.Chrome(service=my_service)

driver.get('https://fabrykatestow.pl')
driver.close()