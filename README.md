# Weather Web Scraping

A desktop weather monitoring app that collects current observations from IMGW, stores them in PostgreSQL, and visualizes trends with interactive Plotly charts.

## Features
- Fetches weather data from IMGW Synop endpoint.
- Stores records in PostgreSQL.
- Displays interactive charts for temperature, precipitation, wind, humidity, and pressure.
- Supports multiple time ranges (12h, 24h, 3 days, 7 days, 30 days, full history).
- Exports filtered data to `downloaded.csv`.

## Tech Stack
- Python (Tkinter desktop UI)
- pandas
- requests + BeautifulSoup
- PostgreSQL (`psycopg2`)
- Plotly

## Requirements
- Python 3.10+
- PostgreSQL
- Dependencies from `requirements.txt`

## Setup
1. Create and activate a virtual environment:
```bash
python -m venv .venv
.venv\\Scripts\\activate
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Create a PostgreSQL database named `html`.
4. Update database credentials in `functions.py` inside `MyClass.do_conn()`.

## Run
```bash
python app.py
```

## Project Files
- `app.py` - Tkinter user interface.
- `functions.py` - scraping, database operations, filtering, plotting, CSV export.
- `data.csv` - latest downloaded source snapshot.
- `downloaded.csv` - user-exported filtered data.

## Data Source
IMGW public data: `https://danepubliczne.imgw.pl/api/data/synop/format/html`

## License
MIT (see `LICENSE`).
