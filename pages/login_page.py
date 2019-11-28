from .base_page import BasePage
from .locators import LoginAndRegistartionForm
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "login not in current url"

    def should_be_login_form(self):
        login_form = self.is_element_present(*LoginAndRegistartionForm.LOGIN_FORM)
        assert login_form, "login form not in current url"

    def should_be_register_form(self):
        registr_form = self.is_element_present(*LoginAndRegistartionForm.REGISTRATION_FORM)
        assert registr_form, "Registration form not in current url"
