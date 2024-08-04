from .base_page import BasePage


class ProductListPage(BasePage):
    def add_bolt_t_shirt_to_cart(self):
        self.page.get_by_test_id("add-to-cart-sauce-labs-bolt-t-shirt").click()

    def go_to_cart(self):
        self.page.get_by_test_id("shopping-cart-link").click()