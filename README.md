# ICT720_RTN_Project_2025

## Group Member:                           
1. Puncharus Phongphitthongchai         ID: 6714552246
2. Panharith Chhom                      ID: 6722040760
3. Piyapach Singto                      ID: 6722040323

## Topic: Automatic Alert System for Workplace Safety  
Workplace safety is a critical concern in industrial environments where heavy machinery poses risks to workers. Ensuring a safe workspace requires proactive measures to detect potential hazards and alert workers before accidents occur. This project introduces an automated safety system that utilizes a Passive Infrared Sensor (PIR) to monitor movement around a machine’s safety guard. By providing real-time visual alerts and monitoring capabilities, the system aims to enhance workplace safety and reduce injury risks.

![image](https://github.com/user-attachments/assets/1444af24-c048-4244-a92a-c2dabd568507)



## Objective
This project aims to enhance workplace safety by integrating a Passive Infrared Sensor (PIR) motion sensor with a machine’s safety guard. If a worker enters the hazardous area, the system will trigger an LED alert, notifying both the worker and safety personnel. This proactive warning system helps prevent accidents by ensuring that workers remain aware of their proximity to dangerous zones. 

## Stakeholder
- Worker         : Employees who operate or work near the machine and are at risk of entering hazardous areas.
- Supervisor     : Responsible for overseeing machine operations and ensuring workplace safety compliance.
- Safety Officer : Monitors the overall safety system and responds to potential hazards or false alarms.
   
## User Stories (US)
- US1: As a worker, I want the alert to turn on automatically when I enter a dangerous zone so that I can avoid accidents.
- US2: As a supervisor, I want a visual indicator to show when the machine is stopped so that I can quickly identify the issue.
- US3: As a safety officer, I want to monitor the machine in case of false trigger, so that I know whether the machine ready or not.

## Features
- Motion Detection: The PIR sensor detects motion in the hazardous zone around the machine.
- Visual Alert System: An LED indicator turns RED and show word "NOT SAFE" when motion is detected in the hazardous zone and LED screen turns GREEN and show word "SAFE" when motion is not detected.
- Real-Time Monitoring: The system provides real-time data to safety officers for monitoring and analysis.

## Software Models

### System Diagram 
![image](https://github.com/user-attachments/assets/3ea5552b-59f4-4dc1-af64-419a87b9fac3)


The system consists of multiple interconnected components that work together to detect motion and provide alerts. The key components include:

- PIR Sensor (Motion Detection): Detects movement in the hazardous zone and sends a signal to the ESP32-S3.
- Hazardous Zone (Safety Guard): The monitored area where worker movement is tracked to prevent accidents.
- M5 Sticks (Data Processing): Processes motion data received from the ESP32-S3 and determines whether an alert should be triggered.
- LED Alert (Visual Alert): A high-intensity LED that turns on when motion is detected, providing an immediate visual warning to workers and supervisors.
- WiFi (Network Communication): Enables wireless connectivity for remote monitoring and alert notifications.
- Telegram Alert: Sends a notification via Telegram to the safety manager for real-time hazard awareness.
- Safety Manager: Receives alerts through Telegram and takes necessary action to ensure workplace safety.



### Hardware

# 1. M5StickC
![image](https://github.com/user-attachments/assets/7f0985f2-6643-460d-b90f-8aaab5665339)

M5StickC is a mini M5Stack, powered by ESP32. It is a portable, easy-to-use, open source, IoT development board. What it can do? This tiny block is able to realize your idea, enlighten your creativity, and help with your IoT prototyping in a very short time. It will take away a lot of pains from the development process.M5stickC is one of the core devices in M5Stack product series.

Link:  https://shop.m5stack.com/products/stick-c?variant=43982750843137
    
# 2. M5StickC PIR Hat
![image](https://github.com/user-attachments/assets/5fd6d676-ee6e-4539-bf4b-e3fe0b94dc2f)

PIR HAT is a human body infrared sensor compatible with M5SticKC. It is a passive infrared detector that detects infrared radiation emitted or reflected by a human body or objects. When it detects infrared radiation, it outputs a high level signal and initiates a delay for a certain period of time (during which it maintains a high level and allows for repeated triggering) until the triggering signal disappears (returns to a low level). 

Link: https://docs.m5stack.com/en/hat/hat-pir

### Data Modeling
![image](https://github.com/user-attachments/assets/fefe4e16-a9e2-462b-9caf-dbe8ebac99f6)


## Monitoring Alert
https://github.com/user-attachments/assets/fcb31c3b-0d83-4a74-b675-5f2fbc80f5de

![Screenshot 2025-03-25 165854](https://github.com/user-attachments/assets/938cb2b8-38c1-4703-9471-f6cf29da2572)

### Telegram Notification
![image](https://github.com/user-attachments/assets/9b5e1f3b-6392-4d6b-8ca6-88d50f97e9e5) 








