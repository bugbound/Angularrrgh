class Angular16Helper:
    @staticmethod
    def getAppName():
        return "w00p-ng"
        
    @staticmethod
    def getModules(webdriver):
        script = "return Object.keys(angular.element(document.body).injector().modules);"
        try:
            modules = webdriver.execute_script(script)
            return modules
        except:
            raise

    @staticmethod
    def getVersion(webdriver):
        script = "return angular.version.full;"
        try:
            return webdriver.execute_script(script)
        except:
            raise

    @staticmethod
    def getRequires(webdriver, moduleName):
        script = "return angular.module('"+moduleName+"').requires;"
        try:
            return webdriver.execute_script(script)
        except:
            raise
