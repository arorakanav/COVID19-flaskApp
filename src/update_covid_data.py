from src.constants import ( CCSE_COVID19_TIME_SERIES_CONFIRMED_GLOBAL,
  CCSE_COVID19_TIME_SERIES_DEATHS_GLOBAL, 
  CCSE_COVID19_TIME_SERIES_RECOVERED_GLOBAL)

import pandas as pd

from datetime import datetime

from src.db_connection import exdb

def update_ccse_covid_time_series_confirmed_global():
  df_confirmed = pd.read_csv(CCSE_COVID19_TIME_SERIES_CONFIRMED_GLOBAL)
  df_columns = df_confirmed.columns.values
  db_dates = df_columns[4:]
  db_columns = df_columns[:4]
  db_countries = df_confirmed['Country/Region'].to_numpy()
  for date in db_dates:
    df_get_columns = list(db_columns) + list([date])
    for country in db_countries:
      country_data = df_confirmed.loc[df_confirmed['Country/Region'] == country, df_get_columns]
      for item in country_data.to_numpy():
        state = item[0]
        lat = item[2]
        lng = item[3]
        cases = item[4]
        confirmed_date = datetime.strftime(datetime.strptime(date, '%m/%d/%y'), '%Y-%m-%d')
        exdb.editData("insert into CCSE_COVID19_TIME_SERIES_CONFIRMED_GLOBAL (confirmed_date, country, state, lat, lng, cases) values (\"%s\", \"%s\", \"%s\", \"%s\", \"%s\", %d)" %(confirmed_date, country, state, lat, lng, cases))
    
def update_ccse_covid_time_series_deaths_global():
  df_deaths = pd.read_csv(CCSE_COVID19_TIME_SERIES_DEATHS_GLOBAL)
  df_columns = df_deaths.columns.values
  db_dates = df_columns[4:]
  db_columns = df_columns[:4]
  db_countries = df_deaths['Country/Region'].to_numpy()
  for date in db_dates:
    df_get_columns = list(db_columns) + list([date])
    for country in db_countries:
      country_data = df_deaths.loc[df_deaths['Country/Region'] == country, df_get_columns]
      for item in country_data.to_numpy():
        state = item[0]
        lat = item[2]
        lng = item[3]
        cases = item[4]
        confirmed_date = datetime.strftime(datetime.strptime(date, '%m/%d/%y'), '%Y-%m-%d')
        exdb.editData("insert into CCSE_COVID19_TIME_SERIES_DEATHS_GLOBAL (confirmed_date, country, state, lat, lng, cases) values (\"%s\", \"%s\", \"%s\", \"%s\", \"%s\", %d)" %(confirmed_date, country, state, lat, lng, cases))

def update_ccse_covid_time_series_recovered_global():
  df_recovered = pd.read_csv(CCSE_COVID19_TIME_SERIES_RECOVERED_GLOBAL)
  df_columns = df_recovered.columns.values
  db_dates = df_columns[4:]
  db_columns = df_columns[:4]
  db_countries = df_recovered['Country/Region'].to_numpy()
  for date in db_dates:
    df_get_columns = list(db_columns) + list([date])
    for country in db_countries:
      country_data = df_recovered.loc[df_recovered['Country/Region'] == country, df_get_columns]
      for item in country_data.to_numpy():
        state = item[0]
        lat = item[2]
        lng = item[3]
        cases = item[4]
        confirmed_date = datetime.strftime(datetime.strptime(date, '%m/%d/%y'), '%Y-%m-%d')
        exdb.editData("insert into CCSE_COVID19_TIME_SERIES_RECOVERED_GLOBAL (confirmed_date, country, state, lat, lng, cases) values (\"%s\", \"%s\", \"%s\", \"%s\", \"%s\", %d)" %(confirmed_date, country, state, lat, lng, cases))


