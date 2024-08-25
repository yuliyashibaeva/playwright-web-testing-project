from test_data.user_credentials import STANDARD_USER_USERNAME, PASSWORD, LOCKED_OUT_USER_USERNAME
import pytest
import allure


class TestAuth:
    @allure.title("Standard user should be successfully logged in")
    @pytest.mark.auth_successful
    def test_standard_user_should_be_logged_in(self, login_page, product_list_page):
        login_page.open_page_and_login(STANDARD_USER_USERNAME, PASSWORD)
        product_list_page.page_should_have_product_list_link()

    @allure.title("Locked out user shouldn't be logged in")
    @pytest.mark.auth_failed
    def test_locked_out_user_should_fail_to_login(self, login_page):
        login_page.open_page_and_login(LOCKED_OUT_USER_USERNAME, PASSWORD)
        login_page.error_message_should_be_present()
        login_page.error_message_should_have_text()
