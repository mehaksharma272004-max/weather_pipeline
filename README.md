# Weather & Demographic Data Pipeline

An end-to-end data engineering project that collects live weather data for 50 capital cities, combines it with country-level population data, and prepares the dataset for analysis and visualization.

## Project Overview

This project demonstrates a data pipeline using Python, Pandas, SQL, Google BigQuery, and Looker Studio.

### Key Features

- Fetches current weather metrics from the Open-Meteo API.
- Collects country population data.
- Combines weather and demographic datasets using Python and Pandas.
- Stores and analyzes data using Google BigQuery.
- Supports SQL-based analysis of hot countries with populations above 10 million.
- Enables an interactive Looker Studio dashboard with a map and temperature categories.

## Tech Stack

- **Language:** Python
- **Data Processing:** Pandas
- **API:** Open-Meteo
- **Database & Analytics:** Google BigQuery and SQL
- **Visualization:** Looker Studio
- **Version Control:** Git and GitHub

## Project Structure

```text
weather_pipeline/
├── data/
├── scripts/
│   └── main.py
├── .gitignore
└── README.md
```

## Dataset

The pipeline combines current weather observations with country-level population data.

Weather metrics include:
- City and country
- Latitude and longitude
- Temperature (°C)
- Humidity (%)
- Apparent temperature (°C)
- Observation time
- Population

## Run Locally

1. Clone this repository:

   ```bash
   git clone https://github.com/mehaksharma272004-max/weather_pipeline.git
   cd weather_pipeline
   ```

2. Create and activate a Python virtual environment.

3. Install the required packages:

   ```bash
   pip install requests pandas google-cloud-bigquery pyarrow
   ```

4. Run the pipeline:

   ```bash
   python scripts/main.py
   ```

## Author

**Mehak Sharma**

GitHub: [@mehaksharma272004-max](https://github.com/mehaksharma272004-max)
