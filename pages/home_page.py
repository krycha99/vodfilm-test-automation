from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage

class HomePage(BasePage):

    SEARCH_ICON = (By.CSS_SELECTOR, "img[alt='search icon']")
    SEARCH_INPUT = (By.ID, "search")
    MOVIE_BUTTON = (By.CSS_SELECTOR, "a[href='/filmy']")

    def click_search_icon(self):
        self.click(self.SEARCH_ICON)
    
    def enter_search_text(self, text: str):
        self.enter_text(self.SEARCH_INPUT, text)
    
    def submit_search(self):
        search_field = self.find(self.SEARCH_INPUT)
        search_field.send_keys(Keys.ENTER)

    def search_for(self, text: str):
        self.click_search_icon()
        self.enter_search_text(text)
        self.submit_search()

    def go_to_movies_page(self):
        self.click(self.MOVIE_BUTTON)