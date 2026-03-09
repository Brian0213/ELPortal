import time
from Pages.LoginPage import LoginPage
from utility.readProperties import ReadConfig
from utility.customLogger import LogGen


class BaseTestL:
    baseURL = ReadConfig.getApplicationURL()
    usernameL = ReadConfig.getUseremailL()
    passwordL = ReadConfig.getPasswordL()
    logger = LogGen.loggen()

    def login(self, elportal):
        self.logger.info("****** Starting login ******")
        elportal.implicitly_wait(10)
        elportal.get(self.baseURL)
        login_page = LoginPage(elportal)
        self.logger.info("******** Click the Home Button ********")
        login_page.clickHomeButton()
        login_page.emailAddress(self.usernameL)
        login_page.setPassword(self.passwordL)
        login_page.clickSignin()
        # time.sleep(2)
        self.logger.info("****** Login successful ******")
