from pages.sidebar import Sidebar
from tests.base_test import BaseTest


class TestTwo(BaseTest):

    def test_two(self):
        email = "demo@example.com"
        password = "demo#123"

        assert self.login_page.is_login_page_opened(), "Login page was not opened!"
        """Sign in"""
        self.login_page.sign_in(email, password)

        sidebar = Sidebar(self.driver)
        """Checking login successfully"""
        assert sidebar.is_sidebar_opened(), "The authentication failed!"


