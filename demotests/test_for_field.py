import pytest
import time

from elements.elements_sign import Elements_sign
from navigation.homepage_nav import HomePageNav
from selenium_base.base import SeleniumBase


@pytest.mark.usefixtures('setup')
class TestForField():


        def test_for_field(self):
                driver = Elements_sign(self.driver)
                name_field = driver.find_full_name_field()
                name_field.send_keys('Elena')
                email_field = driver.find_email_field()
                email_field.send_keys('eps@gmail.com')
                current_address_field = driver.find_current_address_field()
                current_address_field.send_keys('Ukraine')
                permanent_address_field = driver.find_permanent_address_field()
                permanent_address_field.send_keys('Kharkiv')
                submit_button = driver.find_submit_button()
                submit_button.click()
                time.sleep(5)
                output_name = driver.get_output_name().split(':', maxsplit=1)[1]
                output_email = driver.get_output_email().split(':', maxsplit=1)[1]
                output_current_address = driver.get_output_current_address().split(':', maxsplit=1)[1]
                output_permanent_address = driver.get_output_permanent_address().split(':', maxsplit=1)[1]

                actual_result = list['Elena', 'eps@gmail.com', 'Ukraine', 'Kharkiv']
                expected_result = list[output_name, output_email, output_current_address, output_permanent_address]
                assert actual_result == expected_result 


