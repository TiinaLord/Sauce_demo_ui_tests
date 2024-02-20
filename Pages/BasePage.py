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

    @allure.step("Отображение элемента {locator}")
    def element_is_displayed(self, locator):
        self.logger.debug("%s: FInding display element: %s" % (self.class_name, str(locator)))
        try:
            check_locator = WebDriverWait(self.browser, 5).until(
                EC.visibility_of_element_located(locator)).is_displayed()
            if check_locator is True:
                return check_locator
            else:
                raise AssertionError(f"'Элемент не отобразился, локатор:' {locator}")
        except TimeoutException:
            raise AssertionError(f"'Элемент не отобразился, локатор:' {locator}")

    @allure.step("Элемент не отображается {locator}")
    def element_is_not_displayed(self, locator):
        self.logger.debug("%s: FInding display element: %s" % (self.class_name, str(locator)))
        try:
            check_locator = WebDriverWait(self.browser, 5).until(
                EC.invisibility_of_element_located(locator))
            if check_locator is True:
                return check_locator
            else:
                raise AssertionError(f"'Элемент отобразился, локатор:' {locator}")
        except TimeoutException:
            raise AssertionError(f"'Элемент отобразился, локатор:' {locator}")

    @allure.step("Сравнение текста {compared_text}")
    def compare_text(self, locator, compared_text):
        self.logger.debug("%s: Comparing text: %s" % (self.class_name, compared_text))
        try:
            text_from_locator = WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(locator)).text
            return text_from_locator == compared_text
        except TimeoutException:
            raise AssertionError(f"'Текст не сходится' {locator}")

    def scroll_to_element_item(self, element):
        self.logger.debug("%s: Scrolling to element: %s" % (self.class_name, str(element)))
        locator = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(element))
        ActionChains(self.browser).scroll_to_element(locator).perform()
