from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from pages.movie_page import MoviePage
from selenium.webdriver.common.by import By

def test_movie_popup_and_link(driver):
    
    driver.get("https://vod.film")
    
    phrase = "pirx"
    
    home = HomePage(driver)
    home.close_cookie_popup()
    home.search_for(phrase)
    
    results = SearchResultsPage(driver)
    results.click_first_result(phrase)

    movie = MoviePage(driver)

    movie.wait_for_player()
    assert movie.is_player_visible() is True
    
    movie.click_play()
    play_button = movie.driver.find_element(By.CSS_SELECTOR, "button[data-plyr='play']")
    assert play_button.get_attribute("aria-pressed") == "true", "Przycisk play powinien być wciśnięty podczasz odtwarzania"

    popup = movie.wait_for_popup()
    assert popup.is_displayed()

    link = movie.get_popup_link()
    assert link is not None
    print(f"Popup link: {link}") 