-- 1. Preview the merged weather and population data
-- Replace YOUR_PROJECT_ID and YOUR_DATASET with your actual BigQuery names.

SELECT
  city,
  country,
  temperature_c,
  humidity,
  apparent_temperature_c,
  population
FROM `YOUR_PROJECT_ID.YOUR_DATASET.merged_weather_population`
LIMIT 10;


-- 2. Top 5 hottest countries with population above 10 million
SELECT
  country,
  population,
  ROUND(AVG(temperature_c), 2) AS average_temperature_c
FROM `YOUR_PROJECT_ID.YOUR_DATASET.merged_weather_population`
WHERE population > 10000000
GROUP BY country, population
ORDER BY average_temperature_c DESC
LIMIT 5;


-- 3. Average temperature by country
SELECT
  country,
  ROUND(AVG(temperature_c), 2) AS average_temperature_c,
  COUNT(*) AS number_of_cities
FROM `YOUR_PROJECT_ID.YOUR_DATASET.merged_weather_population`
GROUP BY country
ORDER BY average_temperature_c DESC;


-- 4. Categorize cities by temperature for dashboard filters
SELECT
  city,
  country,
  latitude,
  longitude,
  temperature_c,
  humidity,
  population,
  CASE
    WHEN temperature_c < 15 THEN 'Cold'
    WHEN temperature_c < 30 THEN 'Mild'
    ELSE 'Hot'
  END AS temperature_category
FROM `YOUR_PROJECT_ID.YOUR_DATASET.merged_weather_population`;
