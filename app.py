from flask import Flask
from flask import json
import logging
app = Flask(__name__)



@app.route('/status')
def status():
    
    response = app.response_class(
            response=json.dumps({"result":"OK - healthy"}),
            status=200,
            mimetype='application/json'
    )
    
    app.logger.info('Status request successfull')
    return response

@app.route('/metrics')
def metrics():
    response = app.response_class(
            response=json.dumps({"status":"success","code":0,"data":{"UserCount":140,"UserCountActive":23}}),
            status=200,
            mimetype='application/json'
    )
    app.logger.info('metrics request successfull')
    return response



@app.route("/")
def hello():
    app.logger.info('home request successfull')
    return "Hello World! Welcome"

if __name__ == "__main__":
    logging.basicConfig(filename='test.log',level=logging.DEBUG)

    app.run(debug=True, host='0.0.0.0')
