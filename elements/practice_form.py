import os
import random
import time
from selenium.webdriver import Keys

from generator.generator import generate_student, generated_image
from selenium_base.base import SeleniumBase



class PracticeForm(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.first_name_field = 'input[id="firstName"]'
        self.last_name_field = 'input[id="lastName"]'
        self.email_field = 'input[id="userEmail"]'
        self.gender = '//*[@id="genterWrapper"]/div[2]/div[2]/label'
        self.radio_buttons = 'div[id="genterWrapper"]'
        self.checkboxes = '//*[@id="hobbiesWrapper"]/div[2]/div[1]/label'
        self.checkboxes_radio_buttons = '.custom-control-label'
        self.mobile_field = 'input[id="userNumber"]'
        self.date_of_birth_field = 'input[id="dateOfBirthInput"]'
        self.subjects_field = 'div[id="subjectsWrapper"]'
        self.state_subject_container = 'div[class=" css-2b097c-container"]'
        #self.subjects_enter = 'div[//*[@id="subjectsContainer"]'
        #self.expected_subjects = 'div[class="css-12jo7m5 subjects-auto-complete__multi-value__label"]'
        self.select_picture_button = 'input[id="uploadPicture"]'
        self.interactions_icon = '//*[@id="app"]/div/div/div[2]/div[1]/div/div/div[5]/span/div/div[2]/div[2]'
        self.current_address_field = 'textarea[id="currentAddress"]'
        self.select_state_dropdown = 'div[id="stateCity-wrapper"]'
        self.select_state_name = 'div[id="state"]'
        self.submit_button = 'button[id="submit"]'
        self.footer = "//*[@id='app']/footer"
        self.check_text = "['Male', 'Female', 'Other', 'Sports', 'Reading', 'Music']"
        self.result_table = 'div[class="table-responsive"]'
        self.close_button = 'button[id="closeLargeModal"]'
        self.name_result = '/html/body/div[4]/div/div/div[2]/div/table/tbody/tr[1]/td[2]'

    def fill_all_fields(self):
        student_info = next(generate_student())
        first_name = student_info.first_name
        last_name = student_info.last_name
        email = student_info.email
        mobile = student_info.mobile
        current_address = student_info.current_address

        self.is_visible('css', self.first_name_field).send_keys(first_name)
        self.is_visible('css', self.last_name_field).send_keys(last_name)
        self.is_visible('css', self.email_field).send_keys(email)
        self.is_visible('css', self.mobile_field).send_keys(mobile)
        self.is_visible('css', self.current_address_field).send_keys(current_address)
        return [first_name+last_name, email, str(mobile), current_address]

    def check_buttons_text(self):
        button = self.are_visible('css', self.checkboxes_radio_buttons)
        data = []
        for item in button:
            data.append(item.text)
        return data

    def check_gender(self):
        gender = self.is_visible('xpath', self.gender)
        self.click_on_element(gender)

    def check_hobbies(self):
        hobby = self.is_visible('xpath', self.checkboxes)
        self.click_on_element(hobby)

    def click_random_checkboxes(self):
        checkbox = self.are_visible('css', self.checkboxes_radio_buttons)
        count = 8
        while count != 0:
            item = checkbox[random.randint(1, 5)]
            if count > 0:
                self.go_to_element(item)
                item.click()
                count -= 1
            else:
                break

    def upload_image_check(self):
        file_name, path = generated_image()
        self.is_present('css', self.select_picture_button).send_keys(path)
        os.remove(path)
        displayed_name = self.is_present('css', self.select_picture_button).text
        print(displayed_name)
        return file_name.split('\\')[-1], displayed_name

    def check_select_state(self):
        select = self.is_visible('css', self.select_state_dropdown)
        self.click_on_element(select)
        #self.is_present('css', self.select_state_dropdown).send_keys(Keys.RETURN)


    def find_subject(self):
        item = self.is_visible('css', self.subjects_field)
        self.click_on_element(item)

    def find_submit_button(self):
        submit = self.is_visible('css', self.submit_button)
        self.click_on_element(submit)


    def footer_delete(self):
        self.is_present('xpath', self.footer)

    def check_result_table(self):
        table = self.are_visible('css', self.result_table)
        data = []
        for row in table:
            data.append(row.text.replace('Student Name', '').replace('Student Email', '').replace('Gender', '').replace('Mobile', '').replace('Date of Birth ', '').replace('Subjects ', '').replace('Hobbies ', '').replace('Picture ', '').replace('Address ', '').replace('StateandCity ', '').replace(' ', '').split('\n')[1:])

        return data

    def find_name_result(self):
        table = self.are_visible('css', self.result_table)
        data = []
        for row in table:
            data.append(row.text.replace('Student Name', '').replace('Student Email', '').replace('Gender', '').replace(
                'Mobile', '').replace('Date of Birth ', '').replace('Subjects ', '').replace('Hobbies ', '').replace(
                'Picture ', '').replace('Address ', '').replace('StateandCity ', '').replace(' ', '').split('\n')[1])

        return data

    def find_email_result(self):
        table = self.are_visible('css', self.result_table)
        data = []
        for row in table:
            data.append(
                row.text.replace('Student Name', '').replace('Student Email', '').replace('Gender', '').replace('Mobile',
                                                                                                            '').replace(
                'Date of Birth ', '').replace('Subjects ', '').replace('Hobbies ', '').replace('Picture ', '').replace(
                'Address ', '').replace('StateandCity ', '').replace(' ', '').split('\n')[2:])

        return data

    def find_mobile_result(self):
        table = self.are_visible('css', self.result_table)
        data = []
        for row in table:
            data.append(
                row.text.replace('Student Name', '').replace('Student Email', '').replace('Gender', '').replace('Mobile',
                                                                                                            '').replace(
                'Date of Birth ', '').replace('Subjects ', '').replace('Hobbies ', '').replace('Picture ', '').replace(
                'Address ', '').replace('StateandCity ', '').replace(' ', '').split('\n')[4:])

        return data

    def find_address_result(self):
        table = self.are_visible('css', self.result_table)
        data = []
        for row in table:
            data.append(
                row.text.replace('Student Name', '').replace('Student Email', '').replace('Gender', '').replace('Mobile',
                                                                                                            '').replace(
                'Date of Birth ', '').replace('Subjects ', '').replace('Hobbies ', '').replace('Picture ', '').replace(
                'Address ', '').replace('StateandCity ', '').replace(' ', '').split('\n')[8:])

        return data

    def find_picture_result(self):
        table = self.are_visible('css', self.result_table)
        data = []
        for row in table:
            data.append(
                row.text.replace('Student Name', '').replace('Student Email', '').replace('Gender', '').replace('Mobile',
                                                                                                            '').replace(
                'Date of Birth ', '').replace('Subjects ', '').replace('Hobbies ', '').replace('Picture ', '').replace(
                'Address ', '').replace('StateandCity ', '').replace(' ', '').split('\n')[7:])

        return data







