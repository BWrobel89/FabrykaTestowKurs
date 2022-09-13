# Niejawne oczekiwanie. Webdriver przeszukuje DOM przez okreslony czas podczas wyszukiwania elementu
from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://simpletestsite.fabrykatestow.pl/")
myDynamicElement = driver.find_element(by=ID, "")
driver.quit()
