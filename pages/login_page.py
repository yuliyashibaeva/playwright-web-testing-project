from .base_page import BasePage
from test_data.links import LOGIN_PAGE_LINK
from playwright.sync_api import expect


class LoginPage(BasePage):
    def error_message_should_be_present(self):
        expect(self.page.get_by_test_id("error")).to_be_visible()

    def error_message_should_have_text(self):
        expect(self.page.get_by_test_id("error")).to_have_text("Epic sadface: Sorry, this user has been locked out.")

    def login(self, username: str, password: str):
        self.page.get_by_test_id("username").fill(username)
        self.page.get_by_test_id("password").fill(password)
        self.page.get_by_test_id("login-button").click()

    def open_login_page(self):
        self.page.goto(LOGIN_PAGE_LINK)
