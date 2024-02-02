from selenium.common import TimeoutException
from selenium.webdriver import ActionChains

from utils.waits import Waits


class Base:
    def __init__(self, driver):
        self.driver = driver
        self._waits = Waits(self.driver, 10)

    def _is_element_present(self, by_locator) -> bool:
        element_present = False
        try:
            self._waits.wait_for_element_to_be_visible(by_locator)
            element_present = True
        except TimeoutException:
            pass
        return element_present

    def _get_action_chains(self) -> ActionChains:
        return ActionChains(self.driver)
