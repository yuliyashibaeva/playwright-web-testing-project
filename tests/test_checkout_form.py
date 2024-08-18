from test_data.user_credentials import STANDARD_USER_USERNAME, PASSWORD
import pytest


@pytest.mark.checkout_inputs_validation
@pytest.mark.parametrize("missing_input", ["First Name", "Last Name", "Postal Code"])
class TestCheckoutForm:
    def test_checkout_should_fail_without_required_field(self, login_page, product_list_page, cart_page, checkout_page,
                                                         customer_data, missing_input):
        login_page.open_page_and_login(STANDARD_USER_USERNAME, PASSWORD)
        product_list_page.add_bolt_t_shirt_to_cart()
        product_list_page.go_to_cart()
        cart_page.go_to_checkout()
        checkout_page.fill_customer_info(customer_data.first_name, customer_data.last_name, customer_data.postal_code,
                                         missing_input)
        checkout_page.click_continue_button()
        checkout_page.error_message_should_be_present()
        checkout_page.error_message_text_should_be_consistent(missing_input)
