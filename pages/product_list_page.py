from .base_page import BasePage
from playwright.sync_api import expect
from test_data.links import PRODUCT_LIST_PAGE_LINK
import allure


class ProductListPage(BasePage):
    def add_backpack_to_cart(self):
        with allure.step("Add the backpack to the cart"):
            self.page.get_by_test_id("add-to-cart-sauce-labs-backpack").click()

    def add_bolt_t_shirt_to_cart(self):
        with allure.step("Add Bolt T-Shirt to the cart"):
            self.page.get_by_test_id("add-to-cart-sauce-labs-bolt-t-shirt").click()

    def go_to_cart(self):
        with allure.step("Go to the cart"):
            self.page.get_by_test_id("shopping-cart-link").click()

    def page_should_have_product_list_link(self):
        with allure.step("Check that page has the product list link"):
            expect(self.page).to_have_url(PRODUCT_LIST_PAGE_LINK)
