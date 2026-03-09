import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait

from Pages.LoginPage import LoginPage
from Pages.VCBCPage import VCBCPage
from testData.vcbc_learners import VCBC_STUDENTS
from utility.readProperties import ReadConfig


class Test_Login_ElPortal():

    baseURL = ReadConfig.getApplicationURL()

    @pytest.mark.parametrize("learner", VCBC_STUDENTS)
    def test_schedule_single_learner(self, setup, learner):
        self.elportal = setup
        self.elportal.get(self.baseURL)
        self.elp = LoginPage(self.elportal)
        self.vcp = VCBCPage(self.elportal)
        windowsIDs = self.elportal.window_handles
        parentwindowid = windowsIDs[0]
        self.elp.clickHomeButton()


        self.elp.emailAddress(learner["email"])
        self.elp.setPassword(learner["password"])

        self.elp.clickSignin()

        self.vcp.clickVCBCMgtL()
        self.vcp.clickMyVCBC()
        # slots=self.vcp.open_slot_dropdown()
        #
        # for index in range(len(slots)):
        #     self.vcp.open_slot_dropdown()
        #     self.vcp.select_slot_by_index(index)

        # self.vcp.clickRoleAlert()
        # Select a time slot

        # self.vcp.btnSchedule()
        # self.logger.info("********Switch to the Create VCBCs Form********")
        self.vcp.learnerSchedule()
        self.vcp.fieldLearnerSlot()
        self.vcp.learnerSlot2()
        self.vcp.learnerSlotSchedule()
        # self.elportal.find_element(By.XPATH, "//div[@class='ts-control']").click()
        # self.elportal.find_element(
        #     (By.XPATH, "//div[contains(@id,'slot-opt') and not(contains(@class,'is-disabled'))]")
        # ).click()
        # self.vcp.pickSlot()
        # self.elportal.find_element(By.XPATH, "//div[@class='ts-control']").click()
        # self.elportal.find_element(By.XPATH, "//div[contains(@id,'slot-opt') and not(contains(@class,'is-disabled'))]").click()
        # self.vcp.confirmSlot()

        # Fail test if backend rejects
        assert not self.elportal.find_elements(
            By.XPATH, "//*[@role='alert' and contains(@class,'bg-red')]"
        ), f"Scheduling failed for {learner['email']}"

        # Reset session
        self.elportal.delete_all_cookies()

