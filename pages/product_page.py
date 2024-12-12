from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket_button.click()


    def get_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        return product_name.text

    
    def get_product_name_in_add_to_basket_alert(self):
        product_name_in_alert = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_ADDED_TO_BASKET_ALERT)
        return product_name_in_alert.text
    
    def get_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        return product_price.text
    

    def get_basket_price_in_alert(self):
        basket_price_in_alert = self.browser.find_element(*ProductPageLocators.BASKET_PRICE_IN_ADDED_TO_BASKET_ALERT)
        return basket_price_in_alert.text
