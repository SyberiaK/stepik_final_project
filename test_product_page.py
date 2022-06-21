import pytest
import time
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"


class TestUserAddToBasketFromProductPage:
    
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.page = LoginPage(browser, "http://selenium1py.pythonanywhere.com/ru/accounts/login/")
        self.page.open()
        email = f"{time.time()}@fakemailesso.org"
        password = str(time.time())
        self.page.register_new_user(email, password)
        self.page = ProductPage(browser, link)
        self.page.open()
        self.page.should_be_authorized_user()
        
    def test_user_can_add_product_to_basket(self, browser):
        self.page.add_product_to_basket()
        self.page.should_book_names_be_equal()
        self.page.should_book_prices_be_equal()
    
    
    def test_user_cant_see_success_message(self, browser):
        self.page.should_not_be_success_message()