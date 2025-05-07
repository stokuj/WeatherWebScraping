
# Aplikacja Pogodowa - Wizualizacja Danych IMGW

Aplikacja służąca do pobierania, przechowywania oraz wizualizacji danych meteorologicznych z Instytutu Meteorologii i Gospodarki Wodnej (IMGW). 

## Funkcjonalności
- **Automatyczna aktualizacja danych**: Co 5 minut pobiera nowe dane ze strony IMGW.
- **Przechowywanie danych**: Zapis do bazy danych PostgreSQL i plików CSV.
- **Interaktywna wizualizacja**:
  - Wykresy liniowe: temperatura, ciśnienie, wilgotność, prędkość wiatru
  - Wykresy słupkowe: suma opadów
  - Różowa mapa wiatru (kierunek i siła)
  - Możliwość wyboru zakresu czasowego (24h, 7 dni, miesiąc itp.)
- **Obliczanie średnich wartości** dla wybranych parametrów
- **Eksport danych** do formatu CSV

## Wymagania systemowe
- python 3.13
- postgreSQL 13+
- pandas
- requests
- beautifulsoup4
- psycopg2-binary
- plotly
- tkinter
- sv-ttk

## Konfiguracja bazy danych
1. Zainstaluj i skonfiguruj PostgreSQL
2. Utwórz bazę danych o nazwie `html`
3. Ustaw dane dostępowe w kodzie (klasa `MyClass.do_conn()`):

  host="localhost"
  database="html"
  user="postgres"
  password="NstftHLz"

## Uruchomienie

python app.py


## Struktura danych

Tabela MyClass w PostgreSQL zawiera:
-ID rekordu
-Nazwę stacji
-Datę i godzinę pomiaru
-Parametry meteorologiczne:
 - Temperatura (°C)
 - Prędkość wiatru (m/s)
 - Kierunek wiatru (°)
 - Wilgotność względna (%)
 - Suma opadów (mm)
 - Ciśnienie (hPa)
 - 
## Uwagi

- Aplikacja wymaga aktywnego połączenia internetowego
- Dane historyczne są gromadzone od momentu pierwszego uruchomienia
- Zalecana okresowa konserwacja bazy danych (czyszczenie duplikatów)

## Licencja

MIT License - Wolne użycie do celów edukacyjnych i komercyjnych
