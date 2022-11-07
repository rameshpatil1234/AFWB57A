import time

import time
from generic.base_test import BaseTest
from pages.login_page import LoginPage
from pages.home_page import HomePage

class TestValidLogin(BaseTest):

    def test_validlogin(self):
        loginpage=LoginPage(self.driver)
        # 1.Enter valid username
        loginpage.set_username("admin")
        # 2. Enter valid password
        loginpage.set_password("manager")
        # 3. click on login button
        loginpage.click_loginbutton()
        # 4. verify that homepage is displayed
        homepage=HomePage(self.driver)
        result=homepage.verify_homepage_is_displayed(self.wait)
        assert result

