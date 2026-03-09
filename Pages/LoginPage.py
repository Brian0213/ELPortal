from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class LoginPage:

    def __init__(self, elportal):
        self.elportal = elportal

    def emailAddress(self, emailaddress):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='username']"))).send_keys(emailaddress)

    def setPassword(self, setpassword):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='password']"))).send_keys(setpassword)


    def emailAddressL(self, emailaddressL):
        WebDriverWait(self.elportal, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='username']"))).send_keys(emailaddressL)

    def setPasswordL(self, setpasswordL):
        WebDriverWait(self.elportal, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='password']"))).send_keys(setpasswordL)

    def clickSignin(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()

    def clickHomeButton(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Click Here to Continue']"))).click()

    def semesterNav(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='button']//*[name()='svg']"))).click()

    def semesSpring(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Spring 2025')]"))).click()

    def semesFall(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Fall 2025')]"))).click()

    def semesSpring26(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Spring 2026')]"))).click()

    def semesSummer26(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Summer 2026')]"))).click()

    def clickDFC(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="sidebar"]/div[2]/div/ul/li[3]/a/div/div'))).click()

    def clickVCBCMgt(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="sidebar"]/div[2]/div/ul/li[4]/a/div/div'))).click()

    def stopImpersonate(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='stop']"))).click()

    def btnAdvanced(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='details-button']"))).click()

    def linkContinue(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@id='proceed-link']"))).click()

    def userMenuNav(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='flex items-center truncate']//*[name()='svg']"))).click()

    def buttonImpersonate(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Impersonate']"))).click()

    def buttonImpersonate(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Impersonate']"))).click()

    def emailImpersonate(self, emailimpersonate):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='email']"))).send_keys(emailimpersonate)

    def Impersonate(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@form='frmImpersonate']"))).click()

    def login(self, username, password):
        # Fill email/username
        self.elportal.until(EC.visibility_of_element_located((By.ID, "email"))).send_keys(username)
        # Fill password
        self.elportal.until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(password)
        # Click login
        self.elportal.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()

    def logout(self):
        # Optional: logout logic for learners
        self.elportal.until(EC.element_to_be_clickable((By.ID, "logoutButton"))).click()