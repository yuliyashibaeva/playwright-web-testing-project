from .base_page import BasePage
from playwright.sync_api import expect
import allure


class CheckoutPage(BasePage):
    def fill_in_customer_info(self, first_name, last_name, postal_code, missing_input: str = None):
        with allure.step(f"Fill in customer info: First Name = {first_name}, Last Name = {last_name}, "
                         f"Postal Code = {postal_code}, Missing input = {missing_input}"):
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
        with allure.step("Click \"Continue\" button"):
            self.page.get_by_test_id("continue").click()

    def click_finish_button(self):
        with allure.step("Click \"Finish\" button"):
            self.page.get_by_test_id("finish").click()

    def checkout_completion_text_should_be_present(self):
        with allure.step("Check that completion text is present on the page"):
            expect(self.page.get_by_test_id("complete-text")).to_be_visible()

    def error_message_text_should_be_consistent(self, missing_input):
        with allure.step(f"Check that the message \"Error: {missing_input} is required\" is present on the page"):
            expect(self.page.get_by_test_id("error")).to_have_text(f"Error: {missing_input} is required")
