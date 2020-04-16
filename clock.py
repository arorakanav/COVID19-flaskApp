from src.update_covid_data import (update_ccse_covid_time_series_confirmed_global,
  update_ccse_covid_time_series_recovered_global,
  update_ccse_covid_time_series_deaths_global)

from apscheduler.schedulers.blocking import BlockingScheduler

scheduler = BlockingScheduler()
@scheduler.scheduled_job('interval', hour=0)
def update_ccse_covid_time_series_confirmed_global_job():
  update_ccse_covid_time_series_confirmed_global()

@scheduler.scheduled_job('interval', hour=0)
def update_ccse_covid_time_series_recovered_global_job():
  update_ccse_covid_time_series_recovered_global()

@scheduler.scheduled_job('interval', hour=0)
def update_ccse_covid_time_series_deaths_global_job():
  update_ccse_covid_time_series_deaths_global()

scheduler.start()