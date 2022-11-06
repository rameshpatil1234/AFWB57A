from generic.base_test import BaseTest
from generic.utility import Excel


class TestScript1(BaseTest):

    def test_script1(self):
        print('This is my script1')
        print(self.driver.title)
        v=Excel.get_cellvalue("../data/input.xlsx","Sheet1",2,1)
        print(v)