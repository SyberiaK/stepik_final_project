import pytest
import time
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage

product_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"


class TestGuestProductPage:
    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        page = ProductPage(browser, product_link)
        page.open()
        page.should_be_login_link()

    @pytest.mark.need_review
    def test_guest_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, product_link)
        page.open()
        page.add_product_to_basket()
        page.should_book_names_be_equal()
        page.should_book_prices_be_equal()

    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        page = ProductPage(browser, product_link)
        page.open()
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_not_be_any_product_in_basket()
        basket_page.should_be_empty_basket_message()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        login_link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        self.page = LoginPage(browser, login_link)
        self.page.open()
        email = f"{time.time()}@fakemailesso.org"
        password = str(time.time())
        self.page.register_new_user(email, password)
        self.page = ProductPage(browser, product_link)
        self.page.open()
        self.page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        self.page.add_product_to_basket()
        self.page.should_book_names_be_equal()
        self.page.should_book_prices_be_equal()

    def test_user_cant_see_success_message(self, browser):
        self.page.should_not_be_success_message()
