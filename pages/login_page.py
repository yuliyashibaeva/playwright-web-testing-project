from .base_page import BasePage
from test_data.links import LOGIN_PAGE_LINK


class LoginPage(BasePage):
    def login(self, username: str, password: str):
        self.page.get_by_test_id("username").fill(username)
        self.page.get_by_test_id("password").fill(password)
        self.page.get_by_test_id("login-button").click()

    def open_login_page(self):
        self.page.goto(LOGIN_PAGE_LINK)
