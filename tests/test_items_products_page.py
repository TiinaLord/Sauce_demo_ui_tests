from Sauce_demo_ui_tests.Pages.LoginPage import LoginPage
from Sauce_demo_ui_tests.Pages.ProductsPage import ProductsPage


def test_check_backpack_price(browser):
    login_page = LoginPage(browser)
    login_page.open(browser)
    login_page.input_login_standard()
    login_page.input_pass_and_click()
    products_page = ProductsPage(browser)
    products_page.compare_backpack_price()


def test_check_shirt_price(browser):
    login_page = LoginPage(browser)
    login_page.open(browser)
    login_page.input_login_standard()
    login_page.input_pass_and_click()
    products_page = ProductsPage(browser)
    products_page.compare_shirt_price()


def test_check_backpack_name(browser):
    login_page = LoginPage(browser)
    login_page.open(browser)
    login_page.input_login_standard()
    login_page.input_pass_and_click()
    products_page = ProductsPage(browser)
    products_page.compare_backpack_name()


def test_compare_shirt_name(browser):
    login_page = LoginPage(browser)
    login_page.open(browser)
    login_page.input_login_standard()
    login_page.input_pass_and_click()
    products_page = ProductsPage(browser)
    products_page.compare_shirt_name()
