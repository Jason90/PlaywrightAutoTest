from core.page.base import BasePage
from playwright.sync_api import Page
from config import Web_Config

class LoginPage(BasePage):

    # LOCATOR_TXT_USERNAME = ".username"
    # LOCATOR_TXT_PASSWORD = ".password"
    # LOCATOR_BTN_LOGIN= ".proceed"
    # LOCATOR_LBL_MESSAGE= ".messageContainer"

    
    def __init__(self, page:Page):
        super().__init__(page, Web_Config.WEB_LOGIN_URL) 
        self.__txt_username=None
        self.__txt_password=None
        self.__btn_login=None
        self.__lbl_message=None
    
    @property
    def txt_username(self):
        if self.__txt_username is None:
            self.__txt_username=self.page.get_by_role("textbox", name="Username")
            
        return self.__txt_username
    
    @txt_username.setter
    def txt_username(self,value):
        self.txt_username.fill(value)

    @property
    def txt_password(self):
        if self.__txt_password is None:
            self.__txt_password=self.page.get_by_role("textbox", name="Password")
            
        return self.__txt_password
    
    @txt_password.setter
    def txt_password(self,value):
        self.txt_password.clear()
        self.txt_password.fill(value)
    
    @property
    def btn_login(self):
        if self.__btn_login is None:
            self.__btn_login=self.page.get_by_role("button", name="Sign in")
            
        return self.__btn_login 
    
    
    @property
    def lbl_message(self):
        if self.__lbl_message is None:
            self.__lbl_message=self.page.locator("#messageContainer")
            
        return self.__lbl_message 
