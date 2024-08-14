from playwright.sync_api import Playwright, Page, expect


class BasePage:
    def __init__(self, page: Page, playwright: Playwright):
        self.page = page
        playwright.selectors.set_test_id_attribute("data-test")  # needed to use custom test-id locator

    def error_message_should_be_present(self):
        expect(self.page.get_by_test_id("error")).to_be_visible()

    def open(self, link):  # TODO: delete if not used
        self.page.goto(link)

    def shopping_cart_badge_should_be_equal_to(self, qty: int):
        expect(self.page.get_by_test_id("shopping-cart-badge")).to_have_text(str(qty))

    def shopping_cart_badge_should_not_be_present(self):
        expect(self.page.get_by_test_id("shopping-cart-link")).to_be_empty()
