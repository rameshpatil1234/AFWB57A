import pytest

from generic.base_test import BaseTest
from generic.utility import Excel
from pages.login_page import LoginPage


class TestInValidLogin(BaseTest):
    @pytest.mark.run(order=2)
    def test_invalid_login(self):
        try:
            un = Excel.get_cell_value("../data/input.xlsx", "Invalidlogin", 2, 1)
            pw = Excel.get_cell_value("../data/input.xlsx", "Invalidlogin", 2, 2)
        except:
            un = Excel.get_cell_value("data/input.xlsx", "Invalidlogin", 2, 1)
            pw = Excel.get_cell_value("data/input.xlsx", "Invalidlogin", 2, 2)
        loginpage = LoginPage(self.driver)

        # enter invalid un
        loginpage.set_username(un)
        # enter invalid pw
        loginpage.set_password(pw)
        # click on login button
        loginpage.click_loginbutton()
        # verify error msg is displayed
        result=loginpage.verify_errormsg_is_displayed(self.wait)
        assert result
