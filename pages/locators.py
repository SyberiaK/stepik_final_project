from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class MainPageLocators:
    pass
    

class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form_invalid")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form_invalid")
    
    
class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")
    ALERT_WITH_BOOK_NAME = (By.CSS_SELECTOR, "#messages strong")
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    BOOK_PRICE_IN_BASKET_ALERT = (By.CSS_SELECTOR, "#messages p strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert")