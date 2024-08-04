from .base_page import BasePage


class CartPage(BasePage):
    def go_to_checkout(self):
        self.page.get_by_test_id("checkout").click()

    def remove_backpack_from_cart(self):
        self.page.get_by_test_id("remove-sauce-labs-backpack").click()
