import paho.mqtt.client as mqtt
from datetime import datetime
import requests
import json
import os
import sys
from pymongo import MongoClient


# Load environment variables
mongo_uri = os.getenv('MONGO_URI')
mongo_db = os.getenv('MONGO_DB')
mongo_col_status = os.getenv('MONGO_COL_STATUS')
mqtt_broker = os.getenv('MQTT_BROKER')
mqtt_port = int(os.getenv('MQTT_PORT'))
mqtt_topic = os.getenv('MQTT_TOPIC')
telegram_bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
telegram_chat_id = os.getenv('TELEGRAM_CHAT_ID')

# Ensure all required environment variables are set
if not all([mongo_uri, mongo_db, mongo_col_status, mqtt_broker, mqtt_port, mqtt_topic, telegram_bot_token, telegram_chat_id]):
    print('Missing required environment variables.')
    sys.exit(1)

# Initialize MongoDB
mongo_client = MongoClient(mongo_uri)
db = mongo_client[mongo_db]
status_collection = db[mongo_col_status]

# Function to send alerts to Telegram
def send_telegram_alert(message):
    if not telegram_bot_token or not telegram_chat_id:
        print("Telegram bot credentials not set.")
        return
    url = f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage"
    payload = {"chat_id": telegram_chat_id, "text": message}
    try:
        requests.post(url, json=payload)
    except requests.RequestException as e:
        print("Error sending Telegram alert:", e)

# MQTT Callbacks
def on_connect(client, userdata, flags, reason_code, properties=None):
    print(f"Connected with result code {reason_code}")
    # In MQTT 5.0, properties should be passed, even if not used
    client.subscribe(mqtt_topic + "/#")

def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))
    
    try:
        # Decode the byte string to a regular string
        payload = msg.payload.decode("utf-8").strip()
        
        # Now, we parse the decoded string into a dictionary (JSON object)
        data = json.loads(payload)  # Convert string to dictionary
        
        # Access the 'motion' key correctly
        motion = data.get("motion", "unknown_motion")  # Default to "unknown_motion" if not present
        
        # Print and update the system status based on 'motion'
        if motion == "NOT SAFE":
            print("The system is NOT SAFE!")
            send_telegram_alert("Alert! The system is NOT SAFE.")
        else:
            print("The system is SAFE.")

        # Insert the alert record into MongoDB
        status_collection.insert_one({"motion": motion, "timestamp": datetime.now()})
        
        # Send data to Flask API (optional, if you have a Flask app to handle this)
        # flask_url = os.getenv("REST_STATUS_URI", "http://rest_app:5000/api/status")
        # try:
        #     resp = requests.post(flask_url, json={"motion": motion})
        #     if resp.status_code == 200:
        #         print("Data sent to Flask API successfully.")
        #     else:
        #         print(f"Status code: {resp.status_code}, Response: {resp.text}")

        # except requests.RequestException as e:
        #     print("Error sending data to Flask API:", e)

    except json.JSONDecodeError:
        print(f"Error processing MQTT message: Invalid JSON -> {msg.payload}")
    except Exception as e:
        print(f"Error processing MQTT message: {e}")

# Initialize MQTT client
mqttc = mqtt.Client()
mqttc.on_connect = on_connect
mqttc.on_message = on_message

try:
    mqttc.connect(mqtt_broker, mqtt_port, 60)
    mqttc.loop_forever()
except Exception as e:
    print("MQTT Connection Error:", e)
    sys.exit(1)
