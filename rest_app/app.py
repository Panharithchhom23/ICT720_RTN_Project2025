import sys
from flask import Flask, request, jsonify
from pymongo import MongoClient
from datetime import datetime, timedelta
import os

# Load environment variables
mongo_uri = os.getenv('MONGO_URI', None)
mongo_db = os.getenv('MONGO_DB', None)
mongo_col_status = os.getenv('MONGO_COL_STATUS', None)
if mongo_uri is None or mongo_db is None or mongo_col_status is None:
    print('MONGO_URI is required')
    sys.exit(1)

# Initialize Flask app
app = Flask(__name__)
mongo_client = MongoClient(mongo_uri)
db = mongo_client[mongo_db]
status_collection = db[mongo_col_status]

print(f"Connected to MongoDB at {mongo_uri}, Database: {mongo_db}")

# Store Machine Status from MQTT messages
@app.route('/api/status', methods=['POST'])
def log_status():
    data = request.json
    
    # Log the incoming request to check the data format
    print("Received data:", data)
    
    # Validate that required fields are present
    if "motion" not in data.keys():
        return jsonify({"status": "error", "message": "Invalid data: 'device' and 'status' are required fields."}), 400
    
    status_record = {
        "alert_type": data["motion"],
        "timestamp": datetime.now()
    }
    
    # Insert the status record into MongoDB
    status_collection.insert_one(status_record)
    
    return jsonify({"status": "ok", "message": "Data logged successfully"})

# Get Machine Status
@app.route('/api/status/<device_id>', methods=['GET'])
def get_status(device_id):
    mins_cond = int(request.args.get('mins', 10))
    time_threshold = datetime.now() - timedelta(minutes=mins_cond)

    # Query the status collection for records for the specified device in the last X minutes
    records = status_collection.find({"device": device_id, "timestamp": {"$gt": time_threshold}}).sort("timestamp", -1)
    
    response = {
        "status": "ok",
        "device": device_id,
        "data": []
    }

    # Process each record and format the response
    for record in records:
        response["data"].append({
            "timestamp": record["timestamp"].isoformat(),
            "status": record["status"],
            "alert_type": record.get("alert_type", "status_update")
        })

    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
