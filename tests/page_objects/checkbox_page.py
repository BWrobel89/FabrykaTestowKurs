from tests.helpers.support_functions import *
from time import sleep

checkbox_tab = 'checkbox-header'
all_checkboxes = 'checkboxes'
checkbox_1 = '//*[@id="checkboxes"]/input[1]'
checkbox_2 = '//*[@id="checkboxes"]/input[2]'


def checkbox_visible(driver_instance):
    elem = wait_for_visibility_of_element_id(driver_instance, all_checkboxes)
    return elem.is_displayed()


def click_checkboxes_tab(driver_instance):
    wait_for_visibility_of_element(driver_instance, checkbox_tab)
    elem = driver_instance.find_element(By.ID, checkbox_tab)
    elem.click()


def click_checkboxes(driver_instance):
    elem = driver_instance.find_element(By.XPATH, checkbox_1)
    elem.click()
    elem1 = driver_instance.find_element(By.XPATH, checkbox_2)
    elem1.click()
    sleep(3)
