from flask import Flask, jsonify, request
from utils import internal_auth_required
import os
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

@app.route("/", methods=['get'])
def index():
    welcome_message = "Welcome at Dataviz hello!"
    return welcome_message, 200 # 204 no content response


#@app.route('/auth', methods=['get'])
#@internal_auth_required
#def dummy_function():
#    request_json = request.get_json()
#    print(request_json)
#    return jsonify(request_json), 200

from bq_execute_query import get_bq_data_function

@internal_auth_required
@app.route('/bq_execute_query', methods=['post'])
def dummy_function():
    request_json = request.get_json()
    query = request_json['query']
    print(request_json)
    return get_bq_data_function(query)


if __name__ == "__main__":
    server_port = int(os.environ.get("PORT", 2001))
    app.run(host='0.0.0.0', port=server_port, debug=True)
