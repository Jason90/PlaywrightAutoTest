from playwright.sync_api import Page

from util.log_util import log

class BasePage:
    
    def __init__(self, page: Page, url):
        self.page = page
        self.url = url
        self._element_cache = {}
    
    def navigate(self,url):
        self.page.goto(url)
    
    def navigate(self):
        self.page.goto(self.url)
        
    #todo: cache element by url+locator
    def find_element(self, locator) :
        if locator not in self._element_cache:
            self._element_cache[locator] = self.page.locator(locator)
        return self._element_cache[locator]