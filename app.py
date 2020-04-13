from flask import Flask
from flask_cors import CORS

from src.covidapp import covidapp
from src.update_covid_data import (update_ccse_covid_time_series_confirmed_global,
  update_ccse_covid_time_series_recovered_global,
  update_ccse_covid_time_series_deaths_global)

from apscheduler.schedulers.background import BackgroundScheduler


#Creating a FLASK instance
app = Flask(__name__)
app.register_blueprint(covidapp)
CORS(app)

@app.route("/")
def helloWorld():
  return "Hello, cross-origin-world!"

#Cors
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

if __name__ == '__main__':
    app.run(threaded=True, host="0.0.0.0:8000", use_reloader=True, debug=true)
    scheduler = BackgroundScheduler()
    scheduler.add_job(update_ccse_covid_time_series_confirmed_global, 'interval', minutes=20)
    scheduler.add_job(update_ccse_covid_time_series_recovered_global, 'interval', minutes=20)
    scheduler.add_job(update_ccse_covid_time_series_deaths_global, 'interval', minutes=20)
    scheduler.start()


