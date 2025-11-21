import pytest
from selenium.webdriver.common.by import By
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from pages.movie_page import MoviePage

@pytest.mark.e2e
@pytest.mark.parametrize("search_phrase, should_exist", [
    ("the pickup", True), #fraza pozytywna
    ("abcxyz123", False), #fraza negatywna
])

def test_search_flow(driver, search_phrase, should_exist):
    # test E2E wyszukiwarki filmów

    # 1. Wejście na stronę główną
    driver.get("https://vod.film")
    home = HomePage(driver)
    home.close_cookie_popup()

    # 2. Kliknięcie w ikonę lupki
    # 3. Wyszukanie "frazy"
    home.search_for(search_phrase)
    results = SearchResultsPage(driver)

    if should_exist:
        # 4. Sprawdzenie czy "fraza" pojawia się w wyszukiwaniach.
        titles = results.result_titles()
        assert results.results_exist
        for title in titles: assert search_phrase in title.lower(), "Wyszukiwane filmy nie zawierają frazy"

        # 5. Wejście na stronę szczegółów tego filmu.
        results.click_first_result(search_phrase)

        # 6. Sprawdzenie, czy nagłówek H1 na stronie filmu zawiera "frazę".
        movie = MoviePage(driver)
        movie.wait_for_player()
        h1_text = movie.get_movie_title()
        assert search_phrase.lower() in h1_text.lower(), "Nagłówek H1 nie zawiera wyszukiwanej frazy"

        # 7.Sprawdzenie, czy na stronie widoczny jest odtwarzacz wideo.
        assert movie.is_player_visible(), "Odtwarzacz jest niewidoczny"

        # 8. Uruchomienie odtwarzania filmu (kliknięcie "play").
        movie.click_play()
        play_button = movie.driver.find_element(By.CSS_SELECTOR, "button[data-plyr='play']")
        assert play_button.get_attribute("aria-pressed") == "true", "Przycisk Play powinien być wciśnięty podczas odtwarzania"

        # 9. Weryfikacja asynchroniczności: Sprawdzenie, czy w przedziale od 1 do 60 sekund odtwarzanie zostanie przerwane i na ekranie pojawi się popup.
        popup = movie.wait_for_popup(timeout=60)
        assert popup.is_displayed(), "Popup nie został wyświetlony"

        # 10. Sprawdzenie, na jaki adres URL (lub domenę) próbuje przekierować użytkownika kliknięcie w ten popup.
        popup_link = movie.get_popup_link()
        assert popup_link is not None, "Nie znaleziono linku przeikierowania"
        print(f"Popup link: {popup_link}")

    else:
        #Negatywna fraza - brak wyników wyszukiwania
        titles = results.result_titles()
        assert results.results_exist
        for title in titles: assert search_phrase not in title.lower(), "Dla frazy negatywnej wyszukiwanie nie powinno znaleźć żadnych wyników"

