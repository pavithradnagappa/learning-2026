class CartPage:
    def __init__(self, page):
        self.page = page

    def get_product_names(self):
        return self.page.locator(".inventory_item_name").all_text_contents()

    def proceed_to_checkout(self):
        self.page.get_by_role("button", name="Checkout").click()
