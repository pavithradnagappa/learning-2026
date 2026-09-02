
class InventoryPage:

    def __init__(self,page):
        self.page=page

#locators
        self.Product_title=".title"
        # self.backpack="#add-to-cart-sauce-labs-backpack"
        # self.cart=".shopping_cart_link"
#to verify product title
    def verify_product_pagetitle(self):
        return self.page.locator(self.Product_title).text_content()

#add backpack to cart
    def add_backpack_to_cart(self):
        self.page.locator("#add-to-cart-sauce-labs-backpack").click()
        self.page.wait_for_timeout(5000)


#open cart
    def open_cart(self):
        self.page.locator(".shopping_cart_badge").click()
        self.page.wait_for_timeout(5000)

