import pytest
from Pages.cart_page import CartPage
from Pages.checkout_page import CheckoutPage
from Pages.inventory_page import InventoryPage
from Pages.login_page import LoginPage

@pytest.mark.checkout
def test_checkout_error_message_validation(page):
    login = LoginPage(page)
    inventory = InventoryPage(page)
    cart = CartPage(page)
    checkout = CheckoutPage(page)

    # login and add an item to the cart
    login.launch_application()
    login.login("standard_user", "secret_sauce")
    assert inventory.verify_product_pagetitle() == "Products"
    inventory.add_backpack_to_cart()
    inventory.open_cart()

    # proceed to checkout without filling in customer information
    cart.proceed_to_checkout()
    checkout.continue_checkout()

    # verify that the appropriate error message is displayed
    error_message = checkout.get_error_message()
    assert error_message == "Error: First Name is required"