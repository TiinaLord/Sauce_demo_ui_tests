from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class LoginPage(BasePage):
    # Fields and btn
    LOGIN_FIELD = (By.CSS_SELECTOR, "#user-name")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#password")
    BTN_LOG_IN = (By.CSS_SELECTOR, "#login-button")
    # Some elements and texts
    CHECK_TEXT_PRODUCTS = (By.CSS_SELECTOR, "div.header_secondary_container > span")
    CHECK_ERROR_AFTER_LOG_IN = (By.CSS_SELECTOR, "div.error-message-container.error > h3")
    TEXT_ERROR = "Epic sadface: Sorry, this user has been locked out."
    # Creds
    LOGIN_CRED = ["standard_user", "locked_out_user", "problem_user", "performance_glitch_user", "error_user",
                  'visual_user']
    PASSWORD_CRED = "secret_sauce"

    def open(self, browser):
        self.open_page(browser)
        url = browser.get(browser.url)
        return url

    # @pytest.mark.parametrize(LOGIN_CRED, ["standard_user", "locked_out_user", "problem_user", "performance_glitch_user",
    #    "error_user", 'visual_user'])
    def input_login_standard(self):
        self.input(self.LOGIN_FIELD, self.LOGIN_CRED[0])

    def input_login_locked(self):
        self.input(self.LOGIN_FIELD, self.LOGIN_CRED[1])

    def input_login_problem(self):
        self.input(self.LOGIN_FIELD, self.LOGIN_CRED[2])

    def input_login_perfomance(self):
        self.input(self.LOGIN_FIELD, self.LOGIN_CRED[3])

    def input_login_error(self):
        self.input(self.LOGIN_FIELD, self.LOGIN_CRED[4])

    def input_login_visual(self):
        self.input(self.LOGIN_FIELD, self.LOGIN_CRED[5])

    def input_pass_and_click(self):
        self.input(self.PASSWORD_FIELD, self.PASSWORD_CRED)
        self.click(self.BTN_LOG_IN)

    def check_element_after_log_in(self):
        self.element_is_displayed(self.CHECK_TEXT_PRODUCTS)

    def check_element_after_error(self):
        self.element_is_displayed(self.CHECK_ERROR_AFTER_LOG_IN)

    def compare_text_error(self):
        self.compare_text(self.CHECK_ERROR_AFTER_LOG_IN, self.TEXT_ERROR)
