from test_data.user_credentials import STANDARD_USER_USERNAME, PASSWORD
import pytest


@pytest.mark.happy_pass
class TestMakeAnOrder:
    def test_make_an_order_happy_pass(self, login_page, product_list_page, cart_page, checkout_page, customer_data):
        login_page.open_login_page()
        login_page.login(STANDARD_USER_USERNAME, PASSWORD)
        product_list_page.add_bolt_t_shirt_to_cart()
        product_list_page.go_to_cart()
        cart_page.go_to_checkout()
        checkout_page.fill_customer_info(customer_data.first_name, customer_data.last_name, customer_data.postal_code)
        checkout_page.click_continue_button()
        checkout_page.click_finish_button()
        checkout_page.checkout_complete_text_should_be_present()


@pytest.mark.add_tests
class TestAddProductToCart:
    def test_product_should_be_added_to_cart(self, login_page, product_list_page):
        # TODO: too many times open and login
        login_page.open_login_page()
        login_page.login(STANDARD_USER_USERNAME, PASSWORD)
        product_list_page.add_backpack_to_cart()
        product_list_page.shopping_cart_badge_should_be_equal_to(1)


@pytest.mark.delete_tests
class TestDeleteProductFromCart:
    def test_backpack_should_be_deleted_from_product_list_page(self, login_page, product_list_page):
        login_page.open_login_page()
        login_page.login(STANDARD_USER_USERNAME, PASSWORD)
        product_list_page.add_backpack_to_cart()
        product_list_page.delete_backpack_from_list_page()
        product_list_page.shopping_cart_badge_should_not_be_present()

    def test_backpack_should_be_deleted_from_cart_page(self, login_page, product_list_page, cart_page):
        login_page.open_login_page()
        login_page.login(STANDARD_USER_USERNAME, PASSWORD)
        product_list_page.add_backpack_to_cart()
        product_list_page.go_to_cart()
        cart_page.remove_backpack_from_cart()
        cart_page.shopping_cart_badge_should_not_be_present()
