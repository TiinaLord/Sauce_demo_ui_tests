from Sauce_demo_ui_tests.Pages.LoginPage import LoginPage
from Sauce_demo_ui_tests.Pages.ProductsPage import ProductsPage
from Sauce_demo_ui_tests.Pages.CartPage import CartPage
from Sauce_demo_ui_tests.Pages.CheckoutPage import CheckoutPage


def test_checkout_cancel(browser):
    login_page = LoginPage(browser)
    login_page.open(browser)
    login_page.input_login_standard()
    login_page.input_pass_and_click()
    products_page = ProductsPage(browser)
    products_page.click_cart_btn()
    cart_page = CartPage(browser)
    cart_page.click_checkout()
    checkout_page = CheckoutPage(browser)
    checkout_page.click_cancel()
    cart_page.check_title_cart()


def test_checkout_errors(browser):
    login_page = LoginPage(browser)
    login_page.open(browser)
    login_page.input_login_standard()
    login_page.input_pass_and_click()
    products_page = ProductsPage(browser)
    products_page.click_cart_btn()
    cart_page = CartPage(browser)
    cart_page.click_checkout()
    checkout_page = CheckoutPage(browser)
    # First try
    checkout_page.click_continue()
    checkout_page.compare_text_error_first_name()
    # Second try
    checkout_page.input_first_name()
    checkout_page.click_continue()
    checkout_page.compare_text_error_last_name()
    # Third try
    checkout_page.input_last_name()
    checkout_page.click_continue()
    checkout_page.compare_text_error_postal_code()
