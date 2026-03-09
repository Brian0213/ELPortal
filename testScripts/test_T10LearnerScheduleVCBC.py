import time
import sys

import pytest
from selenium.webdriver.common.by import By

from Pages.VCBCPage import VCBCPage
from Pages.LoginPage import LoginPage
from testScripts.base_testL import BaseTestL
from testData.vcbc_students import VCBC_STUDENTS



class Test_Learner_Schedule_VCBC(BaseTestL):


    def test_login(self, setup):
        self.elportal = setup
        self.login(self.elportal)
        self.logger.info("******** Verifying Regular VCBCs Creation********")
        self.logger.info("******** Define the Job Driver********")
        self.lpg = LoginPage(self.elportal)
        self.vcb = VCBCPage(self.elportal)
        self.logger.info("******** Click VCBC Management Menu ********")
        self.vcb.clickVCBCMgtL()
        self.elportal.find_element(By.XPATH, "//button[@hx-get='/vcbc/28/schedule']").click()
        self.logger.info("******** Switch back to the Create a DFC Rotation form********")
        self.elportal.switch_to.default_content()
        self.elportal.find_element(By.XPATH, "//div[@class='ts-control']").click()
        self.elportal.find_element(By.XPATH, "//div[@id='slot-opt-3']").click()
        self.elportal.find_element(By.XPATH, "//button[@form='frmSchedule']").click()
        # self.elportal.find_element(By.XPATH, "//span[normalize-space()='Cancel']").click()
        self.elportal.find_element(By.XPATH, "//div[@class='flex items-center truncate']//*[name()='svg']").click()
        self.elportal.find_element(By.XPATH, "//a[normalize-space()='Sign Out']").click()









