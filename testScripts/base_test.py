import time
from Pages.LoginPage import LoginPage
from utility.readProperties import ReadConfig
from utility.customLogger import LogGen

class BaseTest:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def login(self, elportal):
        self.logger.info("****** Starting login ******")
        elportal.implicitly_wait(10)
        self.logger.info("******** Launch the Application URL********")
        elportal.get(self.baseURL)
        login_page = LoginPage(elportal)
        self.logger.info("******** Click the Home Button********")
        login_page.clickHomeButton()
        self.logger.info("****** Fill the the Username******")
        login_page.emailAddress(self.username)
        self.logger.info("******Fill the the Password ******")
        login_page.setPassword(self.password)
        self.logger.info("******** Click the Signin Button********")
        login_page.clickSignin()
        time.sleep(2)
        self.logger.info("****** Login successful ******")


























# import time
# from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
#
# from Pages.LoginPage import LoginPage
# from utility.readProperties import ReadConfig
# from utility.customLogger import LogGen
#
#
# class BaseTest:
#     baseURL = ReadConfig.getApplicationURL()
#     username = ReadConfig.getUseremail()
#     password = ReadConfig.getPassword()
#     logger = LogGen.loggen()
#
#     def login(self, elportal, timestamp=None):
#         """Performs a robust login with retries, explicit waits, and screenshot capture on failure."""
#         self.logger.info("****** Starting Login ******")
#         elportal.get(self.baseURL)
#         elportal.maximize_window()
#         wait = WebDriverWait(elportal, 30)
#
#         login_page = LoginPage(elportal)
#
#         try:
#             self.logger.info("******** Clicking Home Button ********")
#             login_page.clickHomeButton()
#
#             self.logger.info("******** Entering Credentials ********")
#             # wait.until(EC.visibility_of_element_located((By.ID, "email")))
#
#             login_page.emailAddress(self.username)
#             login_page.setPassword(self.password)
#
#             self.logger.info("******** Clicking Sign In ********")
#             login_page.clickSignin()
#
#             # Wait for Dashboard to confirm successful login
#             self.logger.info("****** Waiting for Dashboard ******")
#             wait.until(
#                 EC.any_of(
#                     EC.presence_of_element_located((By.XPATH, "//h1[contains(., 'Dashboard')]")),
#                     EC.url_contains("dashboard")
#                 )
#             )
#             self.logger.info("****** Login Successful ******")
#
#         except TimeoutException:
#             self.logger.error("❌ Login failed: Timeout waiting for login elements or dashboard to load.")
#             timestamp = time.strftime("%Y%m%d-%H%M%S")
#             elportal.save_screenshot(f"screenshots/login_timeout_{timestamp}.png")
#             raise
#
#         except StaleElementReferenceException:
#             self.logger.warning("⚠️ StaleElementReference encountered. Retrying once...")
#             time.sleep(2)
#             try:
#                 login_page.clickSignin()
#                 wait.until(EC.url_contains("dashboard"))
#                 self.logger.info("****** Login Successful After Retry ******")
#             except Exception as e:
#                 self.logger.error(f"❌ Login failed after retry: {e}")
#                 elportal.save_screenshot(f"screenshots/login_stale_{timestamp}.png")
#                 raise
#
#         except Exception as e:
#             self.logger.error(f"❌ Unexpected error during login: {e}")
#             timestamp = time.strftime("%Y%m%d-%H%M%S")
#             elportal.save_screenshot(f"screenshots/login_exception_{timestamp}.png")
#             raise

