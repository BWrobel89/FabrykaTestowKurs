from tests.helpers.support_functions import *
from selenium.webdriver.support.select import Select
from time import sleep

dropdown_header = 'dropdownlist-header'
dropdown_content = 'dropdownlist-content'
dropdown_list = 'dropdown'


def click_dropdown_tab(driver_instance):
    elem = driver_instance.find_element(By.ID, dropdown_header)
    elem.click()


def dropdown_content_visible(driver_instance):
    elem = wait_for_visibility_of_element_id(driver_instance, dropdown_content)
    return elem.is_displayed()


def get_first_dropdown_value(driver_instance):
    elem_list = Select(driver_instance.find_element(By.ID, dropdown_list))
    wait_for_visibility_of_element_id(driver_instance, dropdown_list, time_to_wait=1)
    elem_list.select_by_index(1)
    sleep(3)
