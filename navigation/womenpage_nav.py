from typing import List
from selenium.webdriver.remote.webelement import WebElement
from selenium_base.base import SeleniumBase


class WomenPageNav(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.horizont_nav_links: str = "#row_2.grid-x.child_region"
        #self.NAV_LINK_TEXT = 'Women,Men,Kids,Home,Beauty,

    def get_horizont_nav_links(self) -> List[WebElement]:
        return self.are_visible('css', self.horizont_nav_links, 'Category Navigation links')

    def get_horizont_nav_links_text(self) -> str:
        horizont_nav_links = self.get_horizont_nav_links()
        horizont_nav_links_text = [link.text for link in horizont_nav_links]
        return ",".join(horizont_nav_links_text)