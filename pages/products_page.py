from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductsPage:
    """Page Object Model for the SauceDemo products page."""

    def __init__(self, driver):
        self.driver = driver

        # Locators
        # "Add to cart" button for Sauce Labs Backpack
        self.backpack_add_button = (By.ID, "add-to-cart-sauce-labs-backpack")

        # Shopping cart icon (top right)
        self.cart_icon = (By.CLASS_NAME, "shopping_cart_link")

        # Simple locator to confirm products page is loaded
        self.inventory_container = (By.ID, "inventory_container")

    def wait_until_loaded(self):
        """Wait until the products grid is visible."""
        wait = WebDriverWait(self.driver, 10)
        wait.until(
            EC.visibility_of_element_located(self.inventory_container)
        )

    def add_backpack_to_cart(self):
        """Click the 'Add to cart' button for Sauce Labs Backpack."""
        wait = WebDriverWait(self.driver,10)

        add_button = wait.until(
            EC.element_to_be_clickable(self.backpack_add_button)
        )

        add_button.click()

    def go_to_cart(self):
        """Click the cart icon to open the cart page."""
        cart_link = self.driver.find_element(*self.cart_icon)
        cart_link.click()