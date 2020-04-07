from selenium import webdriver
from selenium.webdriver import Chrome


class WebDriverUtil:
    @staticmethod
    def getWebDriver(proxy):
        
        chrome_options = webdriver.ChromeOptions()
        if(proxy):
            chrome_options.add_argument("--proxy-server={0}".format(proxy))
        driver = Chrome(chrome_options=chrome_options)
		
        return driver
