import pytest

from Pages.cart_page import CartPage
from Pages.checkout_page import CheckoutPage
from Pages.inventory_page import InventoryPage
from Pages.login_page import LoginPage


@pytest.mark.smoke
@pytest.mark.checkout
def test_checkout_lowest_priced_product(page):
    login = LoginPage(page)
    inventory = InventoryPage(page)
    cart = CartPage(page)
    checkout = CheckoutPage(page)

    login.launch_application()
    login.login("standard_user", "secret_sauce")
    assert inventory.verify_product_pagetitle() == "Products"

    inventory.sort_by_price_low_to_high()
    product_prices = inventory.get_product_prices()
    assert product_prices == sorted(product_prices)
    product_name, product_price = inventory.add_lowest_priced_product_to_cart()
    assert product_price == min(product_prices)

    inventory.open_cart()
    assert cart.get_product_names() == [product_name]
    cart.proceed_to_checkout()
    checkout.fill_customer_information("Jane", "Doe", "12345")
    checkout.continue_checkout()
    checkout.finish_checkout()

    assert checkout.get_confirmation_message() == "Thank you for your order!"
