from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    """Page Object Model for the SauceDemo cart page."""

    def __init__(self, driver):
        self.driver = driver

        #Cart Page container
        self.cart_items_container = (By.CLASS_NAME, "cart_list")

        # Product names inside cart
        self.backpack_item_name = (By.CLASS_NAME, "inventory_item_name")

        # Checkout button
        self.checkout_button = (By.ID, "checkout")

    def wait_until_loaded(self):
        """Wait until the cart list is visible."""
        wait = WebDriverWait(self.driver, 10)

        wait.until(
            EC.visibility_of_element_located(self.cart_items_container)
        )

    def is_backpack_in_cart(self) -> bool:
        """Return True if 'Sauce Labs Backpack' appears in the cart."""
        wait = WebDriverWait(self.driver, 10)

        try:
            elements = wait.until(
                EC.presence_of_all_elements_located(self.backpack_item_name)
            )

            for el in elements:
                if "Sauce Labs Backpack" in el.text:
                    return True
            return False

        except Exception:
            return False

    def click_checkout(self):
        """Click the Checkout button on the cart page."""
        wait = WebDriverWait(self.driver, 10)
        btn = wait.until(
            EC.element_to_be_clickable(self.checkout_button)
        )
        btn.click()