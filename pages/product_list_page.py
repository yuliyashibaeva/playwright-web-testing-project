from .base_page import BasePage


class ProductListPage(BasePage):
    def add_backpack_to_cart(self):
        self.page.get_by_test_id("add-to-cart-sauce-labs-backpack").click()

    def add_bolt_t_shirt_to_cart(self):
        self.page.get_by_test_id("add-to-cart-sauce-labs-bolt-t-shirt").click()

    def delete_backpack_from_list_page(self):
        self.page.get_by_test_id("remove-sauce-labs-backpack").click()

    def go_to_cart(self):
        self.page.get_by_test_id("shopping-cart-link").click()
