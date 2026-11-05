import pytest
from Pages.cart_page import CartPage
from Pages.checkout_page import CheckoutPage
from Pages.inventory_page import InventoryPage
from Pages.login_page import LoginPage

@pytest.mark.checkout
def test_cart_remove_then_purchase_remaining_item(page):
    login = LoginPage(page)
    inventory = InventoryPage(page)
    cart = CartPage(page)
    checkout = CheckoutPage(page)

# login and add two items to the cart
    login.launch_application()
    login.login("standard_user", "secret_sauce")
    assert inventory .verify_product_pagetitle() == "Products"
    inventory.add_backpack_to_cart()
    inventory.add_bike_light_to_cart()
    inventory.open_cart()

#confirm both items are in the cart
    assert cart.get_product_names() == ["Sauce Labs Backpack", "Sauce Labs Bike Light"]

# remove the backpack from the cart and confirm only the bike light remains
    cart.remove_backpack_from_cart()
    assert cart.get_product_names() == ["Sauce Labs Bike Light"]

# proceed to check out and complete the purchase of the remaining item
    cart.proceed_to_checkout()
    checkout.fill_customer_information("Jane", "Doe", "12345")
    checkout.continue_checkout()
    checkout.finish_checkout()

# confirm the order confirmation message is displayed
    assert checkout.get_confirmation_message() == "Thank you for your order!"
