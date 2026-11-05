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
def test_valid_login(page, username, password, expected_result):
    # FIX: valid and invalid login paths must be validated differently.
    login = LoginPage(page)
    inventory = InventoryPage(page)
    logout = LogOut(page)

    login.launch_application()
    login.login(username, password)

    if expected_result == "Success":
        # FIX: after valid login, check the inventory page instead of the login logo.
        assert inventory.verify_product_pagetitle() == "Products"
        logout.Hamberger_menu()
        logout.Logout()
        assert logout.verify_homepage() == "Swag Labs"
    else:
        # FIX: invalid login should not try to open the hamburger menu.
        error_message = page.locator("[data-test='error']")
        assert error_message.is_visible()
        assert "Username and password do not match any user in this service" in error_message.text_content()



