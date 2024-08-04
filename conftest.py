import pytest
from playwright.sync_api import Playwright, Page
from pages.login_page import LoginPage
from pages.product_list_page import ProductListPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from test_data.customer_info import Customer


@pytest.fixture(scope='function')
def login_page(page: Page, playwright: Playwright) -> LoginPage:
    return LoginPage(page, playwright)


@pytest.fixture(scope='function')
def product_list_page(page: Page, playwright: Playwright) -> ProductListPage:
    return ProductListPage(page, playwright)


@pytest.fixture(scope="function")
def cart_page(page: Page, playwright: Playwright) -> CartPage:
    return CartPage(page, playwright)


@pytest.fixture(scope="function")
def checkout_page(page: Page, playwright: Playwright) -> CheckoutPage:
    return CheckoutPage(page, playwright)


@pytest.fixture(scope="function")
def customer() -> Customer:
    customer = Customer()
    customer.generate_customer_data()
    return customer
