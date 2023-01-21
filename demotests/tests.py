import pytest

from elements.checkbox import CheckBoxes
from elements.radiobutton import RadioButtons
from elements.webtables import WebTables



@pytest.mark.usefixtures('setup')
class TestForCheckbox:

        def test_home_checkbox(self):
                CheckBoxDriver = CheckBoxes(self.driver)
                CheckBoxDriver.find_checkboxes_page().click()
                CheckBoxDriver.find_expand().click()
                CheckBoxDriver.click_random_checkboxes()
                checkbox_clicked = CheckBoxDriver.get_checked_items()
                checkbox_list = CheckBoxDriver.find_checkboxes_text()
                print(checkbox_clicked)
                print(checkbox_list)
                #checked_items = ','.join(checkbox_clicked)
                #actual_checkboxes = ','.join(checkbox_list)
                #assert checkbox_clicked in actual_checkboxes
                #assert checked_items in actual_checkboxes

                #actual_result_text = CheckBoxDriver.find_checkboxes_text()
                #expected_result_text = CheckBoxDriver.checkbox_list_text
                #assert actual_result_text == expected_result_text
                #actual_result = CheckBoxDriver.find_checkboxes_text()
                #expected_result = CheckBoxDriver.checkbox_list_text
                #assert actual_result == expected_result
#
        def test_radio_buttons(self):
                radiobutton = RadioButtons(self.driver)
                radiobutton.find_page().click()
                radiobutton.find_yes_button().click()
                output_yes = radiobutton.find_output_text()
                radiobutton.find_impressive_button().click()
                output_impressive = radiobutton.find_output_text()
                #radiobutton.find_no_button().click()
                #output_no = radiobutton.find_output_text()

                assert output_yes == 'Yes'
                #assert output_no == 'No'
                assert output_impressive == 'Impressive'

        def test_Webtables(self):
                webtables = WebTables(self.driver)
                webtables.find_webtables_page().click()
                webtables.find_add().click()
                new_person = webtables.fill_all_fields()
                table_result = webtables.get_table_row()
                print(table_result)
                print(new_person)
                assert new_person in table_result

