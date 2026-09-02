
class BasePage:

    def __init__(self,page):
        # Store Playwright page object
        self.page=page

    def click(self,locator):

        # Whatever locator we pass,click on that element.
        self.page.locator(locator).click()


    def fill(self,locator,value):
        # Whatever locator we pass,enter the given text
        self.page.locator(locator).fill(value)

    def get_text(self,locator):
        # return the text present in given locator
        return self.page.locator(locator).text_content()

    # Instead of writing page.goto we can create method
    def open_url(self, url):
        self.page.goto(url)

    # Take Screenshot
    def take_screenshot(self, path):
        self.page.screenshot(path=path)

    # Hover
    def hover(self, locator):
        self.page.locator(locator).hover()

    # Scroll
    def scroll_into_view(self, locator):
        self.page.locator(locator).scroll_into_view_if_needed()
