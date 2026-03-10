import pytest
from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

class VCBCPage:

    MONTH_DROPDOWN = (By.CSS_SELECTOR, "select.flatpickr-monthDropdown-months")
    YEAR_INPUT = (By.CSS_SELECTOR, "input.numInput.cur-year")
    MONTH_OPTIONS = (By.CSS_SELECTOR, "option.flatpickr-monthDropdown-month")
    SLOT_DROPDOWN = (By.ID, "slot")
    SLOT_OPTIONS = (By.XPATH, "//select[@id='slot']/option")

    # Alternative locators
    MONTH_DROPDOWN_XPATH = (By.XPATH, "//select[@aria-label='Month']")

    def __init__(self, elportal):
        self.elportal = elportal
        self.wait = WebDriverWait(elportal, 5)

    def clickVCBCMgt(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='VCBC Management']"))).click()

    def clickVCBCMgtL(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='My VCBC']"))).click()

    def clickMyVCBC(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@hx-get='/vcbc/28/schedule']"))).click()

    def clickRoleAlert(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@role='alert']")))

    def btnSchedule(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='ts-control']"))).click()

    def pickSlot(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@id,'slot-opt') and not(contains(@class,'is-disabled'))]"))).click()

    def confirmSlot(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@form='frmSchedule']"))).click()

    def open_slot_dropdown(self):
        self.wait.until(EC.element_to_be_clickable(self.SLOT_DROPDOWN)).click()

    def get_all_slots(self):
        return self.wait.until(
            EC.presence_of_all_elements_located(self.SLOT_OPTIONS)
        )

    def select_slot_by_index(self, index):
        slots = self.get_all_slots()
        slots[index].click()

    def select_slot_by_visible_text(self, text):
        slots = self.get_all_slots()
        for slot in slots:
            if slot.text.strip() == text:
                slot.click()
                return
        raise Exception(f"Time slot '{text}' not found")

    def createVCBC(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Create VCBC']"))).click()

    def vcbcSessionName(self, sessionname):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='name']"))).send_keys(sessionname)

    def typeMakeup(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='makeup']"))).click()

    def typeRegular(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='regular']"))).click()

    def vcbcCourses(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="frmVCBCEditor"]/div[3]/div'))).click()

    def descriptionIframe(self):
        iframeext=WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//iframe[@class='rte-editable']")))
        self.elportal.switch_to.frame(iframeext)

    def enterDescription(self, description):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//body[@class='rte-toggleborder']"))).send_keys(description)

    def lookupCourse(self, coursepick):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="tomselect-6-ts-control"]'))).send_keys(coursepick)

    def pickCourseMakeDFC(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="tomselect-6-opt-3"]'))).click()

    def pickCourseReg1(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="tomselect-6-opt-1"]'))).click()

    def pickCourseReg2(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="tomselect-6-opt-2"]'))).click()

    def pickCourseReg3(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="tomselect-6-opt-2"]'))).click()

    def enterSlots(self, slot):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='slots']"))).clear()
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='slots']"))).send_keys(slot)

    def liveAt(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='sm:col-span-3 flex flex-col']//input[@type='text']"))).click()

    def liveAtJan(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'flatpickr-current-month')]//option[@value='0']"))).click()

    def liveAtFeb(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@class='flatpickr-monthDropdown-months']/option[@value='1']"))).click()

    def liveAtMar(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@class='flatpickr-monthDropdown-months']/option[@value='2']"))).click()

    def liveAtApr(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@class='flatpickr-monthDropdown-months']/option[@value='3']"))).click()

    def liveAtMay(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@class='flatpickr-monthDropdown-months']/option[@value='4']"))).click()

    def liveAtOct(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[6]/div[1]/div/div/select/option[@value='9']"))).click()

    def liveAtNov(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[6]/div[1]/div/div/select/option[@value='10']"))).click()

    def liveAtDec(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[6]/div[1]/div/div/select/option[@value='11']"))).click()


    def liveAtMonth(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='flatpickr-calendar hasTime animate open arrowBottom arrowLeft']//span[@class='flatpickr-current-month']"))).click()

    def liveMonth(self, month):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@aria-label='Month']"))).send_keys(month)

    def liveAtYear(self, year):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='flatpickr-calendar hasTime animate open arrowBottom arrowLeft']//input[@aria-label='Year']"))).clear()
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='flatpickr-calendar hasTime animate open arrowBottom arrowLeft']//input[@aria-label='Year']"))).send_keys(year)

    def liveAtDay(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='dayContainer']//span[@aria-label='September 15, 2025']"))).click()

    def closeAt(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[3]//input[2]"))).click()

    def closeAtYear(self, year):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='flatpickr-calendar hasTime animate open arrowBottom arrowLeft']//input[@aria-label='Year']"))).clear()
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='flatpickr-calendar hasTime animate open arrowBottom arrowLeft']//input[@aria-label='Year']"))).send_keys(year)

    def closeAtDay(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="dayContainer"]//span')))
        # WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='dayContainer']//span[@aria-label='September 20, 2025']")))

    def liveHour(self, livehour):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='numInputWrapper']//input[@class='numInput flatpickr-hour']"))).clear()
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='numInputWrapper']//input[@class='numInput flatpickr-hour']"))).send_keys(livehour)

    def liveMinute(self, liveminute):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='numInputWrapper']//input[@class='numInput flatpickr-minute']"))).clear()
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='numInputWrapper']//input[@class='numInput flatpickr-minute']"))).send_keys(liveminute)

    def closeHour(self, closehour):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//body/div[7]/div[3]/div[1]/input"))).clear()
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//body/div[7]/div[3]/div[1]/input"))).send_keys(closehour)

    def closeMinute(self, closeminute):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='numInputWrapper']//input[@class='numInput flatpickr-minute']"))).clear()
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='numInputWrapper']//input[@class='numInput flatpickr-minute']"))).send_keys(closeminute)

    def selLiveAM(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='flatpickr-calendar']//span[@title='Click to toggle'][normalize-space()='AM']"))).click()

    def selClosePM(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, '//body/div[6]/div[3]/span[2]'))).click()

    def closeAtMar(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[6]/div[1]/div/div/select/option[@value='2']"))).click()

    def closeAtOct(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[7]/div[1]/div/div/select/option[@value='9']"))).click()

    def closeAtNov(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[7]/div[1]/div/div/select/option[@value='11']"))).click()

    def closeAtDec(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[7]/div[1]/div/div/select/option[@value='12']"))).click()

    def closeAtJan(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[7]/div[1]/div/div/select/option[@value='1']"))).click()

    def closeAtFeb(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[7]/div[1]/div/div/select/option[@value='2']"))).click()

    def closeAtApr(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[7]/div[1]/div/div/select/option[@value='3']"))).click()

    def closeAtMay(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[7]/div[1]/div/div/select/option[@value='4']"))).click()

    def closeAtMonth(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='flatpickr-calendar hasTime animate open arrowBottom arrowLeft']//span[@class='flatpickr-next-month']"))).click()

    def dateField(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='w-full px-3']//input[@type='text']"))).click()

    def dateJan(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@class='flatpickr-monthDropdown-months']/option[@value='0']"))).click()

    def dateFeb(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@class='flatpickr-monthDropdown-months']/option[@value='1']"))).click()

    def dateMar(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@class='flatpickr-monthDropdown-months']/option[@value='2']"))).click()

    def dateApr(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@class='flatpickr-monthDropdown-months']/option[@value='3']"))).click()

    def dateMay(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@class='flatpickr-monthDropdown-months']option[@value='4']"))).click()

    def dateJun(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@class='flatpickr-monthDropdown-months']/option[@value='5']"))).click()

    def dateJul(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@class='flatpickr-monthDropdown-months']/option[@value='6']"))).click()

    def dateAug(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@class='flatpickr-monthDropdown-months']/option[@value='7']"))).click()

    def dateSep(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@class='flatpickr-monthDropdown-months']/option[@value='8']"))).click()

    def dateOct(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@class='flatpickr-monthDropdown-months']/option[@value='9']"))).click()

    def dateNov(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@class='flatpickr-monthDropdown-months']/option[@value='10']"))).click()

    def dateDec(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@class='flatpickr-monthDropdown-months']/option[@value='11']"))).click()

    def dateYear(self, year):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='numInputWrapper']//input[@aria-label='Year']"))).clear()
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='numInputWrapper']//input[@aria-label='Year']"))).send_keys(year)

    def date1(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//body/div[7]/div[2]/div/div[2]/div/span[6]"))).click()

    def date5(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//body/div[7]/div[2]/div/div[2]/div/span[8]"))).click()

    def date10(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//body/div[7]/div[2]/div/div[2]/div/span[13]"))).click()

    def date15(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//body/div[7]/div[2]/div/div[2]/div/span[18]"))).click()

    def date20(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//body/div[7]/div[2]/div/div[2]/div/span[23]"))).click()

    def date25(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//body/div[7]/div[2]/div/div[2]/div/span[28]"))).click()

    def date30(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//body/div[7]/div[2]/div/div[2]/div/span[33]"))).click()

    def date31(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//body/div[7]/div[2]/div/div[2]/div/span[34]"))).click()

    def vcbcSaveChanges(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//body/div[4]/div[2]/div/mactions/div/button[2]"))).click()

    def publishtoFaculty(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Publish to Faculty']"))).click()

    def vcbcPubSuccess(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Close']"))).click()

    def regularVCBC(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//tbody/tr[20]/td[6]/a[1]/span[1]"))).click()

    def makeUpVCBC(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//tbody/tr[19]/td[6]/a[1]/span[1]"))).click()

    def tabMakeUp(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Make Up']"))).click()

    def tabRegular(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Regular']"))).click()

    def allocateSlotBtn(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Assign Slots']"))).click()

    def selFaculty(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='faculty_id']"))).click()

    def facultyMs(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='faculty_id']/option[@value='51']"))).click()

    def facultyProfFadel(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='faculty_id']/option[@value='16']"))).click()

    def facultyQueenBartell(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='faculty_id']/option[@value='29']"))).click()

    def allocateButton(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@form='frmAllocateSlot']"))).click()

    def allocateSlots(self, slot):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='slots']"))).clear()
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='slots']"))).send_keys(slot)

    def btnVcbcSlot1(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Slot #1']"))).click()

    def btnVcbcSlot2(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Slot #2']"))).click()

    def btnAddLearner(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Add Learner']"))).click()

    def btnFormAddLearner(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@form='frmAddLearner']"))).click()

    def btnCancelAddLearner(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Cancel']"))).click()

    def fieldLearnerEmail(self, email):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='enter learner email address']"))).send_keys(email)

    def btnUser(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Auto Admin']"))).click()

    def btnImpersonate(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Impersonate']"))).click()

    def fieldImpersonateFaculty(self, faculty):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='email']"))).send_keys(faculty)

    def fieldImpersonateLearner(self, learner):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='email']"))).send_keys(learner)

    def btnConfirmImpersonate(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Impersonate']"))).click()

    def impersonateMyDFC(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="sidebar"]/div[2]/div/ul/li[2]/a'))).click()

    def impersonateMyVCBC(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="sidebar"]/div[2]/div/ul/li[3]/a/div/div'))).click()

    def impersonateMyCollegeCompliance(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="sidebar"]/div[2]/div/ul/li[4]/a'))).click()

    def impersonateMyPracticums(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="sidebar"]/div[2]/div/ul/li[5]/a'))).click()

    def vcbcViewButton(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, '//tbody/tr[4]/td[5]/a[1]/span[1]'))).click()

    def btnScheduleDate(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@x-model='sdate']/option[@value='2025-11-10']"))).click()

    def btnScheduleTime(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@x-model='stime']/option[@value='11:15']"))).click()

    def btnSchedule(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Schedule']"))).click()

    def btnRelease(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Release']"))).click()

    def btnStop(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='stop']"))).click()

    def selectVCBC(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//tbody/tr[5]/td[6]/a[1]/span[1]"))).click()

    def btnEditVcbc(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Edit']"))).click()

    def fromVCBCEditor(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="frmVCBCEditor"]/div[6]/div[3]/input[2]'))).click()

    def btnLearnerVCBC(self):
        try:
        # Wait for page to fully load after login
        WebDriverWait(self.elportal, 20).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )
        WebDriverWait(self.elportal, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='My VCBC']"))
        ).click()
    except TimeoutException:
        print(f"\n[DEBUG] URL after login: {self.elportal.current_url}")
        print(f"[DEBUG] Page title: {self.elportal.title}")
        # Dump all visible span and a tag texts to find the real element
        spans = self.elportal.find_elements(By.TAG_NAME, "span")
        print(f"[DEBUG] All spans: {[s.text.strip() for s in spans if s.text.strip()]}")
        links = self.elportal.find_elements(By.TAG_NAME, "a")
        print(f"[DEBUG] All links: {[l.text.strip() for l in links if l.text.strip()]}")
        raise
        # WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='My VCBC']"))).click()

    def learnerSchedule(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@hx-get='/vcbc/31/schedule']"))).click()

    def learnerReSchedule(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@hx-get='/vcbc/40/schedule?old_slot=3675']"))).click()

    def fieldLearnerSlot(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='ts-control']"))).click()

    def learnerSlot1(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='slot-opt-1']"))).click()

    def learnerSlot2(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='slot-opt-2']"))).click()

    def learnerSlot3(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='slot-opt-3']"))).click()

    def learnerSlotSchedule(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@form='frmSchedule']"))).click()

    def learnerSlotReSchedule(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@form='frmSchedule']"))).click()

    def learnerSlotCancel(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Cancel']"))).click()

    def pickDate(self, driver, date_value):
        alldates = driver.find_elements(By.XPATH, '//div[@class="dayContainer"]//span')
        for datepick in alldates:
            if datepick.text == date_value:
                datepick.click()
                break

    def pickMonth(self, driver, month_name):
        allmonths = driver.find_elements(
            By.XPATH,
            '//div[contains(@class,"flatpickr-current-month")]//option')
        for month in allmonths:
            if month.text == month_name:
                month.click()
                break

    def pickFebruary(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='flatpickr-calendar hasTime animate open arrowBottom arrowLeft']//option[@value='1'][normalize-space()='February']"))).click()

    def pickMarch(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='flatpickr-calendar hasTime animate open arrowBottom arrowLeft']//option[@value='2'][normalize-space()='March']"))).click()

    def pickApril(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='flatpickr-calendar hasTime animate open arrowBottom arrowLeft']//option[@value='3'][normalize-space()='April']"))).click()

    def pickMay(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='flatpickr-calendar hasTime animate open arrowBottom arrowLeft']//option[@value='4'][normalize-space()='May']"))).click()

    def pickJune(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='flatpickr-calendar hasTime animate open arrowBottom arrowLeft']//option[@value='4'][normalize-space()='June']"))).click()

    def pickJuly(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='flatpickr-calendar hasTime animate open arrowBottom arrowLeft']//option[@value='4'][normalize-space()='July']"))).click()

    def pickAugust(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='flatpickr-calendar hasTime animate open arrowBottom arrowLeft']//option[@value='4'][normalize-space()='August']"))).click()

    def pickSeptember(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='flatpickr-calendar hasTime animate open arrowBottom arrowLeft']//option[@value='4'][normalize-space()='September']"))).click()

    def pickOctober(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='flatpickr-calendar hasTime animate open arrowBottom arrowLeft']//option[@value='4'][normalize-space()='October']"))).click()

    def pickNovember(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='flatpickr-calendar hasTime animate open arrowBottom arrowLeft']//option[@value='4'][normalize-space()='November']"))).click()

    def pickDecember(self):
        WebDriverWait(self.elportal, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='flatpickr-calendar hasTime animate open arrowBottom arrowLeft']//option[@value='4'][normalize-space()='December']"))).click()

    def open_schedule_modal(self, vcbc_id="27"):
        self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//button[@hx-get='/vcbc/{vcbc_id}/schedule']")
            )
        ).click()

    # def test_select_date(self, driver):
    #     # Use the locator
    #     month_element = driver.find_element(*DatePickerLocators.MONTH_DROPDOWN)
    #     Select(month_element).select_by_visible_text("March")

    def select_slot_with_retry(self, slot_id, retries=3):
        for _ in range(retries):
            try:
                self.wait.until(EC.element_to_be_clickable(self.SLOT_CONTROL)).click()
                self.wait.until(EC.element_to_be_clickable((By.ID, slot_id))).click()
                return
            except StaleElementReferenceException:
                continue
        raise

    def select_slot(self, slot_id):
        """
        Selects a VCBC slot in a stale-safe way
        """

        # Always re-open dropdown (DOM refreshes after each schedule)
        self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[contains(@class,'ts-control')]")
            )
        ).click()

        # Select slot
        self.wait.until(
            EC.element_to_be_clickable(
                (By.ID, slot_id)
            )
        ).click()

    def submit_schedule(self):
        self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[@form='frmSchedule']")
            )
        ).click()

    def close_schedule_modal(self):
        self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//span[normalize-space()='Cancel']")
            )
        ).click()


    def select_slot(self, slot_number: int = 1):
        """Select a slot by number (default is 1)"""
        available_slots = self.wait.until(EC.presence_of_all_elements_located(
            (By.XPATH, "//div[contains(@id,'slot-opt') and not(contains(@class,'is-disabled'))]")
        ))
        if len(available_slots) < slot_number:
            pytest.fail(f"Requested slot {slot_number} not available. Only {len(available_slots)} slots found.")
        available_slots[slot_number - 1].click()
        
