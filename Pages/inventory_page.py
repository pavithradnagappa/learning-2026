
class InventoryPage:

    def __init__(self,page):
        self.page=page

        self.Product_title=".title"

    def verify_product_pagetitle(self):
        return self.page.locator(self.Product_title).text_content()

    def add_backpack_to_cart(self):
        self.page.locator("#add-to-cart-sauce-labs-backpack").click()

    def sort_by_price_low_to_high(self):
        self.page.locator("[data-test='product-sort-container']").select_option("lohi")

    def get_product_prices(self):
        prices = self.page.locator(".inventory_item_price").all_text_contents()
        return [float(price.replace("$", "")) for price in prices]

    def add_lowest_priced_product_to_cart(self):
        lowest_product = self.page.locator(".inventory_item").first
        product_name = lowest_product.locator(".inventory_item_name").text_content()
        product_price = float(
            lowest_product.locator(".inventory_item_price").text_content().replace("$", "")
        )
        lowest_product.get_by_role("button", name="Add to cart").click()
        return product_name, product_price

    def open_cart(self):
        self.page.locator(".shopping_cart_link").click()
