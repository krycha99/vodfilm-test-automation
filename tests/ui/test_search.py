from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage

def test_search_returns_correct_results(driver):
    
    driver.get("https://vod.film")

    home = HomePage(driver)
    home.close_cookie_popup()
    home.search_for("pirx")

    results = SearchResultsPage(driver)
    titles = results.result_titles()
    
    assert results.results_exist()
    for title in titles: assert "pirx" in title.lower()