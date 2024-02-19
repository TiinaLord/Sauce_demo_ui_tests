from selenium.webdriver.common.by import By
from Sauce_demo_ui_tests.Pages.BasePage import BasePage


class CartPage(BasePage):
    TITLE_YOUR_CART = (By.CSS_SELECTOR, "div.header_secondary_container > span")
    CONTINUE_SHOPPING_BTN = (By.CSS_SELECTOR, "#continue-shopping")
    CHECKOUT_BTN = (By.CSS_SELECTOR, "#checkout")
    REMOVE_BTN = (By.CSS_SELECTOR, "#remove-sauce-labs-backpack")
    FIRST_NUMBER_IN_CART = (By.CSS_SELECTOR, "div.cart_item > div.cart_quantity")

    def open(self, browser):
        self.open_page(browser)
        url = browser.get(browser.url)
        return url

    def check_elements_on_page(self):
        self.element_is_displayed(self.TITLE_YOUR_CART)
        self.element_is_displayed(self.CONTINUE_SHOPPING_BTN)
        self.element_is_displayed(self.CHECKOUT_BTN)

    def check_number_is_displayed(self):
        self.element_is_displayed(self.FIRST_NUMBER_IN_CART)

    def check_remove_btn(self):
        self.element_is_displayed(self.REMOVE_BTN)
    def check_number_is_not_displayed_in_empty_cart(self):
        self.element_is_not_displayed(self.FIRST_NUMBER_IN_CART)

    def click_continue_shopping(self):
        self.click(self.CONTINUE_SHOPPING_BTN)

    def click_checkout(self):
        self.click(self.CHECKOUT_BTN)

    def click_remove(self):
        self.click(self.REMOVE_BTN)

    def check_title_cart(self):
        self.element_is_displayed(self.TITLE_YOUR_CART)
