#include <Arduino.h>
#include <M5StickC.h>
#include <Wire.h>
#include <WiFiClient.h>
#include <PubSubClient.h>
#include <ArduinoJson.h>
#include "utility/NetworkModule.h"
#include "utility/PowerModule.h"

// Define PIR sensor pin
#define PIR_PIN 36  

// MQTT Configuration
#define MQTT_SERVER "your_mqtt_broker_ip"
#define MQTT_PORT 1883
#define MQTT_TOPIC "safety/alert"

// Wi-Fi Configuration
const char* ssid = "your_wifi_ssid";
const char* password = "your_wifi_password";

// MQTT & Network Modules
WiFiClient espClient;
PubSubClient mqtt_client(espClient);
NetworkModule network_module;
PowerModule power_module;
JsonDocument doc;

void setup() {
    M5.begin();
    Serial.begin(115200);

    pinMode(PIR_PIN, INPUT);  // Set PIR sensor pin as input
    
    M5.Lcd.setRotation(3);
    M5.Lcd.fillScreen(GREEN);
    M5.Lcd.setTextColor(BLACK);
    M5.Lcd.setTextSize(2);
    M5.Lcd.setCursor(20, 40);
    M5.Lcd.print("SAFE");

    // Connect to Wi-Fi
    network_module.connect();
    
    // Setup MQTT
    mqtt_client.setServer(MQTT_SERVER, MQTT_PORT);
    mqtt_client.connect("M5StickC");
}

void loop() {
    if (!mqtt_client.connected()) {
        mqtt_client.connect("M5StickC");
    }

    int motion = digitalRead(PIR_PIN);
    if (motion == HIGH) {
        mqtt_client.publish(MQTT_TOPIC, "not_safe");
        M5.Lcd.fillScreen(RED);
        M5.Lcd.setCursor(20, 40);
        M5.Lcd.print("NOT SAFE");
    } else {
        mqtt_client.publish(MQTT_TOPIC, "safe");
        M5.Lcd.fillScreen(GREEN);
        M5.Lcd.setCursor(20, 40);
        M5.Lcd.print("SAFE");
    }

    mqtt_client.loop();
    delay(1000);
}
