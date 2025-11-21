from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from pages.movie_page import MoviePage

def test_movie_player_visibility(driver):
    
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