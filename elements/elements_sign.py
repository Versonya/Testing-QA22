from typing import List
from selenium.webdriver.remote.webelement import WebElement
from selenium_base.base import SeleniumBase


class Elements_sign(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.full_name: str = "#userName"
        self.email: str = "#userEmail"
        self.permanent_address: str = "#permanentAddress"
        self.current_address: str = "#currentAddress"
        self.button_submit = "#submit"
        self.output_name: str = "#name"
        self.output_email: str = "#email"
        self.output_curr_addr: str = "#currentAddress.mb-1"
        self.output_perm_addr: str = "#permanentAddress.mb-1"

    def find_full_name_field(self) -> WebElement:
        return self.is_visible('css', self.full_name, "Full name field")

    def find_email_field(self) -> WebElement:
        return self.is_visible('css', self.email, "Email field")

    def find_current_address_field(self) -> WebElement:
        return self.is_visible('css', '#currentAddress', "Current Address field")

    def find_permanent_address_field(self) -> WebElement:
        return self.is_visible('css', self.permanent_address, "Permanent Address field")

    def find_submit_button(self) -> WebElement:
        return self.is_visible('css', self.button_submit, "Submittion")

    def get_output_name(self) -> str:
        return self.is_visible('css', self.output_name, "Output name").text

    def get_output_email(self) -> str:
        return self.is_visible('css', self.output_email, "Output email").text

    def get_output_current_address(self) -> str:
        return self.is_visible('css', self.output_curr_addr, "output current adrress").text

    def get_output_permanent_address(self) -> str:
        return self.is_visible('css', self.output_perm_addr, "Output permanent address").text
