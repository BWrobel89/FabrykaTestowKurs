from tests.helpers.support_functions import *


add_remove_element_hearder = 'addremoveelements-header'
add_remove_element_content = 'addremoveelements-content'
new_element = '//*[@id="addremoveelements-content"]/div/div/button'
added_element = '//*[@id="elements"]/button'


def click_and_remover_tab(driver_instance):
    elem = driver_instance.find_element(By.ID, add_remove_element_hearder)
    elem.click()


def add_remover_content_visible(driver_instance):
    elem = wait_for_visibility_of_element_id(driver_instance, add_remove_element_content)
    return elem.is_displayed()


def add_element(driver_instance):
    elem = driver_instance.find_element(By.XPATH, new_element)
    elem.click()

def delete_element(driver_instance):
    elem = driver_instance.find_element(By.XPATH, added_element)
    elem.click()
    wait_for_visibility_of_element(driver_instance, added_element)


def element_invisible(driver_instance):
    try:
        wait_for_visibility_of_element(driver_instance, added_element)
        return  True
    except NoSuchElementException:
        return False