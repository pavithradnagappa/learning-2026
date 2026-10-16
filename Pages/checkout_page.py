class CheckoutPage:
    def __init__(self, page):
        self.page = page

    def fill_customer_information(self, first_name, last_name, postal_code):
        self.page.locator("#first-name").fill(first_name)
        self.page.locator("#last-name").fill(last_name)
        self.page.locator("#postal-code").fill(postal_code)

    def continue_checkout(self):
        self.page.get_by_role("button", name="Continue").click()

    def finish_checkout(self):
        self.page.get_by_role("button", name="Finish").click()

    def get_confirmation_message(self):
        return self.page.locator(".complete-header").text_content()
