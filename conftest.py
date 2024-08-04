import pytest
from playwright.sync_api import Playwright, Page
from pages.login_page import LoginPage


@pytest.fixture(scope='function')
def login_page(page: Page, playwright: Playwright) -> LoginPage:
    return LoginPage(page, playwright)
