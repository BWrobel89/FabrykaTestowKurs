from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import time

my_service = Service('C:/Users/48721/Desktop/KURS PYTHON SELENIUM/chromedriver.exe')
driver = webdriver.Chrome(service=my_service)

driver.get('https://fabrykatestow.pl')
driver.maximize_window()

driver.find_element(By.ID, "menu-item-1871").click()
element = driver.find_element(By.XPATH, "//a[@href='https://fabrykatestow.pl/taps' and @role='button']")
time.sleep(5)  # required otherwise element is not clickable

element.click()

teacher_info = driver.find_element(By.XPATH, "//div[@data-id='162580f4']")
action2 = ActionChains(driver)
action2.move_to_element(teacher_info)
action2.perform()

driver.save_screenshot("files/screenshot.png")

driver.quit()
