import unittest
from selenium import webdriver
from config.test_settings import TestSettings
from tests.page_objects import main_page, checkbox_page, hovers_page, users_page, input_page, dropdown_page, add_remove_element

class Tests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = TestSettings.page_url
        self.driver.get(self.url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test1_main_page_content_visible(self):
        self.assertTrue(main_page.content_visible(self.driver))

    def test2_checkboxes(self):
        checkbox_page.click_checkboxes_tab(self.driver)
        self.assertTrue(checkbox_page.checkbox_visible(self.driver))
        checkbox_page.click_checkboxes(self.driver)

    def test3_hovers(self):
        hovers_page.click_hovers_tab(self.driver)
        self.assertTrue(hovers_page.hover_content_displayed(self.driver))
        hovers_page.hover_over_element_and_click(self.driver)
        self.assertTrue(users_page.error_info_displayed(self.driver))

    def test4_inputs_visibility(self):
        input_page.click_input_tab(self.driver)
        self.assertTrue(input_page.input_content_visible(self.driver))

    def test5_inputs_correct_input(self):
        input_page.click_input_tab(self.driver)
        self.assertTrue(input_page.send_correct_keys_to_input(self.driver))

    def test6_inputs_incorrect_input(self):
        input_page.click_input_tab(self.driver)
        self.assertTrue(input_page.send_incorrect_keys_to_input(self.driver))

    def test7_dropdown_select(self):
        dropdown_page.click_dropdown_tab(self.driver)
        self.assertTrue(dropdown_page.dropdown_content_visible(self.driver))
        dropdown_page.get_first_dropdown_value(self.driver)

    def test8_add_delement(self):
        add_remove_element.click_and_remover_tab(self.driver)
        self.assertTrue(add_remove_element.add_remover_content_visible(self.driver))
        add_remove_element.add_element(self.driver)

    def test9_remove_element(self):
        # Tests.test8_add_delement(self) - mozna to uzyc ale my robimy tak aby byly niezalezne
        add_remove_element.click_and_remover_tab(self.driver)
        self.assertTrue(add_remove_element.add_remover_content_visible(self.driver))
        add_remove_element.add_element(self.driver)
        add_remove_element.delete_element(self.driver)
        self.assertTrue(add_remove_element.element_invisible(self.driver))


if __name__ == '__main__':
    unittest.main()