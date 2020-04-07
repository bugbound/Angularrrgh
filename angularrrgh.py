#!/bin/python
"""Usage: 
	angularrrgh.py [--proxy=<proxy>] [--keepopen] [--verbose] [--angular=<angular-version>] <url>
	angularrrgh.py -h | --help
	angularrrgh.py --version
	
Options:
    --proxy=<proxy>    		       set browser to use proxy, eg --proxy=http://localhost:8080
    --angular=<angular-version>    Use this version of angular, Currently supplots 1.6.x
    --keepopen                     leave browser window open on app exit
	-h --help                      how this
	--version                      shows the current version
    
Arguments:
    <url>                          url with angular app eg http://example.com/myapp/index.html
"""
from docopt import docopt
import time

from libs.WebDriverUtil import *
from libs.Angular16Helper import *

class AngularrrghTool:
    @staticmethod
    def doit(webdriver, angularHelper, url, verbose):
        webdriver.get(url)
        time.sleep(10)
        print("Angular Version: %s"%angularHelper.getVersion(webdriver))
        print("App Name: %s"%angularHelper.getAppName())
        modules = angularHelper.getModules(webdriver)
        print("Modules: Found %d modules"%len(modules))
        if verbose:
            for x in modules:
                print(x)
                print("\t requires: %s"%angularHelper.getRequires(webdriver, x))
                print('')
        print('')


if __name__ == "__main__":
    arguments = docopt(__doc__, version='angularrrgh 0.1 BETA')
    proxy = arguments['--proxy']
    keepopen = arguments['--keepopen']
    verbose = arguments['--verbose']
    driver = WebDriverUtil.getWebDriver(proxy)
    url = arguments['<url>']
    AngularrrghTool.doit(driver, Angular16Helper, url, verbose)
    
    if(keepopen == False):
        driver.quit()
