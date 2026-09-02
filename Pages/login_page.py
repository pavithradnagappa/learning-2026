from Pages.base_page import BasePage  #importing from base page
from config import BASE_URL

class LoginPage(BasePage):  #so class LoginPage will inherit all the methods n att from BasePage.its a child of BasePage class now.
    def __init__(self,page):
        # Call BasePage constructor
        super().__init__(page)

        #Locators
        self.username_txt= "#user-name"
        self.password_txt= "#password"
        self.login_btn= "#login-button"
        self.title= ".title"

#Launch application
    def launch_application(self):
        self.open_url(BASE_URL)    #from config.py, whre commonly used url etc kept

#enter username
    def enter_username(self,username):
        # Calls BasePage.fill()
        self.fill(self.username_txt, username)

    # enter password
    def enter_password(self,password):
        # Calls BasePage.fill()
        self.fill(self.password_txt, password)

# click login
    def click_login(self):
        # Calls BasePage.click()
        self.click(self.login_btn)

# Complete Login
    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

# verify title
    def verify_title(self):
        # Calls BasePage.get_text()
        return self.get_text(self.title)



