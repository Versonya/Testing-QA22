from selenium.webdriver.remote.webelement import WebElement
from selenium_base.base import SeleniumBase


class CheckBoxes(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.plus_click: str = ".rct-option.rct-option-expand-all"
        self.minus_click: str = ".rct-option.rct-option-collapse-all"
        self.home_toggle = 'button[aria-label="Toggle"]'
        self.home_button = 'span[class="rct-checkbox"]'
        #self.desktop_button =


    def plus_check(self) -> WebElement:
        return self.is_visible('css', self.plus_click, "Plus button")

    def tree_opening(self):
        return self.is_visible('css', self.home_toggle, "Opening of checkbox tree")

    def minus_check(self) -> WebElement:
        return self.is_visible('css', self.minus_click, "Plus button")

    def home_button_check(self):
        return self.is_visible('css', self.home_button, 'Home check')