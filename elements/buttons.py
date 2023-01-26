from selenium_base.base import SeleniumBase


class Buttons(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.button_page = 'li[id="item-4"]'
        self.double = 'button[id="doubleClickBtn"]'
        self.right = 'button[id="rightClickBtn"]'
        self.click_me = "//div[3]/button"
        self.success_double = 'p[id="doubleClickMessage"]'
        self.success_right = 'p[id="rightClickMessage"]'
        self.success_click = 'p[id="dynamicClickMessage"]'
        self.double_text = 'You have done a double click'
        self.right_text = 'You have done a right click'
        self.click_text = 'You have done a dynamic click'



    def find_buttons_page(self):
        return self.is_visible('css', self.button_page).click()

    def click_on_different_buttons(self, type_click):
        if type_click == "double":
            self.action_double_click(self.is_visible('css', self.double))
            return self.check_clicked_on_button(self.success_double)

        if type_click == "right":
            self.action_right_click(self.is_visible('css', self.right))
            return self.check_clicked_on_button(self.success_right)

        if type_click == "click":
            self.is_present('xpath', self.click_me).click()
            return self.check_clicked_on_button(self.success_click)

    def check_clicked_on_button(self, element):
        return self.is_present('css', element).text