from selenium.webdriver.common.by import By
from Sauce_demo_ui_tests.Pages.BasePage import BasePage
import pytest


class ProductsPage(BasePage):
    #Products
        #Backpack
    BACKPACK_PRICE = (By.CSS_SELECTOR, "#inventory_container > div > div:nth-child(1) > div.inventory_item_description > div.pricebar > div")
    BACKPACK_NAME = (By.CSS_SELECTOR, "#item_4_title_link > div")
    BACKPACK_ADD_CART_BTN = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")
    CHECK_BACKPACK_PRICE = "$29.99"
    CHECK_BACKPACK_NAME = "Sauce Labs Backpack"
        #T_Shirt
    SHIRT_PRICE = (By.CSS_SELECTOR, "div:nth-child(3) > div.inventory_item_description > div.pricebar > div")
    SHIRT_NAME = (By.CSS_SELECTOR, "#item_1_title_link > div")
    SHIRT_ADD_CART = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt")
    CHECK_SHIRT_PRICE = "$15.99"
    CHECK_SHIRT_NAME = "Sauce Labs Bolt T-Shirt"
    #Footer
    PRODUCTS_TITLE = (By.CSS_SELECTOR, "div.header_secondary_container > span")
    #Burger
    OPEN_BURGER_BTN = (By.CSS_SELECTOR, "#react-burger-menu-btn")
    CLOSE_BURGER_BTN = (By.CSS_SELECTOR, "#react-burger-cross-btn")
    ALL_ITEMS_BTN = (By.CSS_SELECTOR, "#inventory_sidebar_link")
    ABOUT_BTN = (By.CSS_SELECTOR, "#about_sidebar_link")
    LOGOUT_BTN = (By.CSS_SELECTOR, "#logout_sidebar_link")
    RESET_APP_STATE_BTN = (By.CSS_SELECTOR, "#reset_sidebar_link")
    #Social_media_btns
    X_BTN = (By.CSS_SELECTOR, "li.social_twitter > a")
    META_BTN = (By.CSS_SELECTOR, "li.social_facebook > a")
    LINKEDIN_BTN = (By.CSS_SELECTOR, "li.social_linkedin > a")
    #GoCart
    CART_BTN = (By.CSS_SELECTOR, "#shopping_cart_container > a")

    def open(self, browser):
        self.open_page(browser)
        url = browser.get(browser.url)
        return url

    def compare_backpack_price(self):
        self.compare_text(self.BACKPACK_PRICE, self.CHECK_BACKPACK_PRICE)

    def compare_shirt_price(self):
        self.compare_text(self.SHIRT_PRICE, self.CHECK_SHIRT_PRICE)

    def compare_backpack_name(self):
        self.compare_text(self.BACKPACK_NAME, self.CHECK_BACKPACK_NAME)

    def compare_shirt_name(self):
        self.compare_text(self.SHIRT_NAME, self.CHECK_BACKPACK_NAME)

    def open_burger_menu(self):
        self.click(self.OPEN_BURGER_BTN)

    def check_burger_menu_is_displayed(self):
        self.element_is_displayed(self.OPEN_BURGER_BTN)

    def close_burger_menu(self):
        self.click(self.CLOSE_BURGER_BTN)

    def check_burger_list(self):
        self.element_is_displayed(self.ALL_ITEMS_BTN)
        self.element_is_displayed(self.ABOUT_BTN)
        self.element_is_displayed(self.LOGOUT_BTN)
        self.element_is_displayed(self.RESET_APP_STATE_BTN)

    def scroll_to_media_links(self):
        self.scroll_to_element_item(self.X_BTN)

    def check_media_btns_is_displayed(self):
        self.element_is_displayed(self.X_BTN)
        self.element_is_displayed(self.META_BTN)
        self.element_is_displayed(self.LINKEDIN_BTN)

    def click_cart_btn(self):
        self.click(self.CART_BTN)

    def click_add_backpack_to_cart(self):
        self.click(self.BACKPACK_ADD_CART_BTN)

    def click_add_shirt_to_cart(self):
        self.click(self.SHIRT_ADD_CART)

    def check_title_products(self):
        self.element_is_displayed(self.PRODUCTS_TITLE)
