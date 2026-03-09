import time
import sys
import pytest
from selenium.webdriver.common.by import By

from Pages.DFCPage import DfcPage
from Pages.VCBCPage import VCBCPage
from Pages.LoginPage import LoginPage
from testScripts.base_test import BaseTest
from testData.vcbc_learners import VCBC_STUDENTS
from utility.readProperties import ReadConfig
from utility.customLogger import LogGen

class Test_VCBC_Learner_Schedule:

    baseURL = ReadConfig.getApplicationURL()
    # usernameL = ReadConfig.getUseremailL()
    # passwordL = ReadConfig.getPasswordL()

    logger = LogGen.loggen()

    @pytest.mark.parametrize("learner", VCBC_STUDENTS)
    def test_login(self, setup, learner):
        self.elportal = setup
        self.logger.info("******** Verifying Login Test ********")
        self.logger.info("******** Call the Browse Configuration ********")
        self.elportal.implicitly_wait(10)
        self.logger.info("******** Launch the Application URL ********")
        self.elportal.get(self.baseURL)
        self.logger.info("******** Define the LoginPage Driver ********")
        self.elp = LoginPage(self.elportal)
        self.vcb = VCBCPage(self.elportal)
        self.logger.info("******** Click the Home Button ********")
        self.elp.clickHomeButton()
        self.logger.info("******** Enter the Username ********")
        self.elp.emailAddress(learner["email"])
        self.logger.info("******** Enter the Password ********")
        self.elp.setPassword(learner["password"])
        self.logger.info("******** Click the Sign in Button********")
        self.elp.clickSignin()
        self.logger.info("******** Click the Learner's My VCBC Menu********")
        self.vcb.btnLearnerVCBC()
        self.logger.info("******** Click the VCBC pick********")  # Update the VCBC pick before execution
        self.vcb.learnerSchedule()
        self.logger.info("******** Click the VCBC Date Field********")
        self.vcb.fieldLearnerSlot()
        self.logger.info("******** Learner Selects Preferred Date********")
        self.vcb.learnerSlot1()                                 # Update the VCBC pick date before execution
        self.logger.info("******** Learner Clicks the Schedule Button********")
        self.vcb.learnerSlotSchedule()
        self.logger.info("******** Close the Browser********")
        self.elportal.delete_all_cookies()
        self.elportal.quit()
        self.logger.info("**********Learner VCBC Schedule Test is Successful********")








