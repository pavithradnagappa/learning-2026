class LogOut:

    def __init__(self,page):
        self.page=page
        self.login_logo = ".login_logo"

#locators
    def Hamberger_menu(self):
        self.page.locator("#react-burger-menu-btn").click()

    def Logout(self):
        self.page.locator("#logout_sidebar_link").click()

    def verify_homepage(self):
        return self.page.locator(self.login_logo).text_content()