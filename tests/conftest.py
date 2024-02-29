import logging
import datetime
import pytest
import json
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.firefox.service import Service as FFService


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--url", action="store", default="https://www.saucedemo.com")
    parser.addoption("--log_level", action="store", default="DEBUG")
    parser.addoption("--platform", default="Linux")
    parser.addoption("--logs", action="store_true")


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    log_level = request.config.getoption("--log_level")

    logger = logging.getLogger(request.node.name)
    logger.setLevel(level=log_level)
    logger.info("===> Test %s started at %s" % (request.node.name, datetime.datetime.now()))
    if browser_name == "chrome":
        service = ChromiumService()
        driver = webdriver.Chrome(service=service)
    elif browser_name == "firefox":
        service = FFService()
        driver = webdriver.Firefox(service=service)
    else:
        raise ValueError

    allure.attach(
        name=driver.session_id,
        body=json.dumps(driver.capabilities),
        attachment_type=allure.attachment_type.JSON)

    driver.maximize_window()
    driver.get(url)
    driver.url = url
    driver.log_level = log_level
    driver.logger = logger
    driver.test_name = request.node.name
    logger.info("Browser %s started" % browser)\


    def pytest_runtest_makereport(item, call):
        if call.when == "call" and call.outcome == "failed":
            driver = item.funcargs['browser']
            allure.attach(
                driver.get_screenshot_as_png(),
                name="Screenshot on failure",
                attachment_type=AttachmentType.PNG
            )

    def fin():
        logger.info("===> Test %s finished at %s" % (request.node.name, datetime.datetime.now()))

    request.addfinalizer(fin)
    return driver

