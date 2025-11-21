import pytest
import requests

BASE_URL = "https://vod.film"

@pytest.mark.api
@pytest.mark.parametrize(
    "query, expected_non_empty",
    [
        ("the pickup", True)
    ]
)
def test_search_route_response_structure(driver, query, expected_non_empty):
    
    # test API /search-route
    driver.get(BASE_URL)

    selenium_cookies = driver.get_cookies()
    cookies = {c['name']: c['value'] for c in selenium_cookies}

    headers = {
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json",
        "Origin": "https://vod.film",
        "Referer": "https://vod.film/",
        "User-Agent": driver.execute_script("return navigator.userAgent;")
    }

    payload = {
        "host": "vod.film",
        "locale": "pl",
        "searchTerm": query
    }

    url = f"{BASE_URL}/search-route"
    response = requests.post(url, json=payload, headers=headers, cookies=cookies)

    # Sprawdzenie status code
    assert response.status_code == 200, f"API nie zwraca statusu 200, otrzymano {response.status_code}"

    # Sprawdzenie JSON
    data = response.json().get("data")
    assert isinstance(data, list), "Brak listy 'data' w odpowiedzi"

    if expected_non_empty:
        assert len(data) > 0, "Lista jest pusta dla pozytywnej frazy"
    else:
        assert len(data) == 0, "Oczekiwano pustej listy dla negatywnej frazy"

    # Sprawdzenie czy w ciele odpowiedzi (JSON) znajdują się dane szukanego filmu
    if expected_non_empty:
        found = any(query.lower() in item.get("title", "").lower() or
                    query.lower() in item.get("title_with_prefix", "").lower()
                    for item in data)
        assert found, f"Żaden wynik w odpowiedzi nie zawiera frazy '{query}'"




    