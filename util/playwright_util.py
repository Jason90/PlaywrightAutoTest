from playwright.sync_api import sync_playwright
from util.log_util import log
import time

class PlaywrightUtil:
    def __init__(self):
        self.playwright = None
        self.browser = None
        self.page = None

    def initialize_browser(self, browser_type="chromium", headless=True):
        """Initialize Playwright browser instance"""
        log.logger.info(f"Initializing {browser_type} browser (headless: {headless})")
        self.playwright = sync_playwright().start()
        
        if browser_type == "chromium":
            self.browser = self.playwright.chromium.launch(headless=headless)
        elif browser_type == "firefox":
            self.browser = self.playwright.firefox.launch(headless=headless)
        elif browser_type == "webkit":
            self.browser = self.playwright.webkit.launch(headless=headless)
        else:
            raise ValueError(f"Unsupported browser type: {browser_type}")
            
        self.page = self.browser.new_page()
        return self.page

    def navigate_to(self, url):
        """Navigate to specified URL"""
        log.logger.info(f"Navigating to: {url}")
        self.page.goto(url, wait_until="networkidle")

    def click_element(self, selector, timeout=30000):
        """Click element by selector"""
        log.logger.info(f"Clicking element: {selector}")
        self.page.click(selector, timeout=timeout)

    def input_text(self, selector, text, timeout=30000):
        """Input text into element"""
        log.logger.info(f"Entering text '{text}' into: {selector}")
        self.page.fill(selector, text, timeout=timeout)

    def get_text(self, selector, timeout=30000):
        """Get text from element"""
        text = self.page.text_content(selector, timeout=timeout)
        log.logger.info(f"Extracted text from {selector}: {text}")
        return text

    def take_screenshot(self, path):
        """Take screenshot and save to path"""
        self.page.screenshot(path=path)
        log.logger.info(f"Screenshot saved to: {path}")

    def close_browser(self):
        """Clean up browser resources"""
        log.logger.info("Closing browser")
        if self.browser:
            self.browser.close()
        if self.playwright:
            self.playwright.stop()

# Singleton instance for utility usage
playwright_util = PlaywrightUtil()