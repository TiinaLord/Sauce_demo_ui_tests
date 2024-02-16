from selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class BasePage:

    def __init__(self, browser):
        self.browser = browser
        self.logger = browser.logger
        self.class_name = type(self).__name__

    @allure.step("Открытие страницы {url}")
    def open_page(self, url):
        self.logger.debug("%s: Opening url: %s" % (self.class_name, url))
        try:
            self.browser.get(self.browser.url)
        except Exception:
            raise WebDriverException()
        return self

    @allure.step("Ввод {locator}, {value}")
    def input(self, locator, value):
        self.logger.debug("%s: Input text: %s" % (self.class_name, str(locator)))
        element = WebDriverWait(self.browser, 5).until(
                EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(value)
        return self

    @allure.step("Клик {element}")
    def click(self, element):
        self.logger.debug("%s: Clicking element: %s" % (self.class_name, str(element)))
        WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(element)).click()