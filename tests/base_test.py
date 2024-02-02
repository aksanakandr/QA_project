import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service

from pages.login_page import LoginPage


class BaseTest:
    driver = None
    url = ("https://preview.themeforest.net/item/wieldy-react-redux-ant-design-admin-template/full_screen_preview"
           "/22719616?_ga=2.62160101.837904251.1706544053-1484721041.1706544053")
    login_page = None

    @classmethod
    def setup_class(cls):
        browser = "Chrome"

        if browser == "Chrome":
            chrome_driver_service = Service(ChromeDriverManager().install())
            cls.driver = webdriver.Chrome(service=chrome_driver_service)
        elif browser == "Firefox":
            firefox_driver_service = Service(GeckoDriverManager().install())
            cls.driver = webdriver.Firefox(service=firefox_driver_service)
        else:
            pytest.fail(f"{browser} browser is not supported.")

        cls.driver.maximize_window()
        cls.driver.get(cls.url)

        cls.login_page = LoginPage(cls.driver)

        if browser == "Chrome":
            # Note: In Chrome, elements within an iframe must be accessed by switching to it, unlike in Firefox where
            # this step isn't necessary.
            frame = cls.login_page.get_preview_iframe()
            cls.driver.switch_to.frame(frame)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
