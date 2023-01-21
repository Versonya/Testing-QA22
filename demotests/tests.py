import random
import time

import pytest

from elements.checkbox import CheckBoxes
from elements.radiobutton import RadioButtons
from elements.webtables import WebTables
from elements.buttons import Buttons
from elements.links import Links


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
        actual_result = CheckBoxDriver.output_result()
        assert actual_result == checkbox_clicked
        #

    def test_radio_buttons(self):
        radiobutton = RadioButtons(self.driver)
        radiobutton.find_page().click()
        radiobutton.find_yes_button().click()
        output_yes = radiobutton.find_output_text()
        radiobutton.find_impressive_button().click()
        output_impressive = radiobutton.find_output_text()
        radiobutton.find_no_button().click()
        output_no = radiobutton.find_output_text()
        assert output_yes == 'Yes'
        assert output_impressive == 'Impressive'
        assert output_no == 'No'

    def test_Webtables(self):
        webtables = WebTables(self.driver)
        webtables.find_webtables_page().click()
        webtables.find_add().click()
        new_person = webtables.fill_all_fields()
        table_result = webtables.get_table_row()
        print(table_result)
        print(new_person)
        webtables.find_search_field().send_keys('Cierra')
        webtables.find_edit().click()
        time.sleep(2)
        assert new_person in table_result

    def test_Webtables_search_person(self):
        webtables = WebTables(self.driver)
        webtables.find_webtables_page().click()
        webtables.find_add().click()
        key_word = webtables.fill_all_fields()[random.randint(0, 5)]
        webtables.find_search_field().send_keys(key_word)
        table_result = webtables.get_table_row()[0]
        assert key_word in table_result

    def test_webtables_count_row(self):
        webtables = WebTables(self.driver)
        webtables.find_webtables_page().click()
        count = webtables.select_go_to_rows()
        assert count == [5, 10, 15, 25, 50, 100]

    def test_click_on_different_buttons(self):
        button_page = Buttons(self.driver)
        button_page.find_buttons_page()
        double = button_page.click_on_different_buttons("double")
        right = button_page.click_on_different_buttons("right")
        click = button_page.click_on_different_buttons("click")
        assert double == button_page.double_text
        assert right == button_page.right_text
        assert click == button_page.click_text

    def test_for_links(self):
        link_page = Links(self.driver)
        link_page.find_link().click()
        create = link_page.created_check()
        print(create)
        assert create == link_page.created_text
