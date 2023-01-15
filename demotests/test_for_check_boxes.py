import pytest
import time

from checkbox.checkbox import CheckBoxes


@pytest.mark.usefixtures('setup')
class TestForCheckbox:

        def test_home_checkbox(self):
                CheckBoxDriver = CheckBoxes(self.driver)
                CheckBoxDriver.find_checkboxes_page().click()
                CheckBoxDriver.find_expand().click()
                CheckBoxDriver.click_random_checkboxes()
                #CheckBoxDriver.get_checked_checkboxes()
                #actual_result_text = CheckBoxDriver.find_checkboxes_text()
                #expected_result_text = CheckBoxDriver.checkbox_list_text
                #assert actual_result_text == expected_result_text
                #actual_result = CheckBoxDriver.find_checkboxes_text()
                #expected_result = CheckBoxDriver.checkbox_list_text
                #assert actual_result == expected_result
#

