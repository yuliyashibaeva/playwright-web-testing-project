from test_data.user_credentials import STANDARD_USER_USERNAME, PASSWORD, LOCKED_OUT_USER_USERNAME
import pytest


class TestAuth:
    @pytest.mark.auth_successful
    def test_standard_user_should_be_logged_in(self, login_page, product_list_page):
        login_page.open_login_page()
        login_page.login(STANDARD_USER_USERNAME, PASSWORD)
        product_list_page.page_should_have_product_list_link()

    @pytest.mark.auth_failed
    def test_locked_out_user_should_fail_to_login(self, login_page):
        login_page.open_login_page()
        login_page.login(LOCKED_OUT_USER_USERNAME, PASSWORD)
        login_page.error_message_should_be_present()
        login_page.error_message_should_have_text()
