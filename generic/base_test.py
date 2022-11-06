import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from pyjavaproperties import Properties
from selenium.webdriver import  ChromeOptions
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.support.wait import WebDriverWait


class BaseTest:

    @pytest.fixture(autouse=True)
    def pre_post_condition(self):
        # create object of Properties class
        pfile = Properties()
        # open the property file
        pfile.load(open('../config.properties'))
        # get the value by specifying the key
        browser = pfile['browser']
        url = pfile['url']
        ITO = pfile['ITO']
        ETO = pfile['ETO']
        usegrid=pfile['usegrid']
        gridurl=pfile['gridurl']

        if usegrid=='no':
            if browser == 'chrome':
                self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
                print('Lunched chrome browser in local system')
            else:
                self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
                print('Lunched firefox browser in local system')
        else:
            if browser == 'chrome':
                browseroptions=ChromeOptions()
                print('Lunched chrome browser in remote system')
            else:
                browseroptions=FirefoxOptions()
                print('Lunched firefox browser in remote system')
            self.driver =webdriver.Remote(gridurl,options=browseroptions)

        # maximize the browser
        self.driver.maximize_window()
        # enter the URL
        print("Enter the url")
        self.driver.get(url)

        # set the timeout
        print("Set ITO:",ITO)
        self.driver.implicitly_wait(ITO)
        print("Set ETO:",ETO)
        self.wait=WebDriverWait(self.driver,ETO)
        # close the browser
        yield
        print("Close the browser")
        self.driver.quit()