from .base_page import BasePage


class CartPage(BasePage):
    def go_to_checkout(self):
        self.page.get_by_test_id("checkout").click()
