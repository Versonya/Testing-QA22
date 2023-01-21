from selenium.webdriver.remote.webelement import WebElement
from selenium_base.base import SeleniumBase


class Links(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.find_page = 'li[id="item-5"]'
        self.home_link = '#simpleLink'
        self.Homea_link = '#dynamicLink'
        self.created_link = '#created'
        self.no_content_link = '#no-content'
        self.moved_link = '#moved'
        self.bad_request_link = '#bad-request'
        self.unauthorized_link = '#unauthorized'
        self.forbidden_link = '#forbidden'
        self.not_found_link = '#invalid-url'
        self.link_answer = 'p[id="linkResponse"]'
        self.created_text = 'Link has responded with staus 201 and status text Created'

    def find_link(self) -> WebElement:
        return self.is_visible('css', self.find_page)

    def created_check(self):
        self.is_visible('css', self.created_link).click()
        data = self.is_visible('css', self.link_answer).text
        return data
