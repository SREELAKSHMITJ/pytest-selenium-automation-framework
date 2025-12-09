import os
import sys
import pytest

# Add the project root directory to sys.path
# so that 'utils' and 'pages' can be imported.
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

from utils.driver_setup import create_driver,quit_driver
from pages.login_page import LoginPage

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

@pytest.fixture
def driver(request):
    """Pytest fixture to open and clean up the WebDriver"""

    #Open a fresh page in the browser
    driver  = create_driver()

    #Give the driver to the test
    yield driver

    rep_call = getattr(request.node, "rep_call", None)

    if rep_call and rep_call.failed:
        screenshots_dir = os.path.join(PROJECT_ROOT, "screenshots")
        os.makedirs(screenshots_dir, exist_ok=True)

        test_name = request.node.name
        screenshot_path = os.path.join(screenshots_dir, f"{test_name}.png")

        driver.save_screenshot(screenshot_path)
        print(f"\n[SCREENSHOT] Saved failure screenshot to: {screenshot_path}")

    #close the browser
    quit_driver(driver)

@pytest.fixture
def login(driver):
    """Reusable fixture to perform login."""
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    assert login_page.is_logged_in(), "Login failed – cannot continue to add to cart test."
    return login_page


