from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_basket_empty(self):
        self.should_not_products_in_basket()
        self.should_be_message_basket_is_empty()

    def should_not_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Basket have products"

    def should_be_message_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_MESSAGE), "Havnt message about empty basket"
