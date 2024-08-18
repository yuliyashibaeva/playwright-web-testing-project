from .base_page import BasePage
from playwright.sync_api import expect


class CheckoutPage(BasePage):
    def fill_customer_info(self, first_name, last_name, postal_code, missing_input: str = None):
        self.page.get_by_test_id("firstName").fill(first_name)
        self.page.get_by_test_id("lastName").fill(last_name)
        self.page.get_by_test_id("postalCode").fill(postal_code)

        if missing_input is None:
            pass
        elif missing_input == "First Name":
            self.page.get_by_test_id("firstName").clear()
        elif missing_input == "Last Name":
            self.page.get_by_test_id("lastName").clear()
        elif missing_input == "Postal Code":
            self.page.get_by_test_id("postalCode").clear()

    def click_continue_button(self):
        self.page.get_by_test_id("continue").click()

    def click_finish_button(self):
        self.page.get_by_test_id("finish").click()

    def checkout_complete_text_should_be_present(self):
        expect(self.page.get_by_test_id("complete-text")).to_be_visible()

    def error_message_text_should_be_consistent(self, missing_input):
        expect(self.page.get_by_test_id("error")).to_have_text(f"Error: {missing_input} is required")
