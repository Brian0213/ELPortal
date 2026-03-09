import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.VCBCPage import VCBCPage
from testScripts.base_testL import BaseTestL
from testData.vcbc_students import VCBC_STUDENTS


class Test_Learner_Schedule_VCBC(BaseTestL):

    def test_schedule_10_learners(self, setup):
        driver = setup
        wait = WebDriverWait(driver, 10)

        self.login(driver)
        self.vcb = VCBCPage(driver)

        self.vcb.clickVCBCMgtL()
        # wait.until(EC.element_to_be_clickable(
        #     (By.XPATH, "//a[contains(@href,'vcbc')]"))
        # ).click()

        for learner in VCBC_STUDENTS:
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//button[@hx-get='/vcbc/28/schedule']"))
            ).click()

            driver.switch_to.default_content()

            wait.until(EC.invisibility_of_element_located(
                (By.XPATH, "//*[@role='alert']")
            ))

            wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//div[@class='ts-control']"))
            ).click()

            wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//div[contains(@id,'slot-opt') and not(contains(@class,'is-disabled'))]"))
            ).click()

            wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//button[@form='frmSchedule']"))
            ).click()

            # ❌ fail if backend rejects
            assert not driver.find_elements(
                By.XPATH, "//*[@role='alert' and contains(@class,'bg-red')]"
            ), f"Scheduling failed for {learner['email']}"

            # ✅ confirm success
            wait.until(EC.visibility_of_element_located(
                (By.XPATH, "//*[@role='alert' and contains(@class,'bg-green')]")
            ))

            self.logger.info(f"Scheduled {learner['email']} successfully")

        time.sleep(5)


















    # def test_schedule_multiple_learners(self, setup):
    #     self.elportal = setup
    #     self.login(self.elportal)
    #
    #     self.vcb = VCBCPage(self.elportal)
    #
    #     for learner in VCBC_STUDENTS:
    #         slot_id = learner.get("slot_id")
    #         assert slot_id, f"Missing slot_id in test data: {learner}"
    #
    #         self.vcb.clickVCBCMgtL()   # triggers HTMX load
    #         self.schedule_learner(slot_id)
    #
    # def schedule_learner(self, slot_id):
    #     d = self.elportal
    #     wait = WebDriverWait(d, 15)
    #
    #     d.switch_to.default_content()  # safe reset (no iframe switching)
    #
    #     # 🔑 wait for HTMX-rendered Schedule button
    #     schedule_btn = wait.until(
    #         EC.presence_of_element_located(
    #             (By.XPATH, "//button[@hx-get='/vcbc/27/schedule']")
    #         )
    #     )
    #     schedule_btn.click()
    #
    #     wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='ts-control']"))).click()
    #     wait.until(EC.element_to_be_clickable((By.ID, slot_id))).click()
    #     wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@form='frmSchedule']"))).click()
