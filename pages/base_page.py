from playwright.sync_api import Playwright, Page


class BasePage:
    def __init__(self, page: Page, playwright: Playwright):
        self.page = page
        playwright.selectors.set_test_id_attribute("data-test")

    def open(self, link):
        self.page.goto(link)
