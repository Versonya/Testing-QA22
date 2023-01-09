import pytest
from navigation.homepage_nav import HomePageNav


@pytest.mark.usefixtures('setup')
class TestHomePage:

    def test_category(self):
        homepage_nav = HomePageNav(self.driver)
        category_text = homepage_nav.find_category_text()
        print(category_text)

    def test_foxtrot_links_text(self):
        homepage_nav = HomePageNav(self.driver)
        foxtrot_links_text = homepage_nav.find_foxtrot_list_text()
        print(foxtrot_links_text)
        #actual_result = homepage_nav.find_foxtrot_list_text()
        #expected_result = homepage_nav.foxtrot_LIST_TEXT
        #assert actual_result == expected_result

    def test_nav_links(self):
        homepage_nav = HomePageNav(self.driver)
        actual_links = homepage_nav.get_nav_links_text()
        expected_links = homepage_nav.NAV_LINK_TEXT
        assert actual_links == expected_links, 'Validating Nav_links_text'

    def test_link_rail(self):
        homepage_nav = HomePageNav(self.driver)
        actual_links = homepage_nav.get_link_rail_text()
        expected_links = homepage_nav.LINK_RAIL_TEXT
        assert actual_links == expected_links, 'Validating Link_Rail_text'

    def test_logo_button(self):
        homepage_nav = HomePageNav(self.driver)
        actual_result = homepage_nav.logo_clickable()
        expected_result = homepage_nav.logo_button
        logo_button = homepage_nav.logo_clickable()
        logo_button.click()
        assert actual_result == expected_result

    def test_signin_button(self):
        homepage_nav = HomePageNav(self.driver)
        actual_result = homepage_nav.find_signin_button().text
        expected_result = 'Sign In'
        signin_button = homepage_nav.find_signin_button()
        signin_button.click()
        assert actual_result == expected_result

    def test_sign_up_title(self):
        homepage_nav = HomePageNav(self.driver)
        actual_result = homepage_nav.get_sign_up_title_text()
        expected_result = homepage_nav.SIGN_UP_TITLE_TEXT
        assert actual_result == expected_result

    def test_kid_category_button(self):
        homepage_nav = HomePageNav(self.driver)
        kids_category_button = homepage_nav.find_kids_button()
        kids_category_button.click()