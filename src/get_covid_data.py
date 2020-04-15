from src.db_connection import exdb
from datetime import datetime

def get_ccse_covid_time_series_confirmed_global():
  confirmed_cases = exdb.getData("SELECT confirmed_date, country, SUM(cases) as total_confirmed_cases FROM CCSE_COVID19_TIME_SERIES_CONFIRMED_GLOBAL GROUP BY confirmed_date, country;")
  confirmed_cases_dict = dict()
  
  for confirmed_case in confirmed_cases:
    confirmed_date = datetime.strftime(confirmed_case['confirmed_date'], '%Y-%m-%d')
    country = str(confirmed_case['country'])
    total_confirmed = int(confirmed_case['total_confirmed_cases'])
    if confirmed_date in confirmed_cases_dict:
      confirmed_cases_dict[confirmed_date].update({
        country: total_confirmed
      })
    else:
      confirmed_cases_dict[confirmed_date] = {
        country: total_confirmed
      }
  return confirmed_cases_dict

def get_ccse_covid_time_series_deaths_global():
  death_cases = exdb.getData("SELECT confirmed_date, country, SUM(cases) as total_deaths FROM CCSE_COVID19_TIME_SERIES_DEATHS_GLOBAL GROUP BY confirmed_date, country;")
  deaths_dict = dict()
  for confirmed_case in death_cases:
    confirmed_date = datetime.strftime(confirmed_case['confirmed_date'], '%Y-%m-%d')
    country = str(confirmed_case['country'])
    total_deaths = int(confirmed_case['total_deaths'])
    if confirmed_date in deaths_dict:
      deaths_dict[confirmed_date].update({
        country: total_deaths
      })
    else:
      deaths_dict[confirmed_date] = {
        country: total_deaths
      }
  return deaths_dict

def get_ccse_covid_time_series_recovered_global():
  recovered_cases = exdb.getData("SELECT confirmed_date, country, SUM(cases) as total_recovered FROM CCSE_COVID19_TIME_SERIES_RECOVERED_GLOBAL GROUP BY confirmed_date, country;")
  deaths_dict = dict()
  
  for confirmed_case in recovered_cases:
    recovered_date = datetime.strftime(confirmed_case['confirmed_date'], '%Y-%m-%d')
    country = str(confirmed_case['country'])
    total_recovered = int(confirmed_case['total_recovered'])
    if recovered_date in deaths_dict:
      deaths_dict[recovered_date].update({
        country: total_recovered
      })
    else:
      deaths_dict[recovered_date] = {
        country: total_recovered
      }
  return deaths_dict

def get_ccse_covid_time_series_summary_table_global():
  cases_summary = exdb.getData("with confirmed_table as (\
    SELECT country, SUM(CCSE_COVID19_TIME_SERIES_CONFIRMED_GLOBAL.cases) as total_confirmed_cases\
    FROM CCSE_COVID19_TIME_SERIES_CONFIRMED_GLOBAL\
    GROUP BY country),\
    recovered_table as (\
    SELECT country, SUM(cases) as total_recovered\
    FROM CCSE_COVID19_TIME_SERIES_RECOVERED_GLOBAL\
    GROUP BY country),\
    deaths_table as (\
    SELECT country, SUM(cases) as total_deaths\
    FROM CCSE_COVID19_TIME_SERIES_DEATHS_GLOBAL\
    GROUP BY country)\
    SELECT c.country, c.total_confirmed_cases, r.total_recovered, d.total_deaths\
    from confirmed_table c\
    JOIN recovered_table r\
        ON c.country = r.country\
    JOIN deaths_table d\
        ON d.country = r.country;")
  summary_dict = dict()
  for case in cases_summary:
    country = str(case['country'])
    total_confirmed = int(case['total_confirmed_cases'])
    total_recovered = int(case['total_recovered'])
    total_deaths = int(case['total_deaths'])
    summary_dict[country] = {
      'recovered': total_recovered,
      'confirmed': total_confirmed,
      'deaths': total_deaths
    }
  return summary_dict

def get_ccse_covid_geo_summary_global():
  geo_summary = exdb("with confirmed_table as (\
      SELECT lat, lng, SUM(CCSE_COVID19_TIME_SERIES_CONFIRMED_GLOBAL.cases) as total_confirmed_cases\
      FROM CCSE_COVID19_TIME_SERIES_CONFIRMED_GLOBAL\
      GROUP BY lat, lng),\
      recovered_table as (\
      SELECT lat, lng, SUM(cases) as total_recovered\
      FROM CCSE_COVID19_TIME_SERIES_RECOVERED_GLOBAL\
      GROUP BY lat, lng),\
      deaths_table as (\
      SELECT lat, lng, SUM(cases) as total_deaths\
      FROM CCSE_COVID19_TIME_SERIES_DEATHS_GLOBAL\
      GROUP BY lat, lng)\
      SELECT c.lat, c.lng, c.total_confirmed_cases, r.total_recovered, d.total_deaths\
      from confirmed_table c\
      JOIN recovered_table r\
      ON c.lat = r.lat\
      AND c.lng = r.lng\
      JOIN deaths_table d\
      ON r.lat = d.lat\
      AND r.lng = d.lng;")[0]
  summary_dict = dict()
  return geo_summary
