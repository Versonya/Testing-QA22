from typing import List
from selenium.webdriver.remote.webelement import WebElement
from selenium_base.base import SeleniumBase


class HomePageNav(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav_links: str = "#mainNavigationFobs>Li"
        self.NAV_LINK_TEXT = 'Women,Men,Kids,Home,Beauty,Shoes,Handbags,Jewelry,Furniture,Toys,Gifts,Trending,Sale'
        self.link_rail: str = "#link-rail.rail.link-rail"
        self.LINK_RAIL_TEXT = ('Give a gift with one click! Shop Gift Cards\n'
                                'Wedding Registry\n'
                                'Shop Your Store\n'
                                'Sign In')
        self.signin_button: str = '#myRewardsLabel-status'
        self.logo_button: str = '#logo'
        self.sign_up_title: str = '#sign-up-title'
        self.SIGN_UP_TITLE_TEXT = 'No account yet?'
        self.kids_button = '#flexid_5991.fob'
        self.foxtrot_list = '.main-slider__doth-list.smooth-scroll.js-main-carousel-doth'
        self.foxtrot_LIST_TEXT = ('Новий рік\n'
                                    'iPhone 14 Pro\n'
                                    'Galaxy\n'
                                    'Знижки на техніку\n'
                                    'Залишайся в мережі\n'
                                    'Перемагаємо темряву\n'
                                    'Кухня\n'
                                    'ТВ Samsung\n'
                                    'PlayStation\n'
                                    'Ноутбуки\n'
                                    'Xiaomi\n'
                                    'Asus\n'
                                    'iPhone .13\n'
                                    'ТВ Hisense\n'
                                    'Щедрик\n'
                                    'Ф-підтримка\n'
                                    'iPad 2020\n'
                                    'Тепло\n'
                                    'ТВ UD\n'
                                    'PS VR2')
        self.smartphone_link = '#js-catalog-list.catalog__wrap'

    def find_smartphone_category(self) -> List[WebElement]:
        return self.are_visible('css', self.smartphone_link, '')

    def find_category_text(self):
        category = self.find_smartphone_category()
        category_text = [link.text for link in category]
        return ",".join(category_text)

    def find_foxtrot_list(self) -> list[WebElement]:
        return self.are_visible('css', self.foxtrot_list, 'Category list')

    def find_foxtrot_list_text(self) -> str:
        foxtrot_links = self.find_foxtrot_list()
        foxtrot_links_text = [link.text for link in foxtrot_links]
        return ",".join(foxtrot_links_text)

    def find_signin_button(self):
        return self.is_visible('css', self.signin_button, 'Click sign_in button')

    def get_nav_links(self) -> List[WebElement]:
        return self.are_visible('css', self.nav_links, 'Header Navigation links')

    def get_nav_links_text(self) -> str:
        nav_links = self.get_nav_links()
        nav_links_text = [link.text for link in nav_links]
        return ",".join(nav_links_text)

    def get_link_rail(self) -> List[WebElement]:
        return self.are_visible('css', self.link_rail, 'Link rail navigation')

    def get_link_rail_text(self) -> str:
        link_rail = self.get_link_rail()
        bag_icon_text = [link.text for link in link_rail]
        return ",".join(bag_icon_text)

    def find_kids_button(self):
        return self.is_visible('css', self.kids_button, 'Kids Category Opening')

    def get_sign_up_title(self) -> WebElement:
        return self.is_visible('css', self.sign_up_title, 'Sign-up')

    def get_sign_up_title_text(self) -> str:
        return self.get_sign_up_title().text

    def logo_clickable(self) -> WebElement:
        return self.is_visible('css', self.logo_button, "Logo")




