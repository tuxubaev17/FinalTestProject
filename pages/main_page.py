from .base_page import BasePage
from .locators import MainPageLocators, LoginPageLocators
from .login_page import LoginPage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.is_element_present(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        # alert = self.browser.switch_to.alert
        # alert.accept()


    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_AND_LOGIN_LINK), "Registration and Login form is not presented"

