import pytest
from playwright.sync_api import Playwright, Page
from pages.login_page import LoginPage
from pages.product_list_page import ProductListPage


@pytest.fixture(scope='function')
def login_page(page: Page, playwright: Playwright) -> LoginPage:
    return LoginPage(page, playwright)


@pytest.fixture(scope='function')
def product_list_page(page: Page, playwright: Playwright) -> ProductListPage:
    return ProductListPage(page, playwright)

