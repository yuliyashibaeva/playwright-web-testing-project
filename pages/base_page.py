from playwright.sync_api import Playwright, Page, expect
import allure


class BasePage:
    def __init__(self, page: Page, playwright: Playwright):
        self.page = page
        playwright.selectors.set_test_id_attribute("data-test")  # needed to use custom test-id locator

    def error_message_should_be_present(self):
        with allure.step("Check that validation message is present"):
            expect(self.page.get_by_test_id("error")).to_be_visible()

    def remove_backpack_from_cart(self):
        with allure.step("Remove backpack from the cart"):
            self.page.get_by_test_id("remove-sauce-labs-backpack").click()

    def shopping_cart_badge_should_be_equal_to(self, qty: int):
        with allure.step(f"Shopping cart badge should contain {qty} item(s)"):
            expect(self.page.get_by_test_id("shopping-cart-badge")).to_have_text(str(qty))

    def shopping_cart_badge_should_not_be_present(self):
        with allure.step("The cart should be empty"):
            expect(self.page.get_by_test_id("shopping-cart-link")).to_be_empty()
