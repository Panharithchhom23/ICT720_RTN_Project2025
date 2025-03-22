#include <Arduino.h>
#include <M5StickC.h>
#include <WiFi.h>
#include <WiFiClient.h>
#include <PubSubClient.h>
#include <ArduinoJson.h>

// PIR Sensor Pin
#define PIR_PIN 36  

// Wi-Fi Credentials
#define WIFI_SSID "Nan"
#define WIFI_PASSWD "Yuna2003"

// MQTT Settings
#define MQTT_SERVER "192.168.137.1"
#define MQTT_PORT 1883
#define MQTT_TOPIC "safety/alert"
#define MQTT_CLIENT_ID "Puncharus_device"

WiFiClient espClient;
PubSubClient mqtt_client(espClient);
JsonDocument doc;  

// Variable to track motion state
int lastMotionState = LOW;
int currentMotionState = LOW;

void connectWiFi() {
  Serial.print("Connecting to WiFi...");
  WiFi.begin(WIFI_SSID, WIFI_PASSWD);
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(1000);
  }
  Serial.println("\nWiFi connected!");
  Serial.printf("IP Address: %s\n", WiFi.localIP().toString().c_str());
}

void connectMQTT() {
  while (!mqtt_client.connected()) {
    Serial.print("Connecting to MQTT...");
    if (mqtt_client.connect(MQTT_CLIENT_ID)) {
      Serial.println("Connected!");
      mqtt_client.subscribe(MQTT_TOPIC);  // Subscribe to topic if needed
    } else {
      Serial.print("Failed, rc=");
      Serial.print(mqtt_client.state());
      Serial.println(" retrying in 5 seconds...");
      delay(5000);
    }
  }
}

void setup() {
  delay(3000);  // Wait a moment for system startup

  M5.begin();
  Serial.begin(115200);
  
  pinMode(PIR_PIN, INPUT);
  
  M5.Lcd.setRotation(3);
  M5.Lcd.fillScreen(GREEN);
  M5.Lcd.setTextColor(BLACK);
  M5.Lcd.setTextSize(2);
  M5.Lcd.setCursor(20, 40);
  M5.Lcd.print("SAFE");

  connectWiFi();
  mqtt_client.setServer(MQTT_SERVER, MQTT_PORT);
  connectMQTT();
}

// Time between motion state changes in milliseconds
#define DEBOUNCE_TIME 3000  

// Variable to store the last time motion state changed
unsigned long lastMotionChangeTime = 0;

void loop() {
  if (!mqtt_client.connected()) {
    connectMQTT();
  }
  mqtt_client.loop();  // Ensure MQTT stays connected

  currentMotionState = digitalRead(PIR_PIN);  // Read the PIR sensor state
  unsigned long currentMillis = millis();

  // Check if motion state has changed (debounce)
  if (currentMotionState != lastMotionState && (currentMillis - lastMotionChangeTime >= DEBOUNCE_TIME)) {
    lastMotionChangeTime = currentMillis;  // Update debounce time
    String motionStatus = (currentMotionState == HIGH) ? "NOT SAFE" : "SAFE";
    
    // Print the current motion state to the Serial Monitor
    Serial.print("Motion State: ");
    Serial.println(motionStatus);

    // Prepare the JSON payload
    char payload[200];
    doc.clear();
    doc["millis"] = currentMillis;
    doc["mac"] = WiFi.macAddress().c_str();
    doc["rssi"] = WiFi.RSSI();
    doc["ip"] = WiFi.localIP().toString().c_str();
    doc["motion"] = motionStatus.c_str();  // "SAFE" or "NOT SAFE"
    serializeJson(doc, payload);
    mqtt_client.publish(MQTT_TOPIC, payload);  // Publish to MQTT broker

    // Update LCD based on motion state
    if (currentMotionState == HIGH) {
      M5.Lcd.fillScreen(RED);  // Not safe, motion detected
      M5.Lcd.setCursor(20, 40);
      M5.Lcd.setTextColor(WHITE);
      M5.Lcd.print("NOT SAFE");
    } else {
      M5.Lcd.fillScreen(GREEN);  // Safe, no motion detected
      M5.Lcd.setCursor(20, 40);
      M5.Lcd.setTextColor(BLACK);
      M5.Lcd.print("SAFE");
    }

    lastMotionState = currentMotionState;  // Update last motion state
  }

  delay(100);  // Small delay to avoid flooding the MQTT server
}
