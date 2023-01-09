import pytest
from navigation.homepage_nav import HomePageNav
from navigation.womenpage_nav import WomenPageNav


@pytest.mark.usefixtures('setup')
class TestWomenPage:

    def test_horizont_nav_links(self):
        driver = WomenPageNav(self.driver)
        actual_links = driver.get_horizont_nav_links_text()
        print(actual_links)
        #expected_links = driver.NAV_LINK_TEXT
        #assert actual_links == expected_links, 'Validating Nav_links_text'