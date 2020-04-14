from flask import Blueprint, jsonify

from src.get_covid_data import ( get_ccse_covid_time_series_confirmed_global,
  get_ccse_covid_time_series_deaths_global,
  get_ccse_covid_time_series_recovered_global,
  get_ccse_covid_time_series_summary_table_global,
  get_ccse_covid_geo_summary_global)

covidapp = Blueprint('covidapp', __name__, url_prefix="/covidapp")

@covidapp.route('/test', methods = ['GET'])
def test():
  return jsonify({"success": True, "message": "Data received Successfully! checking reload"})

@covidapp.route('/time_series_confirmed_global', methods = ['GET'])
def time_series_confirmed_global():
  data = get_ccse_covid_time_series_confirmed_global()
  return jsonify({"success": True, "message": "Data received Successfully! checking reload", "data": data})

@covidapp.route('/time_series_deaths_global', methods = ['GET'])
def time_series_deaths_global():
  data = get_ccse_covid_time_series_deaths_global()
  return jsonify({"success": True, "message": "Data received Successfully! checking reload", "data": data})

@covidapp.route('/time_series_recovered_global', methods = ['GET'])
def time_series_recovered_global():
  data = get_ccse_covid_time_series_recovered_global()
  return jsonify({"success": True, "message": "Data received Successfully! checking reload", "data": data})

@covidapp.route('/time_series_summary_table_global', methods = ['GET'])
def time_series_summary_global():
  data = get_ccse_covid_time_series_summary_table_global()
  return jsonify({"success": True, "message": "Data received Successfully! checking reload", "data": data})

@covidapp.route('/time_series_geo_summary_global', methods = ['GET'])
def time_series_geo_summary_global():
  data = get_ccse_covid_geo_summary_global()
  return jsonify({"success": True, "message": "Data received Successfully! checking reload", "data": data})