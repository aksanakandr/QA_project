from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base import Base


class LoginPage(Base):
    def __init__(self, driver):
        super().__init__(driver)

        self.__email_input_field = (By.XPATH, "//input[@id=\"basic_email\"]")
        self.__password_input_field = (By.XPATH, "//input[@id=\"basic_password\"]")
        self.__sign_in_button = (By.XPATH, "//button")
        self.__preview_iframe = (By.XPATH, "//iframe[@name=\"preview-frame\"]")
        self.__terms_and_conditions = (By.XPATH, "//input[@type=\"checkbox\"]/parent::span")


    def is_login_page_opened(self) -> bool:
        return super()._is_element_present(self.__email_input_field)

    def enter_email(self, email):
        element = self._waits.wait_for_element_to_be_visible(self.__email_input_field)
        element.send_keys(Keys.BACK_SPACE*50)
        element.send_keys(email)

    def get_preview_iframe(self):
        return self._waits.wait_for_element_to_be_visible(self.__preview_iframe)

    def enter_password(self, password):
        element = self._waits.wait_for_element_to_be_visible(self.__password_input_field)
        element.send_keys(Keys.BACK_SPACE * 50)
        element.send_keys(password)

    def click_on_sign_in(self):
        self._waits.wait_for_element_to_be_visible(self.__sign_in_button).click()

    def sign_terms_and_conditions(self):
        self._waits.wait_for_element_to_be_visible(self.__terms_and_conditions).click()

    def switch_to_alert(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            return alert_text
        except Exception as e:
            print("Error  message was not correct")

    def sign_in(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.sign_terms_and_conditions()
        self.click_on_sign_in()




