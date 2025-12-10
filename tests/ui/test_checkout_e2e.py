import pytest
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.products_page import ProductsPage
from pages.checkout_page import CheckoutPage

@pytest.mark.e2e
@pytest.mark.regression
def test_checkout_e2e_success(driver, login):
    """
        Full E2E flow:
        1. Login with valid user
        2. Add 'Sauce Labs Backpack' to cart
        3. Go to cart and verify item
        4. Proceed to checkout
        5. Fill customer details
        6. Finish checkout
        7. Verify 'Thank you for your order!' message
    """

    # Products Page actions
    products_page = ProductsPage(driver)
    products_page.wait_until_loaded()
    products_page.add_backpack_to_cart()
    products_page.go_to_cart()

    # Carts Page validations
    cart_page = CartPage(driver)
    cart_page.wait_until_loaded()

    assert cart_page.is_backpack_in_cart(), "Add to cart test failed – Backpack not found in cart."
    cart_page.click_checkout()

    #Checkout: fill information and complete
    checkout_page = CheckoutPage(driver)
    checkout_page.fill_customer_information("Sree", "TJ", "N2G0C9")
    checkout_page.finish_checkout()

    #Checkout: verifying order completion
    assert checkout_page.is_order_complete(), "E2E checkout test failed – order not completed."
