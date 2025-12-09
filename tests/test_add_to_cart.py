import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage

@pytest.mark.regression
def test_add_to_cart(driver,login):
    """End-to-end test: login, add to cart, verify in cart.
    E2E (short) test:
    1. Login
    2. Add 'Sauce Labs Backpack' to cart
    3. Go to cart
    4. Verify backpack is present in the cart
    """

    #Products Page actions
    products_page = ProductsPage(driver)
    products_page.wait_until_loaded()
    products_page.add_backpack_to_cart()
    products_page.go_to_cart()

    #Carts Page validations
    cart_page = CartPage(driver)
    cart_page.wait_until_loaded()

    assert cart_page.is_backpack_in_cart(), "Add to cart test failed – Backpack not found in cart."