from flask import Flask, request, jsonify
from pymongo import MongoClient
from datetime import datetime, timedelta
import os
import sys

# Initialize environment variables
mongo_uri = os.getenv('MONGO_URI', None)
mongo_db = os.getenv('MONGO_DB', None)
mongo_col_status = os.getenv('MONGO_COL_STATUS', None)

if mongo_uri is None or mongo_db is None or mongo_col_status is None:
    print('MONGO_URI, MONGO_DB, and MONGO_COL_STATUS are required')
    sys.exit(1)

# Initialize Flask app
app = Flask(__name__)
mongo_client = MongoClient(mongo_uri)
print("MongoDB connected:", mongo_uri)

# REST API: Get Motion Status
@app.route('/api/status', methods=['GET'])
def get_status():
    resp = {}

    # Extract query parameters
    mins_cond = int(request.args.get('mins', 10))
    time_threshold = datetime.now() - timedelta(minutes=mins_cond)

    # Database connection
    db = mongo_client[mongo_db]
    db_status_col = db[mongo_col_status]

    # Retrieve data from MongoDB
    docs = db_status_col.find({"timestamp": {"$gt": time_threshold}}).sort("timestamp", -1)

    resp['status'] = 'ok'
    resp['data'] = []

    for doc in docs:
        doc_data = {
            "timestamp": doc["timestamp"].isoformat(),
            "motion_status":doc['motion']
        }
        resp['data'].append(doc_data)

    return jsonify(resp)

if __name__ == "__main__":
    app.run(debug=True)
