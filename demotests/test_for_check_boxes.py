import pytest
import time

from checkbox.checkbox import CheckBoxes


@pytest.mark.usefixtures('setup')
class TestForCheckbox:

        def test_home_checkbox(self):
                driver = CheckBoxes(self.driver)
                plus_button = driver.plus_check()
                plus_button.click()
                time.sleep(2)
                minus_button = driver.minus_check()
                minus_button.click()
                time.sleep(2)
                for i in range(2):
                       tree_button = driver.tree_opening()
                       tree_button.click()
                       time.sleep(2)
                home_check = driver.home_button_check()
                home_check.click()
                home_check.click()
