from .base_page import BasePage
from test_data.links import LOGIN_PAGE_LINK
from playwright.sync_api import expect
import allure


class LoginPage(BasePage):
    ERROR_MSG_TEXT = "Epic sadface: Sorry, this user has been locked out."

    def error_message_should_have_text(self):
        with allure.step(f"Check that the validation message has the text: \"{LoginPage.ERROR_MSG_TEXT}\""):
            expect(self.page.get_by_test_id("error")).to_have_text(LoginPage.ERROR_MSG_TEXT)

    def open_page_and_login(self, username: str, password: str):
        with allure.step(f"Open login page and login with the {username} credentials"):
            self.page.goto(LOGIN_PAGE_LINK)
            self.page.get_by_test_id("username").fill(username)
            self.page.get_by_test_id("password").fill(password)
            self.page.get_by_test_id("login-button").click()
