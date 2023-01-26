import requests

from selenium_base.base import SeleniumBase


class BrowserWindow(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.find_page = 'li[id="#item-0"]'
        self.href = 'https://demoqa.com/sample'
        self.new_button = 'button[id="tabButton"]'
        self.new_window_message = 'button[id="messageWindowButton"]'
        self.new_info = '/html/body/text()'

    def find_item(self):
        return self.is_visible('css', self.find_page).click()

    def check_new_tab(self):
        new_tab = self.is_visible('css', self.new_button)
        link_href = self.href
        request = requests.get(link_href)
        if request.status_code == 200:
            new_tab.click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            url = self.driver.current_url
            return link_href, url
        else:
            return request.status_code

    def check_new_window(self):
        new_window = self.is_visible('css', self.new_window_message)
        new_window.click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        info = self.is_visible('xpath', self.new_info)
        return info.text



