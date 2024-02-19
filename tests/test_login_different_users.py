from Sauce_demo_ui_tests.Pages.LoginPage import LoginPage


def test_log_in_standard_user(browser):
    login_page = LoginPage(browser)
    login_page.open(browser)
    login_page.input_login_standard()
    login_page.input_pass_and_click()
    login_page.check_element_after_log_in()


def test_log_in_problem_user(browser):
    login_page = LoginPage(browser)
    login_page.open(browser)
    login_page.input_login_problem()
    login_page.input_pass_and_click()
    login_page.check_element_after_log_in()


def test_log_in_perfomance_user(browser):
    login_page = LoginPage(browser)
    login_page.open(browser)
    login_page.input_login_perfomance()
    login_page.input_pass_and_click()
    login_page.check_element_after_log_in()


def test_log_in_error_user(browser):
    login_page = LoginPage(browser)
    login_page.open(browser)
    login_page.input_login_error()
    login_page.input_pass_and_click()
    login_page.check_element_after_log_in()


def test_log_in_visual_user(browser):
    login_page = LoginPage(browser)
    login_page.open(browser)
    login_page.input_login_visual()
    login_page.input_pass_and_click()
    login_page.check_element_after_log_in()


def test_log_in_locked_user(browser):
    login_page = LoginPage(browser)
    login_page.open(browser)
    login_page.input_login_locked()
    login_page.input_pass_and_click()
    login_page.check_element_after_error()
    login_page.compare_text_error()
