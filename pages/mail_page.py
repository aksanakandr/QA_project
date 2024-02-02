from selenium.webdriver.common.by import By
from pages.base import Base


class MailPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.__compose = (By.XPATH, "//button[contains(text(),\"COMPOSE\")]")
        self.__email_address = (By.XPATH, "//div[@class=\"ant-modal-body\"]/div[1]/input")
        self.__subject = (By.XPATH, "//div[@class=\"ant-modal-body\"]/div[2]/input")
        self.__message = (By.XPATH, "//div[@class=\"ant-modal-body\"]/div/textarea")
        self.__attach_files = (By.XPATH, "//input[@type=\"file\"]/following-sibling::button")
        self.__ok = (By.XPATH, "//div[@class=\"ant-modal-footer\"]/button[2]")
        self.__mail_status = (By.XPATH, "//*[contains(text(),\"Mail Sent Successfully\")]")

    def is_mail_page_opened(self) -> bool:
        return super()._is_element_present(self.__compose)

    def click_on_compose(self):
        self._waits.wait_for_element_to_be_clickable(self.__compose).click()

    def enter_email_address(self, email_address):
        self._waits.wait_for_element_to_be_visible(self.__email_address).send_keys(email_address)

    def enter_email_subject(self, subject):
        self._waits.wait_for_element_to_be_visible(self.__subject).send_keys(subject)

    def enter_email_message(self, message):
        self._waits.wait_for_element_to_be_visible(self.__message).send_keys(message)

    def click_on_attach_file(self):
        self._waits.wait_for_element_to_be_visible(self.__attach_files).click()

    def click_on_attach_ok(self):
        self._waits.wait_for_element_to_be_visible(self.__ok).click()

    def is_mail_sent_successfully(self) -> bool:
        return super()._is_element_present(self.__mail_status)
