from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    """Page Object Model for the SauceDemo checkout flow."""

    def __init__(self, driver):
        self.driver = driver

        # Step One: Your Information
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.postal_code_input = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")

        # Step Two: Overview
        self.finish_button = (By.ID, "finish")

        # Complete page
        self.complete_header = (By.CLASS_NAME, "complete-header")

    def fill_customer_information(self, first_name :str, last_name :str, postal_code :str):
        """Fill in the checkout information form and click Continue."""
        wait = WebDriverWait(self.driver, 10)

        first_name_field = wait.until(
            EC.visibility_of_element_located(self.first_name_input)
        )
        last_name_field = self.driver.find_element(*self.last_name_input)
        postal_code_field = self.driver.find_element(*self.postal_code_input)
        continue_button = self.driver.find_element(*self.continue_button)

        first_name_field.clear()
        first_name_field.send_keys(first_name)

        last_name_field.clear()
        last_name_field.send_keys(last_name)

        postal_code_field.clear()
        postal_code_field.send_keys(postal_code)

        continue_button.click()

    def finish_checkout(self):
        """Click the Finish button on the overview page."""
        wait = WebDriverWait(self.driver, 10)
        finish_btn = wait.until(
            EC.element_to_be_clickable(self.finish_button)
        )
        finish_btn.click()

    def is_order_complete(self):
        """Check if the checkout is completed successfully.
        Return True if the 'Thank you for your order!' message is shown."""
        wait = WebDriverWait(self.driver, 10)
        try:
            header = wait.until(
                EC.visibility_of_element_located(self.complete_header)
            )
            return "Thank you for your order!" in header.text
        except Exception:
            return False

