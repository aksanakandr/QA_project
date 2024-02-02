from selenium.webdriver.common.by import By

from pages.base import Base


class CrmPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.__revenue = (By.XPATH, "//h1[@class=\"gx-mb-1 gx-revenue-title\"]")

    def is_crm_page_opened(self) -> bool:
        return super()._is_element_present(self.__revenue)

    def get_revenue(self) -> str:
        element = self._waits.wait_for_element_to_be_visible(self.__revenue)
        return element.text
