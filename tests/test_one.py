from tests.base_test import BaseTest


class TestOne(BaseTest):

    def test_one(self):
        email = "demo1@company.com"
        password = "123456"

        assert self.login_page.is_login_page_opened(), "Login page was not opened!"
        """Sign in"""
        self.login_page.sign_in(email, password)
        """Verify error message"""
        assert self.login_page.switch_to_alert() == "Access to this account has been temporarily " \
                                                    "disabled due to many failed login attempts." \
                                                    "You can immediately restore it by resetting " \
                                                    "your password or you can try again later"

        # We will get assertion error in this test and  test will fail

