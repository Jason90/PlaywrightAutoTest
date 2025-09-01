from config import Web_Config
from core.page.base import BasePage
from playwright.sync_api import Page

class HomePage(BasePage):
    """Home page object"""
    
    # Locators
    # LOCATOR_LNK_LOGIN = "Client Login"


    def __init__(self, page:Page):
        super().__init__(page, Web_Config.WEB_BASE_URL) 
        self.__lnk_login=None
    
    @property
    def lnk_login(self):
        if self.__lnk_login==None:
            self.__lnk_login=self.page.locator("#menu-item-98557").get_by_role("link", name="Client Login")

        return self.__lnk_login
