from .base_page import BasePage
from .locators import BasePageLocators, LoginPageLocators


class MainPage(BasePage):
    def __int__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"
        assert self.is_element_present(
            *LoginPageLocators.REGISTRATION_AND_LOGIN_LINK), "Registration and Login form is not presented"

