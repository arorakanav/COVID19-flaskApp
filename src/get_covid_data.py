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
  confirmed_cases = exdb.getData("SELECT confirmed_date, country, SUM(cases) as total_deaths FROM CCSE_COVID19_TIME_SERIES_DEATHS_GLOBAL GROUP BY confirmed_date, country;")
  deaths_dict = dict()
  
  for confirmed_case in confirmed_cases:
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
  confirmed_cases = exdb.getData("SELECT confirmed_date, country, SUM(cases) as total_recovered FROM CCSE_COVID19_TIME_SERIES_RECOVERED_GLOBAL GROUP BY confirmed_date, country;")
  deaths_dict = dict()
  
  for confirmed_case in confirmed_cases:
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
