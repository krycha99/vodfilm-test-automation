from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException

class SearchResultsPage(BasePage):

    RESULT_ITEMS = (By.CSS_SELECTOR, "article[class*='ProductionCard']")
    RESULT_TITLES = (By.CSS_SELECTOR, "#search-results .production__Title-sc-77f87755-7")
    FIRST_RESULT = (By.CSS_SELECTOR, "div.search__ResultsContainer-sc-87cf44fc-7 article.production__ProductionCard-sc-77f87755-0 p.production__Title-sc-77f87755-7 a")
    RESULTS_CONTAINER = (By.CSS_SELECTOR, "div.search__ResultsContainer-sc-87cf44fc-7")
    RESULT_TITLES_IN_CONTAINER = (By.CSS_SELECTOR, "article.production__ProductionCard-sc-77f87755-0 p.production__Title-sc-77f87755-7 a")

    def results_exist(self):
        elements = self.find_all(self.RESULT_ITEMS)
        return len(elements) > 0
    
    def result_titles(self):
        elements = self.find_all(self.RESULT_TITLES)
        return [el.text.lower() for el in elements]

    def click_first_result(self, text, timeout = 20):
        text = text.lower()

        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(self.RESULTS_CONTAINER)
            )
        except TimeoutException:
            pass

        def find_fresh_element(driver):
            elements = driver.find_elements(*self.RESULT_TITLES_IN_CONTAINER)

            for el in elements:
                try:
                    if not el.is_displayed():
                        continue
                    if text in el.text.lower():
                        return el
                except StaleElementReferenceException:
                    continue
            return False 

        element = WebDriverWait(self.driver, timeout, poll_frequency=0.5).until(find_fresh_element)

        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

        try:
            element.click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", element)
    
