from src.update_covid_data import (update_ccse_covid_time_series_confirmed_global,
  update_ccse_covid_time_series_recovered_global,
  update_ccse_covid_time_series_deaths_global)

from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()
@scheduler.scheduled_job('interval', minutes=20)
def update_ccse_covid_time_series_global_job():
  update_ccse_covid_time_series_confirmed_global()
  update_ccse_covid_time_series_recovered_global()
  update_ccse_covid_time_series_deaths_global()

# scheduler.start()