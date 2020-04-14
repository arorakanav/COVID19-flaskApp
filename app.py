from flask import Flask
from flask_cors import CORS

from src.covidapp import covidapp


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
    app.run(threaded=True, host="0.0.0.0", use_reloader=True, debug=True)
    


