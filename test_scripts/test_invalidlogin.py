import pytest

from generic.base_test import BaseTest
from generic.utility import Excel
from pages.login_page import LoginPage


class TestInvalidLogin(BaseTest):
    @pytest.mark.run(order=2)
    def test_invlidlogin(self):
        un=Excel.get_cellvalue("../data/input.xlsx","InvalidLogin",2,1)
        pw=Excel.get_cellvalue("../data/input.xlsx","InvalidLogin",2,2)
        # 1. Enter invalid un
        loginpage=LoginPage(self.driver)
        loginpage.set_username(un)
        # 2. Enter invalid pw
        loginpage.set_password(pw)
        # 3. Click login
        loginpage.click_loginbutton()
        # 4. Verify that error msg is displayed
        result=loginpage.verify_errmsg_displayed(self.wait)
        assert result