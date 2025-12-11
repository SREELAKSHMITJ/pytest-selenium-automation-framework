import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def create_driver():
    """This function creates and returns a Chrome browser instance."""
    chrome_options = Options()

    # Start Chrome as guest (no saved passwords, no sync)
    chrome_options.add_argument("--guest")

    chrome_options.add_argument("--start-maximized")  # Opens the Chrome browser full screen
    chrome_options.add_argument("--disable-notifications") #This would disable all the notifications

    # Tell Chrome not to use password manager in this session
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
    }
    chrome_options.add_experimental_option("prefs", prefs)

    # CI = environment variable we will set in GitHub Actions
    if os.getenv("CI"):
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")


    #creating Chrome driver
    driver = webdriver.Chrome(options = chrome_options)
    driver.implicitly_wait(5)
    return driver

def quit_driver(driver):
    """This function closes the browser."""
    driver.quit()