import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service
from pyjavaproperties import Properties
from selenium.webdriver import ChromeOptions
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.support.wait import WebDriverWait


class BaseTest:

    @pytest.fixture(autouse=True)
    def pre_post_condition(self):
        pfile = Properties()
        pfile.load(open('../config.properties'))
        browser = pfile['browser']
        url = pfile['url']
        ITO = pfile['ITO']
        ETO = pfile['ETO']
        use_grid=pfile['use_grid']
        grid_url=pfile['grid_url']

        if use_grid == 'no':
            if browser == 'chrome':
                self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
                print('Launched chrome browser in local system')
            else:
                self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
                print('Launched firefox browser in local system')
        else:
            if browser == 'chrome':
                browser_options = ChromeOptions()
                print('Launched chrome browser in remote system')
            else:
                browser_options = FirefoxOptions()
                print('Launched firefox browser in remote system')
            self.driver = webdriver.Remote(grid_url,options=browser_options)

        self.driver.maximize_window()
        print('Enter the url:',url)
        self.driver.get(url)

        print("Set ITO:",ITO)
        self.driver.implicitly_wait(ITO)
        print("Set ETO:",ETO)
        self.wait = WebDriverWait( self.driver,ETO)
        yield
        print("Close the browser")
        self.driver.quit()
