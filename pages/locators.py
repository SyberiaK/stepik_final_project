from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group a.btn")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators:
    BASKET_CONTENT = (By.CSS_SELECTOR, "#content_inner .basket_summary")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")

class MainPageLocators:
    pass
    

class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form_invalid")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form_invalid")
    REGISTER_EMAIL_INPUT = (By.CSS_SELECTOR, '[name="registration-email"]')
    REGISTER_PASSWORD1_INPUT = (By.CSS_SELECTOR, '[name="registration-password1"]')
    REGISTER_PASSWORD2_INPUT = (By.CSS_SELECTOR, '[name="registration-password2"]')
    REGISTER_SUBMIT = (By.CSS_SELECTOR, '[name="registration_submit"]')
    
    
class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")
    ALERT_WITH_BOOK_NAME = (By.CSS_SELECTOR, "#messages strong")
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    BOOK_PRICE_IN_BASKET_ALERT = (By.CSS_SELECTOR, "#messages p strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert")