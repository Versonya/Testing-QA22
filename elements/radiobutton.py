import random

from selenium.webdriver.remote.webelement import WebElement
from selenium_base.base import SeleniumBase


class RadioButtons(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.find_item = '#item-2'
        self.yes_input = 'label[for="yesRadio"]'
        self.impressive_input = 'label[for="impressiveRadio"]'
        self.no_input = 'label[for="noRadio"]'
        self.output_text = 'span[class="text-success"]'

    def find_page(self):
        return self.is_visible('css', self.find_item, '')

    def find_yes_button(self):
        return self.is_visible('css', self.yes_input, 'Yes click')

    def find_output_text(self):
        return self.is_visible('css', self.output_text, 'radiobutton name').text

    def find_impressive_button(self):
        return self.is_visible('css', self.impressive_input)

    def find_no_button(self):
        return self.is_visible('css', self.no_input, '')