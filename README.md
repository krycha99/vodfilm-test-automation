# VodFilm Test Automation

## Stack technologiczny

- **Python** 3.11.9
- **Selenium** (wybrana biblioteka do automatyzacji)
- **requests** (do testów API)
- **pytest** (do uruchamiania testów automatycznych)
- **Docker** (do konteneryzacji środowiska testowego)
- **Git** (do kontroli wersji i publikacji na GitHub)
- **GitHub Actions** (do CI/CD, automatycznego uruchamiania testów po pushu)

## 1. Instalacja zależności

Projekt wymaga Pythona 3.11 i pip. Aby zainstalować wszystkie zależności, uruchom:
```
pip install -r requirements.txt
```
## 2. Uruchamianie testów

Wszystkie testy (UI, E2E i API) można uruchomić za pomocą pytest:
```
pytest
```
Aby uruchomić tylko testy E2E lub API, można użyć markerów:
```
# Tylko testy E2E
pytest -m e2e

# Tylko testy API
pytest -m api
```
### Uruchomienie testów w kontenerze Docker:

1. Znajdując się w głównym katalogu projektu zbuduj obraz Dockera:
```
docker build -t vodfilm-tests .
```
2. Uruchom kontener:
```
docker run --rm vodfilm-tests
```
Kontener został skonfigurowany tak, aby automatycznie uruchamiać wszystkie testy po starcie.

## 3. Wybrana biblioteka do automatyzacji

W projekcie wykorzystano bibliotekę **Selenium**.

**Uzasadnienie wyboru:**
<br>Głównym powodem wyboru Selenium jest moje większe doświadczenie w pracy z tą biblioteką w porównaniu do Playwright.  
Pozwala to na szybsze i pewniejsze tworzenie testów. Dodatkowo Selenium wymaga minimalnej konfiguracji i dobrze integruje się z pytest.

## 4. Opis zidentyfikowanego endpointu API

Test API korzysta z endpointu:
```
POST https://vod.film/search-route
```

Przykładowy Payload:
```
{
    "host": "vod.film",
    "locale": "pl",
    "searchTerm": "test"
}
```
Endpoint zwraca dane o filmach i serialach dopasowanych do frazy searchTerm. Test sprawdza, czy odpowiedź HTTP jest 200 oraz czy w ciele odpowiedzi znajduje się przynajmniej jeden wynik zawierający tytuł wyszukiwanego filmu.

## 5. Założenia, uproszczenia i napotkane problemy

Podczas realizacji projektu pojawiły się następujące wyzwania i założenia:  

- **Dynamiczne ładowanie strony:**  
  Podczas testów E2E wystąpił problem z kliknięciem w wyszukiwany film, który wynikał z dynamicznego ładowania wyników. Rozwiązaniem było zastosowanie odpowiednich metod oczekiwania (wait) w Selenium, aby upewnić się, że element jest widoczny i klikalny.

- **Pobranie linku z popupu:**  
  Uzyskanie docelowego linku po kliknięciu w popup było początkowo problematyczne z powodu braku doświadczenia.  
  Podjęto próby wydobycia linku bezpośrednio z atrybutów HTML, kodu JavaScript oraz przez śledzenie requestów sieciowych. Ostatecznie zdecydowano się pobierać URL po kliknięciu, co pozwalało poprawnie zweryfikować przekierowanie.

- **Nauka POM w trakcie projektu:**  
  Jednym z wyzwań był brak wcześniejszej styczności z Page Object Model. W trakcie realizacji testów E2E musiałem zapoznać się z tą strukturą i wdrożyć ją w projekcie, aby testy były bardziej modularne i łatwiejsze w utrzymaniu.

- **Wdrożenie Dockera i CI/CD:**  
  Testy zostały skonfigurowane do uruchamiania w kontenerze Docker oraz w ramach pipeline CI/CD w GitHub Actions. Dzięki temu możliwe jest automatyczne uruchamianie testów po każdym pushu do repozytorium.

## 6. Raporty błędów

Raporty w plikach .md dotyczące wykrytych błędów (zgodnie z wymaganiami C.1 i C.2) znajdują się w folderze `reports`.

Błąd numer 1 (Główne zadanie): [Raport nr 1](reports/Blad_nr_1)
  
Błąd numer 2 (Opcjonalny): [Raport nr 2](reports/Blad_nr_2)

## Wnioski z realizacji zadania

- **Praca nad lepszym zrozumieniem mechanizmów oczekiwania (waits):**  
  Praca nad testami E2E pokazała, że kluczowe jest świadome stosowanie różnych typów oczekiwań w Selenium, aby stabilnie reagować na dynamiczne ładowanie elementów.

- **Udoskonalenie struktury POM (Page Object Model):**  
  Tworzenie POM w trakcie projektu pozwoliło lepiej zrozumieć zalety i wyzwania tej architektury. Warto poświęcić czas na planowanie i rozdzielenie odpowiedzialności między stronami, co ułatwia późniejsze rozszerzanie testów.

- **Obsługa dynamicznych elementów i wydobywanie linków:**  
  Praca nad przyciskiem popup ujawniła potrzebę głębszego zrozumienia, jak wydobywać dane (np. URL) z elementów generowanych dynamicznie przez JavaScript.

## Ogólne refleksje nad projektem

- Projekt był dobrą okazją do połączenia testów UI i API w jednym workflow, co pozwoliło mi sprawdzić oraz rozwinąć swoje dotychczasowe umiejętności.
- Zrozumienie i praktyczne zastosowanie POM, mechanizmów wait oraz integracja z CI/CD znacząco podniosły moje doświadczenie w automatyzacji testów.