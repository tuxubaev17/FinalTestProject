from .base_page import BasePage
from .locators import ProductPageLocators
import time

class ProductPage(BasePage):
    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        button.click()



    def should_be_check_basket(self):
        product = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_in_basket = self.browser.find_element(*ProductPageLocators.NAME_IN_BASKET).text
        assert product == product_in_basket, "Товар не в корзине "
        print("Товар добавлен в корзину")

        price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        price_in_basket = self.browser.find_element(*ProductPageLocators.PRICE_IN_BASKET).text
        assert price == price_in_basket, "Цена товара не совпадает с ценой в корзине"
        print("Цена товара совпадает с ценой в корзине")

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Сообщение об успехе представлено, но не должно быть"

    def should_disappeared_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Сообщение об успехе представлено, но не должно быть"



