from test_data.user_credentials import STANDARD_USER_USERNAME, PASSWORD


class TestMakeAnOrder:
    def test_make_an_order_happy_pass(self, login_page, product_list_page, cart_page, checkout_page, customer):
        login_page.open_login_page()
        login_page.login(STANDARD_USER_USERNAME, PASSWORD)
        product_list_page.add_bolt_t_shirt_to_cart()
        product_list_page.go_to_cart()
        cart_page.go_to_checkout()
        checkout_page.fill_customer_info(customer.first_name, customer.last_name, customer.postal_code)
        checkout_page.click_continue_button()
        checkout_page.click_finish_button()
        checkout_page.checkout_complete_text_should_be_present()
