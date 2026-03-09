# import os
# import subprocess
# import webbrowser
#
# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager
# from selenium.webdriver.chrome.options import Options
#
#
# @pytest.fixture()
# def setup(browser):
#     options = Options()
#     options.add_argument("--log-level=3")
#     options.add_argument("start-maximized")
#     options.add_argument("--disable-extensions")
#     options.add_argument("--disable-infobars")
#     options.add_argument("--disable-notifications")
#     options.add_argument("--disable-popup-blocking")
#     options.add_argument("--disable-gpu")
#     options.add_argument("--disable-dev-shm-usage")
#     options.add_experimental_option('excludeSwitches', ['enable-logging'])
#     # Uncomment this line for CI/headless runs:
#     # options.add_argument("--headless=new")
#
#     global elportal
#     if browser == 'chrome':
#         elportal = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
#     elif browser == 'firefox':
#         elportal = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
#     else:
#         raise ValueError("Unsupported browser! Use chrome or firefox.")
#
#     elportal.implicitly_wait(5)
#     yield elportal
#     elportal.quit()
#
#
# def pytest_addoption(parser):
#     """Allows passing browser type from CLI."""
#     parser.addoption("--browser", action="store", default="chrome",
#                      help="Browser to run tests with: chrome or firefox")
#
#
# @pytest.fixture()
# def browser(request):
#     return request.config.getoption("--browser")
#
#
# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     """Capture screenshot automatically on test failure."""
#     outcome = yield
#     rep = outcome.get_result()
#     if rep.failed:
#         driver = item.funcargs.get("setup", None)
#         if driver:
#             os.makedirs("screenshots", exist_ok=True)
#             filename = f"screenshots/{item.name}.png"
#             driver.save_screenshot(filename)


import os
import platform
import subprocess
import tempfile
import webbrowser
from pathlib import Path

from selenium import webdriver
import pytest
from pathlib import Path
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options



options = Options()
options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

@pytest.fixture()
def setup(browser):
    options = webdriver.ChromeOptions()
    options.add_argument("--log-level=3")
    options.add_argument("start-maximized")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--headless=new"")
    options.add_argument("--disable-dev-shm-usage")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    # THIS IS THE KEY LINE
    user_data_dir = tempfile.mkdtemp()
    options.add_argument(f"--user-data-dir={user_data_dir}")

    global elportal
    if browser == 'chrome':
        elportal= webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
    elif browser == 'firefox':
        elportal = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    elportal.implicitly_wait(10)
    return elportal


def pytest_addoption(parser):    # This will get the value from CLI/hooks
    parser.addoption("--browser",
                     action="store",
                     default="chrome",
                     help="Browser to run tests with: chrome or firefox")

@pytest.fixture()
def browser(request):    # This will return the Browser value to the setup method.
    return request.config.getoption("--browser")


def pytest_sessionfinish(session, exitstatus):
    """ Automatically open HTML report after test run """
    html_report_path = os.path.abspath("Reports/autorep.html")
    if os.path.exists(html_report_path):
        print(f"\nOpening test report: {html_report_path}")
        try:
            webbrowser.open(f"file://{html_report_path}")
        except Exception as e:
            print(f"Failed to open report automatically: {e}")
    else:
        print("Test report not found: Reports/autorep.html")


# def pytest_sessionfinish(session, exitstatus):
    """Auto-launch Allure report in browser after test run (macOS only, local only)"""

    # Run ONLY on macOS and NOT in CI
    if platform.system() != "Darwin" or os.environ.get("CI"):
        return

    allure_results_dir = os.path.abspath("allure-results")

    if not os.path.exists(allure_results_dir):
        print("Allure results directory not found. Did you run with --alluredir=allure-results?")
        return

    try:
        print(f"\nLaunching Allure report from: {allure_results_dir}")

        subprocess.Popen(
            ["allure", "serve", allure_results_dir],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            start_new_session=True
        )

    except Exception as e:
        print(f"Failed to serve Allure report: {e}")


#     """Auto-launch Allure report in browser after test run (pass or fail)"""
#     allure_results_dir = os.path.abspath("allure-results")
#
#     if os.path.exists(allure_results_dir):
#         try:
#             print(f"\nLaunching Allure report from: {allure_results_dir}")
#             subprocess.Popen(["allure", "serve", allure_results_dir], shell=True)
#         except Exception as e:
#             print(f"Failed to serve Allure report: {e}")
#     else:
#         print("Allure results directory not found. Did you run with --alluredir=allure-results?")




# import subprocess
# import webbrowser
# from pathlib import Path
#
# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager
#
#
# # =====================================================
# # PATH CONFIGURATION (Pathlib ONLY)
# # =====================================================
#
# BASE_DIR = Path(__file__).resolve().parent
#
# REPORTS_DIR = BASE_DIR / "reports"
# SCREENSHOTS_DIR = REPORTS_DIR / "screenshots"
# ALLURE_RESULTS_DIR = BASE_DIR / "allure-results"
#
# for directory in (REPORTS_DIR, SCREENSHOTS_DIR, ALLURE_RESULTS_DIR):
#     directory.mkdir(parents=True, exist_ok=True)
#
#
# @pytest.fixture(scope="session")
# def paths():
#     """Shared project paths"""
#     return {
#         "base": BASE_DIR,
#         "reports": REPORTS_DIR,
#         "screenshots": SCREENSHOTS_DIR,
#         "allure": ALLURE_RESULTS_DIR
#     }
#
#
# # =====================================================
# # PYTEST CLI OPTIONS
# # =====================================================
#
# def pytest_addoption(parser):
#     parser.addoption(
#         "--browser",
#         action="store",
#         default="chrome",
#         help="Browser to run tests with: chrome or firefox"
#     )
#
#
# @pytest.fixture
# def browser(request):
#     return request.config.getoption("--browser")
#
#
# # =====================================================
# # WEBDRIVER FIXTURE
# # =====================================================
#
# @pytest.fixture
# def setup(browser):
#     options = Options()
#     options.add_argument("--log-level=3")
#     options.add_argument("--start-maximized")
#     options.add_argument("--disable-notifications")
#     options.add_argument("--disable-gpu")
#     options.add_experimental_option("excludeSwitches", ["enable-logging"])
#
#     if browser == "chrome":
#         driver = webdriver.Chrome(
#             service=Service(ChromeDriverManager().install()),
#             options=options
#         )
#     elif browser == "firefox":
#         driver = webdriver.Firefox(
#             service=Service(GeckoDriverManager().install())
#         )
#     else:
#         raise ValueError(f"Unsupported browser: {browser}")
#
#     yield driver
#     driver.quit()
#
#
# # =====================================================
# # SESSION FINISH HOOK (REPORTS)
# # =====================================================
#
# def pytest_sessionfinish(session, exitstatus):
#     """Auto-open HTML report and serve Allure report after execution"""
#
#     # ---------- HTML REPORT ----------
#     html_report = REPORTS_DIR / "autorep.html"
#     if html_report.exists():
#         try:
#             webbrowser.open(html_report.as_uri())
#         except Exception as e:
#             print(f"Failed to open HTML report: {e}")
#
#     # ---------- ALLURE REPORT ----------
#     if ALLURE_RESULTS_DIR.exists() and any(ALLURE_RESULTS_DIR.iterdir()):
#         try:
#             subprocess.Popen(
#                 ["allure", "serve", str(ALLURE_RESULTS_DIR)],
#                 shell=False
#             )
#         except Exception as e:
#             print(f"Failed to serve Allure report: {e}")
#     else:
#         print("Allure results directory is empty or missing.")






# def pytest_addoption(parser):
#     parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests with")


