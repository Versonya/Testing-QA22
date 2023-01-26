import requests
from selenium.webdriver.remote.webelement import WebElement
from selenium_base.base import SeleniumBase


class Links(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.find_page = 'li[id="item-5"]'
        self.home_link = '#simpleLink'
        self.Homea_link = '#dynamicLink'
        self.main_page = 'div[id="app"]'
        self.created_link = '#created'
        self.no_content_link = '#no-content'
        self.moved_link = '#moved'
        self.bad_request_link = '#bad-request'
        self.unauthorized_link = '#unauthorized'
        self.forbidden_link = '#forbidden'
        self.not_found_link = '#invalid-url'
        self.link_answer = 'p[id="linkResponse"]'
        self.created_text = 'Link has responded with staus 201 and status text Created'

    def find_link(self):
        page = self.is_visible('css', self.find_page, 'link page')
        self.go_to_element(page)
        page.click()


    def valid_home_check(self):
        home = self.is_visible('css', self.home_link)
        link_href = home.get_attribute('href')
        request = requests.get(link_href)
        if request.status_code == 200:
            home.click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            url = self.driver.current_url
            return link_href, url
        else:
            return request.status_code
            
    def created_check(self, url):
        request = requests.get(url)
        if request.status_code == 200:
            self.is_visible('css', self.created_link).click()
        else:
            return request.status_code

    def forbidden_check(self, url):
        request = requests.get(url)
        if request.status_code == 200:
            self.is_visible('css', self.forbidden_link).click()
        else:
            return request.status_code

    def moved_check(self, url):
        request = requests.get(url)
        if request.status_code == 200:
            self.is_visible('css', self.moved_link).click()
        else:
            return request.status_code





