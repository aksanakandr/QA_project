from selenium.webdriver.common.by import By

from pages.base import Base


class Sidebar(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.__dashboard = (By.XPATH, "//div[@role=\"menuitem\"]//following-sibling::span")
        self.__crm = (By.XPATH, "//div[@role=\"menuitem\"]//following-sibling::ul/li[2]")
        self.__mail_app = (
            By.XPATH, "//div[contains(text(),\"In-built\")]/parent::li/ul/li[1]")

    def click_on_dashboard(self):
        self._waits.wait_for_element_to_be_clickable(self.__dashboard).click()

    def click_on_mail_app(self):
        self._waits.wait_for_element_to_be_clickable(self.__mail_app).click()

    def click_on_crm(self):
        self._waits.wait_for_element_to_be_clickable(self.__crm).click()

    def is_sidebar_opened(self) -> bool:
        return super()._is_element_present(self.__dashboard)
