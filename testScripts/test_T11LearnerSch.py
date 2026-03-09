from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

from Pages.VCBCPage import VCBCPage
from Pages.LoginPage import LoginPage
from testScripts.base_testL import BaseTestL
from testData.vcbc_students import VCBC_STUDENTS


class Test_Learner_Schedule_VCBC():

    def close_any_open_modals(self):
        """Close any open modal dialogs before proceeding"""
        try:
            # Try multiple strategies to close modals
            close_selectors = [
                "//span[normalize-space()='Cancel']",
                "//button[contains(@class, 'close') or contains(@aria-label, 'Close')]",
                "//div[@role='dialog']//button[contains(., 'Close')]",
                "//div[@role='dialog']//span[contains(., '×')]",
                "//button[@data-dismiss='modal']",
            ]

            for selector in close_selectors:
                try:
                    close_button = WebDriverWait(self.elportal, 2).until(
                        EC.element_to_be_clickable((By.XPATH, selector))
                    )
                    close_button.click()
                    self.logger.info(f"Closed modal using: {selector}")
                    time.sleep(0.5)
                    return True
                except TimeoutException:
                    continue

            # If no close button found, try clicking outside modal (on backdrop)
            try:
                backdrop = self.elportal.find_element(By.XPATH,
                                                      "//div[@class='fixed inset-0' and contains(@class, 'z-50')]")
                self.elportal.execute_script("arguments[0].click();", backdrop)
                self.logger.info("Closed modal by clicking backdrop")
                time.sleep(0.5)
                return True
            except:
                pass

            # Try pressing ESC key
            from selenium.webdriver.common.keys import Keys
            try:
                self.elportal.find_element(By.TAG_NAME, 'body').send_keys(Keys.ESCAPE)
                self.logger.info("Closed modal with ESC key")
                time.sleep(0.5)
                return True
            except:
                pass

        except Exception as e:
            self.logger.debug(f"No modal to close or error: {str(e)}")

        return False

    def schedule_learner_to_vcbc(self, vcbc_id, learner_data):
        """
        Schedule a single learner to a specific VCBC

        Args:
            vcbc_id: The VCBC ID (e.g., 27)
            learner_data: Dictionary with 'email' and 'slot_id'
        """
        try:
            learner_email = learner_data.get('email')
            slot_id = learner_data.get('slot_id', 'slot-opt-3')

            self.logger.info(f"******** Scheduling {learner_email} to VCBC {vcbc_id} ********")

            # Make sure any previous modal is closed
            self.close_any_open_modals()
            time.sleep(0.5)

            # Wait for the page to be ready and modal to be fully closed
            WebDriverWait(self.elportal, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@role='dialog']"))
            )

            # Click the schedule button for the VCBC
            schedule_button = WebDriverWait(self.elportal, 10).until(
                EC.element_to_be_clickable((By.XPATH, f"//button[@hx-get='/vcbc/{vcbc_id}/schedule']"))
            )

            # Scroll to button to ensure it's in view
            self.elportal.execute_script("arguments[0].scrollIntoView({block: 'center'});", schedule_button)
            time.sleep(0.5)

            # Use JavaScript click to avoid interception
            self.elportal.execute_script("arguments[0].click();", schedule_button)
            self.logger.info(f"Clicked schedule button for VCBC {vcbc_id}")

            # Wait for the modal to appear
            WebDriverWait(self.elportal, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[@role='dialog']"))
            )
            time.sleep(0.5)

            # Switch back to default content (if in iframe)
            self.elportal.switch_to.default_content()

            # Select the slot
            slot_control = WebDriverWait(self.elportal, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@class='ts-control']"))
            )
            slot_control.click()
            self.logger.info("Opened slot dropdown")
            time.sleep(0.3)

            slot_option = WebDriverWait(self.elportal, 10).until(
                EC.element_to_be_clickable((By.XPATH, f"//div[@id='{slot_id}']"))
            )
            slot_option.click()
            self.logger.info(f"Selected slot: {slot_id}")
            time.sleep(0.3)

            # Submit the form
            submit_button = WebDriverWait(self.elportal, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@form='frmSchedule']"))
            )
            submit_button.click()
            self.logger.info("Clicked submit button")

            # Wait for submission to complete
            time.sleep(2)

            # Close the modal/confirmation
            modal_closed = self.close_any_open_modals()

            if not modal_closed:
                # Force close by waiting for modal to disappear
                try:
                    WebDriverWait(self.elportal, 5).until(
                        EC.invisibility_of_element_located((By.XPATH, "//div[@role='dialog']"))
                    )
                    self.logger.info("Modal auto-closed")
                except TimeoutException:
                    self.logger.warning("Modal did not close automatically")

            # Extra wait to ensure everything is settled
            time.sleep(1)

            self.logger.info(f"******** Successfully scheduled {learner_email} to VCBC {vcbc_id} ********")
            return True

        except Exception as e:
            self.logger.error(f"******** Failed to schedule {learner_email} - {str(e)} ********")
            try:
                self.elportal.save_screenshot(f"failed_{learner_email.split('@')[0]}.png")
            except:
                pass

            # Try to recover by closing any modal
            self.close_any_open_modals()
            return False

    def test_schedule_multiple_learners(self, setup):
        """Main test to schedule multiple learners to a VCBC"""
        self.elportal = setup
        self.login(self.elportal)
        self.logger.info("******** Starting VCBC Scheduling for Multiple Learners ********")

        self.lpg = LoginPage(self.elportal)
        self.vcb = VCBCPage(self.elportal)

        self.logger.info("******** Click VCBC Management Menu ********")
        self.vcb.clickVCBCMgtL()
        time.sleep(2)

        # Define which VCBC to schedule learners to
        VCBC_ID = 27  # Change this to the appropriate VCBC ID

        # Make sure we start with a clean state
        self.close_any_open_modals()

        # Schedule all learners
        successful_schedules = []
        failed_schedules = []

        for index, learner in enumerate(VCBC_STUDENTS, 1):
            self.logger.info(f"******** Processing learner {index}/{len(VCBC_STUDENTS)} ********")

            if self.schedule_learner_to_vcbc(VCBC_ID, learner):
                successful_schedules.append(learner['email'])
            else:
                failed_schedules.append(learner['email'])

            # Delay between learners to avoid race conditions
            time.sleep(1)

        # Summary
        self.logger.info("=" * 60)
        self.logger.info(f"******** Scheduling Complete ********")
        self.logger.info(f"VCBC ID: {VCBC_ID}")
        self.logger.info(
            f"Total: {len(VCBC_STUDENTS)} | Success: {len(successful_schedules)} | Failed: {len(failed_schedules)}")

        if successful_schedules:
            self.logger.info(f"Successful: {', '.join(successful_schedules)}")

        if failed_schedules:
            self.logger.error(f"Failed: {', '.join(failed_schedules)}")

        self.logger.info("=" * 60)

        assert len(failed_schedules) == 0, f"{len(failed_schedules)} learner(s) failed to schedule"