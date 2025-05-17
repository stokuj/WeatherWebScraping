
# Aplikacja Pogodowa - Wizualizacja Danych IMGW

Aplikacja służąca do pobierania, przechowywania oraz wizualizacji danych meteorologicznych z Instytutu Meteorologii i Gospodarki Wodnej (IMGW). Umożliwia monitorowanie warunków pogodowych dla 75 stacji meteorologicznych w Polsce.

## Funkcjonalności
- **Automatyczna aktualizacja danych**: Co 5 minut pobiera nowe dane ze strony IMGW.
- **Przechowywanie danych**: Zapis do bazy danych PostgreSQL i plików CSV.
- **Interaktywna wizualizacja**:
  - Wykresy liniowe: temperatura, ciśnienie, wilgotność, prędkość wiatru
  - Wykresy słupkowe: suma opadów
  - Różowa mapa wiatru (kierunek i siła)
  - Możliwość wyboru zakresu czasowego (12h, 24h, 3 dni, 7 dni, miesiąc, cały zakres)
- **Obliczanie średnich wartości** dla wybranych parametrów meteorologicznych
- **Eksport danych** do formatu CSV dla dalszej analizy

## Wymagania systemowe
- Python 3.x
- PostgreSQL 13+
- Biblioteki Python:
  - pandas==2.2.3
  - requests==2.32.3
  - beautifulsoup4==4.11.1
  - psycopg2==2.9.10
  - plotly==6.0.1
  - sv-ttk==2.6.0
  - tkinter (wbudowany w Pythona)

## Instalacja
1. Sklonuj repozytorium:
   ```
   git clone [adres-repozytorium]
   ```
2. Utwórz i aktywuj wirtualne środowisko (opcjonalnie):
   ```
   python -m venv .venv
   .venv\Scripts\activate
   ```
3. Zainstaluj wymagane zależności:
   ```
   pip install -r requirements.txt
   ```

## Konfiguracja bazy danych
1. Zainstaluj i skonfiguruj PostgreSQL
2. Utwórz bazę danych o nazwie `html`
3. Ustaw dane dostępowe w kodzie (klasa `MyClass.do_conn()`):
   ```python
   host="localhost"
   database="html"
   user="postgres"
   password="NstftHLz"
   ```

## Uruchomienie
```
python app.py
```

## Struktura danych
Tabela `MyClass` w PostgreSQL zawiera:
- ID rekordu (id)
- ID stacji (id_stacji)
- Nazwę stacji (stacja)
- Datę pomiaru (data_pomiaru)
- Godzinę pomiaru (godzina_pomiaru)
- Parametry meteorologiczne:
  - Temperatura (°C)
  - Prędkość wiatru (m/s)
  - Kierunek wiatru (°)
  - Wilgotność względna (%)
  - Suma opadów (mm)
  - Ciśnienie (hPa)
- Znacznik czasowy (data_godzina)

## Interfejs użytkownika
Aplikacja posiada intuicyjny interfejs graficzny z następującymi funkcjami:
- Wybór stacji meteorologicznej z listy 75 stacji w Polsce
- Wybór typu wykresu (temperatura, opady, wiatr, wilgotność, ciśnienie)
- Wybór zakresu czasowego dla danych
- Obliczanie średnich wartości dla wybranych parametrów
- Eksport danych do pliku CSV

## Uwagi
- Aplikacja wymaga aktywnego połączenia internetowego
- Dane historyczne są gromadzone od momentu pierwszego uruchomienia
- Zalecana okresowa konserwacja bazy danych (czyszczenie duplikatów)
- Funkcja `deleteDuplicates()` automatycznie usuwa zduplikowane rekordy

## Licencja
MIT License - Wolne użycie do celów edukacyjnych i komercyjnych

# Weather Application - IMGW Data Visualization

An application for fetching, storing, and visualizing meteorological data from the Institute of Meteorology and Water Management (IMGW). It enables monitoring of weather conditions for 75 meteorological stations in Poland.

## Features
- **Automatic data updates**: Fetches new data from the IMGW website every 5 minutes.
- **Data storage**: Saves to PostgreSQL database and CSV files.
- **Interactive visualization**:
  - Line charts: temperature, pressure, humidity, wind speed
  - Bar charts: precipitation
  - Polar wind map (direction and strength)
  - Time range selection (12h, 24h, 3 days, 7 days, month, entire range)
- **Calculation of average values** for selected meteorological parameters
- **Data export** to CSV format for further analysis

## System Requirements
- Python 3.x
- PostgreSQL 13+
- Python libraries:
  - pandas==2.2.3
  - requests==2.32.3
  - beautifulsoup4==4.11.1
  - psycopg2==2.9.10
  - plotly==6.0.1
  - sv-ttk==2.6.0
  - tkinter (built into Python)

## Installation
1. Clone the repository:
   ```
   git clone [repository-address]
   ```
2. Create and activate a virtual environment (optional):
   ```
   python -m venv .venv
   .venv\Scripts\activate
   ```
3. Install required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Database Configuration
1. Install and configure PostgreSQL
2. Create a database named `html`
3. Set access data in the code (class `MyClass.do_conn()`):
   ```python
   host="localhost"
   database="html"
   user="postgres"
   password="NstftHLz"
   ```

## Running the Application
```
python app.py
```

## Data Structure
The `MyClass` table in PostgreSQL contains:
- Record ID (id)
- Station ID (id_stacji)
- Station name (stacja)
- Measurement date (data_pomiaru)
- Measurement time (godzina_pomiaru)
- Meteorological parameters:
  - Temperature (°C)
  - Wind speed (m/s)
  - Wind direction (°)
  - Relative humidity (%)
  - Precipitation (mm)
  - Pressure (hPa)
- Timestamp (data_godzina)

## User Interface
The application has an intuitive graphical interface with the following functions:
- Selection of meteorological station from a list of 75 stations in Poland
- Selection of chart type (temperature, precipitation, wind, humidity, pressure)
- Selection of time range for data
- Calculation of average values for selected parameters
- Export of data to CSV file

## Notes
- The application requires an active internet connection
- Historical data is collected from the moment of first launch
- Periodic database maintenance is recommended (cleaning duplicates)
- The `deleteDuplicates()` function automatically removes duplicate records

## License
MIT License - Free use for educational and commercial purposes
