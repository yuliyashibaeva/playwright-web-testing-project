from .base_page import BasePage
from playwright.sync_api import expect


class CheckoutPage(BasePage):
    def fill_customer_info(self, first_name, last_name, postal_code):
        self.page.get_by_test_id("firstName").fill(first_name)
        self.page.get_by_test_id("lastName").fill(last_name)
        self.page.get_by_test_id("postalCode").fill(postal_code)

    def click_continue_button(self):
        self.page.get_by_test_id("continue").click()

    def click_finish_button(self):
        self.page.get_by_test_id("finish").click()

    def checkout_complete_text_should_be_present(self):
        expect(self.page.get_by_test_id("complete-text")).to_be_visible()
        