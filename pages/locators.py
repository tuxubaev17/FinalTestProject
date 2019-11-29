from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    REGISTRATION_AND_LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    BUTTON_REGIST = (By.CSS_SELECTOR, "#register_form > button")


class LoginAndRegistartionForm():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.col-sm-6.product_main > h1")
    NAME_IN_BASKET = (By.CSS_SELECTOR, "#messages > .alert-success:nth-child(1) > .alertinner > strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main > p')
    PRICE_IN_BASKET = (By.CSS_SELECTOR, "#messages > .alert-info > .alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1)")


class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, '.basket-items')
    EMPTY_MESSAGE = (By.XPATH, "//*[@id='content_inner']/p[contains(text(),'basket is empty')]")
