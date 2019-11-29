from .base_page import BasePage
from .locators import LoginAndRegistartionForm, LoginPageLocators
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        email_select = self.browser.find_element(*LoginPageLocators.EMAIL)
        password_select = self.browser.find_element(*LoginPageLocators.PASSWORD)
        confirm_password = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD)
        email_select.send_keys(email)
        password_select.send_keys(password)
        confirm_password.send_keys(password)
        register = self.browser.find_element(*LoginPageLocators.BUTTON_REGIST)
        register.click()

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
