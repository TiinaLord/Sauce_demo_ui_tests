from Sauce_demo_ui_tests.Pages.LoginPage import LoginPage
from Sauce_demo_ui_tests.Pages.ProductsPage import ProductsPage


def test_open_close_burger(browser):
    login_page = LoginPage(browser)
    login_page.open(browser)
    login_page.input_login_standard()
    login_page.input_pass_and_click()
    products_page = ProductsPage(browser)
    products_page.check_burger_menu_is_displayed()
    products_page.open_burger_menu()
    products_page.close_burger_menu()
    products_page.check_burger_menu_is_displayed()


def test_check_burger_list(browser):
    login_page = LoginPage(browser)
    login_page.open(browser)
    login_page.input_login_standard()
    login_page.input_pass_and_click()
    products_page = ProductsPage(browser)
    products_page.open_burger_menu()
    products_page.check_burger_list()


def test_media_links_is_displayed(browser):
    login_page = LoginPage(browser)
    login_page.open(browser)
    login_page.input_login_standard()
    login_page.input_pass_and_click()
    products_page = ProductsPage(browser)
    products_page.scroll_to_media_links()
    products_page.check_media_btns_is_displayed()