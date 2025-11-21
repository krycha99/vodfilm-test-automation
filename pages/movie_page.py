from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MoviePage(BasePage):

    MOVIE_TITLE = (By.CSS_SELECTOR, "h1[class*='H1']")
    VIDEO_PLAYER = (By.ID, "player")
    PLAY_BUTTON = (By.CSS_SELECTOR, "button[data-plyr='play']")
    POPUP = (By.ID, "popup")
    POPUP_BUTTON = (By.CSS_SELECTOR, "#register-now.FinalMessage__StyledButton-sc-14cea9d8-4.bg-purple")
    OVERLAY = (By.CSS_SELECTOR, ".plyr__controls--overlaid, .plyr__control--overlaid")

    def get_movie_title(self):
        element = self.find(self.MOVIE_TITLE)
        return element.text.strip()
    
    def wait_for_player(self, timeout=15):

        def player_loaded(driver):
            elems = driver.find_elements(*self.VIDEO_PLAYER)
            if not elems:
                return False

            elem = elems[0]

            if not elem.is_displayed():
                return False

            size = elem.size
            if size["height"] < 50:
                return False

            return elem

        return WebDriverWait(self.driver, timeout).until(player_loaded)
    
    def is_player_visible(self):
        self.wait_for_visible(self.VIDEO_PLAYER)
        element = self.find(self.VIDEO_PLAYER)
        return element.is_displayed()
    
    def wait_for_play_button_ready(self, timeout=20):
        
        player = self.find(self.VIDEO_PLAYER)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", player)

        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(self.PLAY_BUTTON)
        )

        try:
            WebDriverWait(self.driver, timeout).until_not(
                EC.visibility_of_element_located(self.OVERLAY)
            )
        except:
            pass

    def click_play(self):
        self.wait_for_play_button_ready()
        button = self.find(self.PLAY_BUTTON)
        button.click()

    def wait_for_popup(self, timeout=60):
        return self.wait_for_visible(self.POPUP, timeout)

    def get_popup_link(self, timeout=20):

        button = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(self.POPUP_BUTTON)
        )
        old_url = self.driver.current_url
        button.click()
        WebDriverWait(self.driver, 20).until(lambda d: d.current_url != old_url)
        link = self.driver.current_url
        return link
    