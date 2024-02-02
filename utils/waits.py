from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Waits:
    def __init__(self, driver, timeout):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(self.driver, self.timeout)

    def wait_for_element_to_be_visible(self, by_locator):
        return self.wait.until(EC.visibility_of_element_located(by_locator))

    def wait_for_element_to_be_clickable(self, by_locator):
        return self.wait.until(EC.element_to_be_clickable(by_locator))

    def wait_for_element_to_disappear(self, by_locator):
        return self.wait.until(EC.invisibility_of_element_located(by_locator))

    def wait_for_elements_to_be_visible(self, by_locator):
        return self.wait.until(EC.visibility_of_all_elements_located(by_locator))
