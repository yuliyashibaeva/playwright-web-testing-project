from .base_page import BasePage
import allure


class CartPage(BasePage):
    def go_to_checkout(self):
        with allure.step("Go to checkout"):
            self.page.get_by_test_id("checkout").click()
