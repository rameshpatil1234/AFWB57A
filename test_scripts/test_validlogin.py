import time

import pytest

from generic.base_test import BaseTest
from generic.utility import Excel
from pages.login_page import LoginPage
from pages.home_page import HomePage

class TestValidLogin(BaseTest):
    @pytest.mark.run(order=1)
    def test_validlogin(self):
        try:
            un=Excel.get_cellvalue("../data/input.xlsx","ValidLogin",2,1)
            pw=Excel.get_cellvalue("../data/input.xlsx","ValidLogin",2,2)
        except:
            un = Excel.get_cellvalue("data/input.xlsx", "ValidLogin", 2, 1)
            pw = Excel.get_cellvalue("data/input.xlsx", "ValidLogin", 2, 2)
        loginpage = LoginPage(self.driver)
        # 1. Enter valid username
        loginpage.set_username(un)
        # 2. Enter valid password
        loginpage.set_password(pw)
        # 3. click on login button
        loginpage.click_loginbutton()
        # 4. verify that home page is displayed
        homepage=HomePage(self.driver)
        result=homepage.verify_homepage_is_displayed(self.wait)
        assert result



