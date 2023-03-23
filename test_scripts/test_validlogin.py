import time

from generic.base_test import BaseTest
from generic.utility import Excel
from pages.login_page import LoginPage
from pages.home_page import HomePage

class TestValidLogin(BaseTest):

    def test_valid_login(self):
        loginpage=LoginPage(self.driver)
        loginpage.set_username("admin")
        loginpage.set_password("manager")
        loginpage.click_loginbutton()
        homepage=HomePage(self.driver)
        homepage.verify_logout_is_displayed(self.wait)
        time.sleep(5)
