from pages.crm_page import CrmPage
from pages.sidebar import Sidebar
from tests.base_test import BaseTest


class TestThree(BaseTest):

    def test_three(self):
        email = "demo@example.com"
        password = "demo#123"

        assert self.login_page.is_login_page_opened(), "Login page was not opened.!"
        """Sign in"""
        self.login_page.sign_in(email, password)

        sidebar = Sidebar(self.driver)
        assert sidebar.is_sidebar_opened(), "The authentication failed.!"

        sidebar.click_on_dashboard()
        sidebar.click_on_crm()

        """Get revenue"""
        crm_page = CrmPage(self.driver)
        assert crm_page.is_crm_page_opened(), "The Crm page is not opened.!"

        revenue = crm_page.get_revenue()
        assert revenue is not ' ', "The revenue is empty.!"
