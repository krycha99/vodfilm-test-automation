from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from pages.movie_page import MoviePage

def test_movie_title(driver):
    
    driver.get("https://vod.film")
    phrase = "pirx"

    home = HomePage(driver)
    home.close_cookie_popup()
    home.search_for(phrase)
    
    results = SearchResultsPage(driver)
    results.click_first_result(phrase)

    movie = MoviePage(driver)
    title = movie.get_movie_title()

    assert results.results_exist()
    assert "pirx" in title.lower()