from Sauce_demo_ui_tests.Pages.LoginPage import LoginPage
from Sauce_demo_ui_tests.Pages.ProductsPage import ProductsPage
from Sauce_demo_ui_tests.Pages.CartPage import CartPage


def test_empty_cart(browser):
    login_page = LoginPage(browser)
    login_page.open(browser)
    login_page.input_login_standard()
    login_page.input_pass_and_click()
    products_page = ProductsPage(browser)
    products_page.click_cart_btn()
    cart_page = CartPage(browser)
    cart_page.check_number_is_not_displayed_in_empty_cart()


def test_continue_shopping(browser):
    login_page = LoginPage(browser)
    login_page.open(browser)
    login_page.input_login_standard()
    login_page.input_pass_and_click()
    products_page = ProductsPage(browser)
    products_page.click_cart_btn()
    cart_page = CartPage(browser)
    cart_page.click_continue_shopping()
    products_page.check_title_products()


def test_add_backpack_and_go_cart(browser):
    login_page = LoginPage(browser)
    login_page.open(browser)
    login_page.input_login_standard()
    login_page.input_pass_and_click()
    products_page = ProductsPage(browser)
    products_page.click_add_backpack_to_cart()
    products_page.click_cart_btn()
    cart_page = CartPage(browser)
    cart_page.check_number_is_displayed()
    cart_page.check_remove_btn()


def test_add_shirt_and_go_cart(browser):
    login_page = LoginPage(browser)
    login_page.open(browser)
    login_page.input_login_standard()
    login_page.input_pass_and_click()
    products_page = ProductsPage(browser)
    products_page.click_add_shirt_to_cart()
    products_page.click_cart_btn()
    cart_page = CartPage(browser)
    cart_page.check_number_is_displayed()
    cart_page.check_remove_btn()


def test_add_and_remove_item_from_cart(browser):
    login_page = LoginPage(browser)
    login_page.open(browser)
    login_page.input_login_standard()
    login_page.input_pass_and_click()
    products_page = ProductsPage(browser)
    products_page.click_add_backpack_to_cart()
    products_page.click_cart_btn()
    cart_page = CartPage(browser)
    cart_page.check_number_is_displayed()
    cart_page.check_remove_btn()
    cart_page.click_remove()
    cart_page.check_number_is_not_displayed_in_empty_cart()



