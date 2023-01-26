import requests

from selenium_base.base import SeleniumBase


class Broken_Links(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.find_page = '#item-6'
        self.broken_link = '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/a[2]'
        self.valid_image = '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/img[1]'
        self.broken_image = '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/img[2]'

    def find_item(self):
        page = self.is_visible('css', self.find_page, 'broken link page')
        self.go_to_element(page)
        page.click()


    def broken_link_check(self):
        link = self.is_visible('xpath', self.broken_link)
        self.go_to_element(link)
        link_href = link.get_attribute('href')
        request = requests.get(link_href)
        if request.status_code == 500:
            link.click()
            self.driver.switch_to.window(self.driver.window_handles[0])
            url = self.driver.current_url
            return link_href, url
        else:
            return request.status_code

    def valid_image_check(self):
        link = self.is_present('xpath', self.valid_image)
        check = link.is_displayed()
        return check

    def broken_image_check(self):
        link = self.is_present('xpath', self.broken_image)
        check = link.is_displayed()
        return check

