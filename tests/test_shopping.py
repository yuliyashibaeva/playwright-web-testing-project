from test_data.user_credentials import STANDARD_USER_USERNAME, PASSWORD, ERROR_USER_USERNAME
import pytest
import allure


@pytest.mark.happy_pass
# implemented failed test to try xfail
@pytest.mark.parametrize("user_name", [STANDARD_USER_USERNAME, ERROR_USER_USERNAME])
@pytest.mark.xfail(condition=lambda: pytest.param.user_name == "ERROR_USER_USERNAME",
                   reason="known bug with the error user")
class TestMakeAnOrder:
    @allure.title("E2E scenario: {user_name} makes an order")
    def test_make_an_order_happy_pass(self, login_page, product_list_page, cart_page, checkout_page, customer_data,
                                      user_name):
        login_page.open_page_and_login(user_name, PASSWORD)
        product_list_page.add_bolt_t_shirt_to_cart()
        product_list_page.go_to_cart()
        cart_page.go_to_checkout()
        checkout_page.fill_in_customer_info(customer_data.first_name, customer_data.last_name, customer_data.postal_code)
        checkout_page.click_continue_button()
        checkout_page.click_finish_button()
        checkout_page.checkout_completion_text_should_be_present()


@pytest.mark.add_tests
class TestAddProductToCart:
    @allure.title("User can add a product to the cart")
    def test_product_should_be_added_to_cart(self, login_page, product_list_page):
        login_page.open_page_and_login(STANDARD_USER_USERNAME, PASSWORD)
        product_list_page.add_backpack_to_cart()
        product_list_page.shopping_cart_badge_should_be_equal_to(1)


@pytest.mark.delete_tests
class TestDeleteProductFromCart:
    @allure.title("User can remove a product from the cart when they are on the product list page")
    def test_product_should_be_removed_from_product_list_page(self, login_page, product_list_page):
        login_page.open_page_and_login(STANDARD_USER_USERNAME, PASSWORD)
        product_list_page.add_backpack_to_cart()
        product_list_page.remove_backpack_from_cart()
        product_list_page.shopping_cart_badge_should_not_be_present()

    @allure.title("User can remove a product from the cart when they are on the cart page")
    def test_product_should_be_removed_from_cart_page(self, login_page, product_list_page, cart_page):
        login_page.open_page_and_login(STANDARD_USER_USERNAME, PASSWORD)
        product_list_page.add_backpack_to_cart()
        product_list_page.go_to_cart()
        cart_page.remove_backpack_from_cart()
        cart_page.shopping_cart_badge_should_not_be_present()
