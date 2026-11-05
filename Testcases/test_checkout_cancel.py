import pytest

from Pages.cart_page import CartPage
from Pages.checkout_page import CheckoutPage
from Pages.inventory_page import InventoryPage
from Pages.login_page import LoginPage

def test_checkout_cancel(page):
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

    # proceed to checkout and fill in customer information
    cart.proceed_to_checkout()
    checkout.fill_customer_information("John", "Doe", "12345")

    # cancel the checkout process
    checkout.cancel_checkout()

    # verify that the user is redirected back to the cart page
    assert page.url == "https://www.saucedemo.com/cart.html"