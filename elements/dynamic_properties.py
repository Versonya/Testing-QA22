import time

from selenium_base.base import SeleniumBase


class DynamicProperties(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.find_page = '#item-8'
        self.visible_button = 'button[id="visibleAfter"]'
        self.enable_button = 'button[id="enableAfter"]'
        self.color_button = 'button[id="colorChange"]'
        self.expected_color_before = 'rgba(255, 255, 255, 1)'
        self.expected_color_after = 'rgba(224, 73, 88, 1)'

    def find_item(self):
        page = self.is_visible('css', self.find_page)
        self.go_to_element(page)
        page.click()

    def check_enable_button(self):
        try:
            self.element_is_clickable('css', self.enable_button)
        except TimeoutError:
            return False
        return True

    def check_visible_after_button(self):
        try:
            self.is_visible('css', self.visible_button)
        except TimeoutError:
            return False
        return True

    def check_color_button(self):
        color = self.is_present('css', self.color_button)
        color_before = color.value_of_css_property('color')
        time.sleep(5)
        color_after = color.value_of_css_property('color')
        return color_before, color_after