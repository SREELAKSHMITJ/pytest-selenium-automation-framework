from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    """Page Object Model for the SauceDemo login page."""

    def __init__(self, driver):
        """Store the driver and define locators for this page."""
        self.driver = driver
        self.url = "https://www.saucedemo.com/"

        # Locators as tuples
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.inventory_container = (By.ID, "inventory_container")

    def open(self):
        """Open the login page URL."""
        self.driver.get(self.url)

    def login(self, username_input :str, password_input:str):
        """Perform login using the given username and password."""
        wait = WebDriverWait(self.driver, 10)

        # Wait until username field is visible
        username_field = wait.until(
            EC.visibility_of_element_located(self.username_input)
        )

        # Find other fields (no need to wait again)
        password_field = self.driver.find_element(*self.password_input)
        login_btn = self.driver.find_element(*self.login_button)

        # Clear fields and type values
        username_field.clear()
        username_field.send_keys(username_input)

        password_field.clear()
        password_field.send_keys(password_input)


        # Click login
        login_btn.click()

    def is_logged_in(self) -> bool:
        """Return True if the products page is visible after login."""
        wait = WebDriverWait(self.driver, 10)
        try:
            wait.until(EC.url_contains("inventory.html"))
            wait.until(
                EC.visibility_of_element_located(self.inventory_container)
            )
            return True
        except Exception:
            return False

        #return "inventory.html" in self.driver.current_url