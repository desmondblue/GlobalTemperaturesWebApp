from flask import Flask,jsonify, request, make_response
import json
from GlobalTempServiceImpl.GlobalLandTempByCityServiceImpl import GlobalLandTempByCityServiceImpl


app = Flask(__name__)
service = GlobalLandTempByCityServiceImpl()

"""
REST API for inserting row data
"""
@app.route("/insert-row-data",methods=['POST'])
def insertRowData():
    data = request.get_json()
    result = service.insert_row_in_table(data)
    return json.dumps(result)

"""
REST API for updating data
"""
@app.route("/update-row-data",methods=['POST'])
def updateRowData():
    data = request.get_json()
    result = service.update_row_in_table(data)
    return json.dumps(result)

"""
REST API for getting top n ciites in descending order of Maximum Average Temp
"""
@app.route("/get-top-cities",methods=['POST'])
def getTopCities():
    data = request.get_json()
    result = service.return_top_cities(data)
    return json.dumps(result)


@app.errorhandler(400)
def bad_request(exception):
    return make_response(jsonify({"error":str(exception)}),400)

@app.errorhandler(500)
def server_error(exception):
    return make_response(jsonify({"error":str(exception)}),400)


if __name__ == '__main__':
    app.run()
