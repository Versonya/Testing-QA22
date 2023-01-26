import random

from selenium.webdriver.remote.webelement import WebElement
from selenium_base.base import SeleniumBase


class CheckBoxes(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.checkboxes_page = '#item-1'
        self.expand_button: str = ".rct-option.rct-option-expand-all"
        self.collapse_button: str = ".rct-option.rct-option-collapse-all"
        self.home_toggle = 'button[aria-label="Toggle"]'
        self.home_button = 'span[class="rct-checkbox"]'
        self.checked_items = 'svg[class="rct-icon rct-icon-check"]'
        self.checkbox_list = 'span[class="rct-title"]'
        self.checkbox_list_text = ['Home', 'Desktop', 'Notes', 'Commands', 'Documents', 'WorkSpace', 'React', 'Angular', 'Veu', 'Office', 'Public', 'Private', 'Classified', 'General', 'Downloads', 'Word File.doc', 'Excel File.doc']
        self.title_item = "//ancestor::span[@class='rct-text']"
        self.output_checkboxes = 'span[class="text-success"]'




    def find_checkboxes_page(self):
        return self.is_visible('css', self.checkboxes_page, 'test checkboxes')

    def find_expand(self) -> WebElement:
        return self.is_visible('css', self.expand_button, "Plus button")

    def tree_opening(self):
        return self.is_visible('css', self.home_toggle, "Opening of checkbox tree")

    def find_collapse(self) -> WebElement:
        return self.is_visible('css', self.collapse_button, "Plus button")

    def find_checkboxes_text(self):
        item_list = self.are_visible('css', self.checkbox_list, '')
        data = []
        for item in item_list:
            data.append(item.text)
        return data

    def click_random_checkboxes(self):
        checkbox = self.are_visible('css', self.checkbox_list)
        count = 21
        while count != 0:
            item = checkbox[random.randint(1, 15)]
            if count > 0:
                self.go_to_element(item)
                item.click()
                count -= 1
            else:
                break


    def get_checked_items(self):
        checked_list = self.are_present('css', self.checked_items)
        data = []
        for box in checked_list:
            title_item = box.find_element('xpath', self.title_item)
            data.append(title_item.text.replace(' ', '').replace('.doc', '').lower())
        return data

    def output_result(self):
        output_link = self.are_visible('css', self.output_checkboxes)
        data = []
        for item in output_link:
            data.append(item.text.replace(' ', '').lower())
        return data

