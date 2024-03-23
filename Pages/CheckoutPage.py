from selenium.webdriver.common.by import By
from Sauce_demo_ui_tests.Pages.BasePage import BasePage


class CheckoutPage(BasePage):
    TITLE_CHECKOUT = (By.CSS_SELECTOR, "div.header_secondary_container > span")
    FIRST_NAME_FIELD = (By.CSS_SELECTOR, "#first-name")
    LAST_NAME_FIELD = (By.CSS_SELECTOR, "#last-name")
    POSTAL_CODE_FIELD = (By.CSS_SELECTOR, "#postal-code")
    CANCEL_BTN = (By.CSS_SELECTOR, "#cancel")
    CONTINUE_BTN = (By.CSS_SELECTOR, "#continue")
    # Erors
    ERROR_WHEN_ANY_FIELD_EMPTY = (By.CSS_SELECTOR, "div.error-message-container.error > h3")
    FIRST_NAME_MSG = "Error: First Name is required"
    LAST_NAME_MSG = "Error: Last Name is required"
    POSTAL_CODE_MSG = "Error: Postal Code is required"

    def open(self, browser):
        self.open_page(browser)
        url = browser.get(browser.url)
        return url

    def check_title_checkout(self):
        self.element_is_displayed(self.TITLE_CHECKOUT)

    def input_first_name(self):
        self.input(self.FIRST_NAME_FIELD, "George")

    def input_last_name(self):
        self.input(self.LAST_NAME_FIELD, "Zender")

    def input_postal_code(self):
        self.input(self.POSTAL_CODE_FIELD, "635331")

    def click_cancel(self):
        self.click(self.CANCEL_BTN)

    def click_continue(self):
        self.click(self.CONTINUE_BTN)

    def compare_text_error_first_name(self):
        self.compare_text(self.ERROR_WHEN_ANY_FIELD_EMPTY, self.FIRST_NAME_MSG)

    def compare_text_error_last_name(self):
        self.compare_text(self.ERROR_WHEN_ANY_FIELD_EMPTY, self.LAST_NAME_MSG)

    def compare_text_error_postal_code(self):
        self.compare_text(self.ERROR_WHEN_ANY_FIELD_EMPTY, self.POSTAL_CODE_MSG)
        print(self.ERROR_WHEN_ANY_FIELD_EMPTY)
