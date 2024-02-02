import os
from pages.mail_page import MailPage
from pages.sidebar import Sidebar
from tests.base_test import BaseTest
from utils.files import save_file


class TestFour(BaseTest):

    def test_four(self):
        email = "demo@example.com"
        password = "demo#123"

        email_address = "smaple@company.com"
        subject = "Something"
        message = "A new test Message"
        file_name = "attachment.txt"

        assert self.login_page.is_login_page_opened(), "Login page was not opened!"
        """Sign in"""
        self.login_page.sign_in(email, password)

        sidebar = Sidebar(self.driver)
        assert sidebar.is_sidebar_opened(), "The authentication failed!"

        sidebar.click_on_mail_app()

        mail_page = MailPage(self.driver)
        assert mail_page.is_mail_page_opened(), "Mail page was not opened!"

        """Send message"""
        mail_page.click_on_compose()
        mail_page.enter_email_address(email_address)
        mail_page.enter_email_subject(subject)
        mail_page.enter_email_message(message)

        mail_page.click_on_attach_file()

        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_dir, file_name)
        save_file(file_path)

        """Verify mail send successfully"""
        mail_page.click_on_attach_ok()
        assert mail_page.is_mail_sent_successfully(), "Email was not sent.!"
