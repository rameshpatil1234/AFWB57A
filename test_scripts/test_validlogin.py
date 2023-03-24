import time

import pytest

from generic.base_test import BaseTest
from generic.utility import Excel
from pages.login_page import LoginPage
from pages.home_page import HomePage

class TestValidLogin(BaseTest):
    @pytest.mark.run(order=1)
    def test_valid_login(self):
        try:
            un=Excel.get_cell_value("../data/input.xlsx","ValidLogin", 2, 1)
            pw = Excel.get_cell_value("../data/input.xlsx", "ValidLogin", 2, 2)
        except:
            un = Excel.get_cell_value("data/input.xlsx", "ValidLogin", 2, 1)
            pw = Excel.get_cell_value("data/input.xlsx", "ValidLogin", 2, 2)

        loginpage=LoginPage(self.driver)
        loginpage.set_username(un)
        loginpage.set_password(pw)
        loginpage.click_loginbutton()
        homepage=HomePage(self.driver)
        result=homepage.verify_homepage_is_displayed(self.wait)
        assert result

