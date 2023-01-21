import random

from selenium.webdriver.remote.webelement import WebElement
from selenium_base.base import SeleniumBase
from generator.generator import generate_row


class WebTables(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.find_page = '#item-3'
        self.add_button = 'button[id="addNewRecordButton"]'
        self.search_field = 'input[id="searchBox"]'
        self.search_click = '.input-group-text'
        self.first_name_field = 'input[id="firstName"]'
        self.last_name_field = 'input[id="lastName"]'
        self.email_field = 'input[id="userEmail"]'
        self.age_field = 'input[id="age"]'
        self.salary_field = 'input[id="salary"]'
        self.department_field = 'input[id="department"]'
        self.submit_button = 'button[id="submit"]'
        self.delete_button = 'span[id="delete-record-1"]'
        self.edit_button = 'span[title="Edit"]'
        self.table_row = 'div[class="rt-tr-group"]'
        self.count_row_list = '[aria-label="rows per page"]'
        self.full_list = 'div[class="rt-tbody"]'

    def find_webtables_page(self):
        return self.is_visible('css', self.find_page, 'Open Webtables')

    def get_table_row(self):
        row_list = self.are_visible('css', self.table_row,'Table text')
        data = []
        for item in row_list:
            data.append(item.text.splitlines())
        return data

    def fill_all_fields(self):
        person_info = next(generate_row())
        first_name = person_info.first_name
        last_name = person_info.last_name
        email = person_info.email
        age = person_info.age
        salary = person_info.salary
        department = person_info.department

        self.find_first_name_field().send_keys(first_name)
        self.find_last_name_field().send_keys(last_name)
        self.find_email_field().send_keys(email)
        self.find_age_field().send_keys(age)
        self.find_salary_field().send_keys(salary)
        self.find_department_field().send_keys(department)
        self.find_submit_button().click()
        return [first_name, last_name, str(age), email, str(salary), department]

    def find_add(self):
        return self.is_visible('css', self.add_button, 'Add Button')

    def find_delete(self):
        return self.is_visible('css', self.delete_button, 'Delete button')

    def find_edit(self):
        return self.is_visible('css', self.edit_button, 'Edit button')

    def find_search_field(self):
        return self.is_visible('css', self.search_field, 'Search field')

    def find_first_name_field(self) -> WebElement:
        return self.is_visible('css', self.first_name_field, "First name field")

    def find_last_name_field(self) -> WebElement:
        return self.is_visible('css', self.last_name_field, "Last name field")

    def find_email_field(self) -> WebElement:
        return self.is_visible('css', self.email_field, "Email field")

    def find_age_field(self) -> WebElement:
        return self.is_visible('css', self.age_field, "Age field")

    def find_salary_field(self) -> WebElement:
        return self.is_visible('css', self.salary_field, "Salary field")

    def find_department_field(self) -> WebElement:
        return self.is_visible('css', self.department_field, "Department field")

    def find_submit_button(self):
        return self.is_visible('css', self.submit_button, '')

    def select_go_to_rows(self):
        count = [5, 10, 25, 50, 100]
        data = []
        for i in count:
            count_row_button = self.is_visible('css', self.count_row_list)
            self.go_to_element(count_row_button)
            count_row_button.click()
            self.is_visible('css', f'option[value="{i}"]').click()
            data.append(self.check_count_rows())
        return data

    def check_count_rows(self):
        list_rows = self.are_present('css', self.full_list)
        return len(list_rows)




