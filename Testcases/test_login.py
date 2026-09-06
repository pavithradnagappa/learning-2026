from Pages.login_page import LoginPage
from Pages.inventory_page import InventoryPage
from Pages.logout_page import LogOut
# from .test_data import LOGIN_DATA   # now reading same data from json file
import pytest
import json
from pathlib import Path

with (Path(__file__).parent / "test_data.json").open(encoding="utf-8") as file:
    LOGIN_DATA = json.load(file)

@pytest.mark.smoke
@pytest.mark.login
@pytest.mark.parametrize(
    "username, password, expected_result",
    [
        (
            data["username"],
            data["password"],
            data["expected_result"]
        )
        for data in LOGIN_DATA
    ]
)

def test_valid_login(page,username,password,expected_result):

#creating object for LoginPage and inventory etc..(for the Pages classes)
    login=LoginPage(page)
    # inventory=InventoryPage(page)
    logout=LogOut(page)

#launch website
    login.launch_application()

#login
    login.login(username, password)

    # inventory.add_backpack_to_cart()
    # inventory.open_cart()

#validation
    # assert inventory.verify_product_pagetitle()=="Your Cart"

#logout
    logout.Hamberger_menu()
    logout.Logout()

    assert logout.verify_homepage()== expected_result



