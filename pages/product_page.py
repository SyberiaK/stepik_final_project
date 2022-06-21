from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Add to basket button is not presented"
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()
        
    def should_book_names_be_equal(self):
        assert self.is_element_present(*ProductPageLocators.BOOK_NAME), "Book name is not presented"
        assert self.is_element_present(*ProductPageLocators.ALERT_WITH_BOOK_NAME), "Alert with book name is not presented"
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
        alert_with_book_name = self.browser.find_element(*ProductPageLocators.ALERT_WITH_BOOK_NAME)
        assert book_name.text == alert_with_book_name.text, "Book names not equal"
        
    def should_book_prices_be_equal(self):
        assert self.is_element_present(*ProductPageLocators.BOOK_PRICE), "Book price is not presented"
        assert self.is_element_present(*ProductPageLocators.BOOK_PRICE_IN_BASKET_ALERT), "Book price in basket alert is not presented"
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE)
        book_price_in_basket_alert = self.browser.find_element(*ProductPageLocators.BOOK_PRICE_IN_BASKET_ALERT)
        assert book_price.text == book_price_in_basket_alert.text, "Book prices not equal"
        
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"    
        
    def should_be_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is not disappeared, but should be"    