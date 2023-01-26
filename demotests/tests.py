import random
import time

import pytest

from elements.alerts_browser_window import BrowserWindow
from elements.broken_links import Broken_Links
from elements.checkbox import CheckBoxes
from elements.dynamic_properties import DynamicProperties
from elements.practice_form import PracticeForm
from elements.radiobutton import RadioButtons
from elements.upload import UploadsDownloads
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
        table_result = webtables.check_person()
        print(table_result)
        assert key_word in table_result

    def test_web_table_update_info(self):
        webtables = WebTables(self.driver)
        webtables.find_webtables_page().click()
        webtables.find_add().click()
        lastname = webtables.fill_all_fields()[1]
        webtables.find_search_field().send_keys(lastname)
        age = webtables.update_person_info()
        row = webtables.check_person()
        assert age in row

    def test_web_table_delete_info(self):
        webtables = WebTables(self.driver)
        webtables.find_webtables_page().click()
        webtables.find_add().click()
        email = webtables.fill_all_fields()[3]
        webtables.find_search_field().send_keys(email)
        webtables.delete_person()
        text = webtables.check_deleted()
        assert text == webtables.no_rows_found_text

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

    def test_check_link(self):
        link_page = Links(self.driver)
        link_page.find_link()
        href_link, current_url = link_page.valid_home_check()
        assert href_link == current_url

    def test_broken_link(self):
        broken_page = Broken_Links(self.driver)
        broken_page.find_item()
        href_link, current_url = broken_page.broken_link_check()
        assert href_link == current_url

    def test_for_valid_broken_image(self):
        broken_page = Broken_Links(self.driver)
        broken_page.find_item()
        check_valid = broken_page.valid_image_check()
        check_broken = broken_page.broken_image_check()
        print(check_broken, check_valid)
        assert check_valid is True
        assert check_broken is False

    def test_for_created_link(self):
        link_page = Links(self.driver)
        link_page.find_link()
        response_code = link_page.created_check('https://demoqa.com/created')
        assert response_code == 201

    def test_for_forbidden_link(self):
        link_page = Links(self.driver)
        link_page.find_link()
        response_code = link_page.created_check('https://demoqa.com/forbidden')
        assert response_code == 403

    def test_for_moved_link(self):
        link_page = Links(self.driver)
        link_page.find_link()
        response_code = link_page.created_check('https://demoqa.com/moved')
        assert response_code == 301

    def test_upload_file(self):
        upload_page = UploadsDownloads(self.driver)
        upload_page.find_item()
        file_name, text = upload_page.upload_check()
        print(file_name)
        print(text)
        assert file_name == text

    def test_download(self):
        upload_page = UploadsDownloads(self.driver)
        upload_page.find_item()
        check = upload_page.download_files()
        assert check is True

    def test_visible_after(self):
        dynamic_page = DynamicProperties(self.driver)
        dynamic_page.find_item()
        result = dynamic_page.check_visible_after_button()
        assert result is True

    def test_enable_button(self):
        dynamic_page = DynamicProperties(self.driver)
        dynamic_page.find_item()
        result = dynamic_page.check_enable_button()
        assert result is True

    def test_for_color_button(self):
        dynamic_page = DynamicProperties(self.driver)
        dynamic_page.find_item()
        color_before, color_after = dynamic_page.check_color_button()
        print(color_before, color_after)
        assert color_before != color_after

    def test_browser_window(self):
        alert_page = BrowserWindow(self.driver)
        link_href, current_url = alert_page.check_new_tab()
        assert link_href == current_url

    def test_new_window(self):
        alert_page = BrowserWindow(self.driver)
        actual_result = alert_page.check_new_window()
        print(actual_result)

    def test_practice_form(self):
        form_page = PracticeForm(self.driver)
        name, email, mobile, current_address = form_page.fill_all_fields()
        print(name, email, mobile, current_address)
        time.sleep(2)
        form_page.check_gender()
        form_page.check_hobbies()
        result = form_page.check_buttons_text()
        print(result)
        file_name, text = form_page.upload_image_check()
        print(file_name)
        form_page.find_subject()
        form_page.check_select_state()
        form_page.find_submit_button()
        time.sleep(5)
        table_result = form_page.check_result_table()
        mobile_result = form_page.find_mobile_result()
        picture_result = form_page.find_picture_result()
        address_result = form_page.find_address_result()
        print(table_result)
        assert name, email in table_result
        assert mobile in mobile_result
        assert current_address in address_result







