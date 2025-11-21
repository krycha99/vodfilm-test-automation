from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

class BasePage:

    DECLINE_COOKIE_BUTTON = (By.XPATH, "//button[contains(text(), 'Nie zgadzam się')]")

    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(driver, timeout)

    def find(self, locator):
        return self.driver.find_element(*locator)
    
    def find_all(self, locator):
        return self.driver.find_elements(*locator)

    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
    
    def enter_text(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text
    
    def wait_for_visible(self, locator, timeout=None):
        wait_time = timeout if timeout else self.timeout
        return WebDriverWait(self.driver, wait_time).until(EC.visibility_of_element_located(locator))
    
    def close_cookie_popup(self):
        try:
            popup = self.wait.until(EC.element_to_be_clickable(self.DECLINE_COOKIE_BUTTON))
            popup.click()
        except TimeoutException:
            pass

    
