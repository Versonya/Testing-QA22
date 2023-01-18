from typing import List
from selenium.webdriver.remote.webelement import WebElement
from selenium_base.base import SeleniumBase
from generator.generator import generated_person

class Elements_sign(SeleniumBase):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.full_name: str = "#userName"
        self.email: str = "#userEmail"
        self.permanent_address: str = "#permanentAddress"
        self.current_address: str = "#currentAddress"
        self.button_submit = 'button[id="submit"]'
        self.output_name: str = 'p[id="name"]'
        self.output_email: str = 'p[id="email"]'
        self.output_curr_addr: str = 'p[id="currentAddress"]'
        self.output_perm_addr: str = 'p[id="permanentAddress"]'



    def find_full_name_field(self) -> WebElement:
        return self.is_visible('css', self.full_name, "Full name field")

    def find_email_field(self) -> WebElement:
        return self.is_visible('css', self.email, "Email field")

    def find_current_address_field(self) -> WebElement:
        return self.is_visible('css', self.current_address, "Current Address field")

    def find_permanent_address_field(self) -> WebElement:
        return self.is_visible('css', self.permanent_address, "Permanent Address field")

    def find_submit_button(self):
        return self.is_clickable('css', self.button_submit, '').click

    def fill_all_fields(self):
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address

        self.find_full_name_field().send_keys(full_name)
        self.find_email_field().send_keys(email)
        self.find_current_address_field().send_keys(current_address)
        self.find_permanent_address_field().send_keys(permanent_address)
        self.find_submit_button()
        return full_name, email, current_address, permanent_address
    def get_output_name(self) :
        return self.is_visible('css', self.output_name, "Output name")

    def get_output_email(self) :
        return self.is_visible('css', self.output_email, "Output email")

    def get_output_current_address(self) :
        return self.is_visible('css', self.output_curr_addr, "output current address")

    def get_output_permanent_address(self) :
        return self.is_visible('css', self.output_perm_addr, "Output permanent address")

    def entered_data(self):
        output_name = self.get_output_name().text.split(':')[1]
        output_email = self.get_output_email().text.split(':')[1]
        output_current_address = self.get_output_current_address().text.split(':')[1]
        output_permanent_address = self.get_output_permanent_address().text.split(':')[1]
        return (output_name, output_email, output_current_address, output_permanent_address)
