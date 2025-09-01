# from selenium import webdriver
from core.page.home import HomePage
from core.page.login import LoginPage
from playwright.sync_api import sync_playwright

class EBPortal():
    def __init__(self) -> None:
        # self.driver=webdriver.Chrome()
        # self.driver.maximize_window()
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=False)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()
        
        self.pg_home = HomePage(self.page)
        self.pg_login = LoginPage(self.page)
        
    def __del__(self):
        self.context.close()
        self.browser.close()
        self.playwright.stop()
        
    def login(self,user,password):
        self.pg_home.navigate()
        self.pg_home.lnk_login.click()
        
        self.pg_login.txt_username.text="Jason"
        self.pg_login.txt_password.text="password"
        self.pg_login.btn_login.click()