from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "form#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "form#register_form")


class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_PRICE = (By.CSS_SELECTOR,".product_main p.price_color")
    PRODUCT_NAME = (By.CSS_SELECTOR,".product_main h1")
    PRODUCT_NAME_IN_ADDED_TO_BASKET_ALERT = (By.CSS_SELECTOR,"#messages > .alert:nth-child(1) > .alertinner strong")
    BASKET_PRICE_IN_ADDED_TO_BASKET_ALERT = (By.CSS_SELECTOR,"#messages > .alert:nth-child(3) > .alertinner strong")