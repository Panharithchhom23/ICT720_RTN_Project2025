# ICT720_RTN_Project_2025

## Group Member:                           
![image](https://github.com/user-attachments/assets/8915c331-8ed8-48f0-a2b3-235a03791f00)


## Topic: Automatic Alert System for Workplace Safety  
Workplace safety is a critical concern in industrial environments where heavy machinery poses risks to workers. Ensuring a safe workspace requires proactive measures to detect potential hazards and alert workers before accidents occur. This project introduces an automated safety system that utilizes a Passive Infrared Sensor (PIR) to monitor movement around a machine’s safety guard. By providing real-time visual alerts and monitoring capabilities, the system aims to enhance workplace safety and reduce injury risks.

![image](https://github.com/user-attachments/assets/1444af24-c048-4244-a92a-c2dabd568507)



## Objective
This project aims to enhance workplace safety by integrating a Passive Infrared Sensor (PIR) motion sensor with a machine’s safety guard. If a worker enters the hazardous area, the system will send an alert to the worker and notify the supervisor and safety officer through the Telegram bot app. This proactive warning system helps prevent accidents by ensuring that workers remain aware of their proximity to dangerous zones.

## Stakeholder
- Worker         : Employees who operate or work near the machine and are at risk of entering hazardous areas.
- Supervisor     : Responsible for overseeing machine operations and ensuring workplace safety compliance.
- Safety Officer : Monitors the overall safety system and responds to potential hazards or false alarms.
   
## User Stories (US)
## User Story 1 "As a woker"
As a worker, I want the alert to turn on automatically when I enter a dangerous zone so that I can avoid accidents.
- Acceptance Critiria: When the worker enter a dangerous zone, the sensor detect and then the visual indicator will change the state from green "Safe" to red "Not Safe".
## User Story 2 "As a Supervisor" 
As a supervisor, I want to ensure my worker's safety and want a visual indicator to show when the machine is stopped so that I can quickly identify the issue.
- Acceptance Critiria 1: The indicator will change its state from green to red and update accordingly to show if its safe or not.
- Acceptance Critiria 2: The supervisor can watch the detection event by timestamp that being sent through telegram.
## User Story 3 "As a Safety Officer"
As a safety officer who's in charge of the whole company safey, I want to monitor the machine in case of false trigger, so that I know whether the machine ready or not. 
- Acceptance Critiria 1: The system will alert the officer and they can check the status through telegram bot app if there are any motion detected. 
- Acceptance Critiria 2: The safety officer can review the detection history of the timestamps of the machine.

## Features
- Motion Detection: The PIR sensor detects motion in the hazardous zone around the machine.
- Visual Alert System: An LCD indicator turns RED and show word "NOT SAFE" when motion is detected in the hazardous zone and LCD screen turns GREEN and show word "SAFE" when motion is not detected.
- Real-Time Monitoring: The system provides real-time data to safety officers for monitoring and analysis.

## Software Models
### System sequence
![RTNsequence](https://github.com/user-attachments/assets/dd77087e-70ce-47b0-8862-6b0a0376bc90)
![diagram-export-26-3-2568-10_28_51](https://github.com/user-attachments/assets/382d2757-a5b7-4ffd-97cc-876b0cd32fc3)
![diagram-export-26-3-2568-10_26_47](https://github.com/user-attachments/assets/2e6aa642-d419-47ca-9fb1-3e12325182eb)

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

### State Diagram
![RTNdiagram](https://github.com/user-attachments/assets/6f1ede64-35ee-46eb-bc7b-9f29360c616d)

### Hardware

# 1. M5StickC
![image](https://github.com/user-attachments/assets/7f0985f2-6643-460d-b90f-8aaab5665339)

M5StickC is a mini M5Stack, powered by ESP32. It is a portable, easy-to-use, open source, IoT development board. What it can do? This tiny block is able to realize your idea, enlighten your creativity, and help with your IoT prototyping in a very short time. It will take away a lot of pains from the development process.M5stickC is one of the core devices in M5Stack product series.

Link:  https://shop.m5stack.com/products/stick-c?variant=43982750843137
    
# 2. M5StickC PIR Hat
![image](https://github.com/user-attachments/assets/5fd6d676-ee6e-4539-bf4b-e3fe0b94dc2f)

PIR HAT is a human body infrared sensor compatible with M5SticKC. It is a passive infrared detector that detects infrared radiation emitted or reflected by a human body or objects. When it detects infrared radiation, it outputs a high-level signal and initiates a delay for a certain period of time (during which it maintains a high level and allows for repeated triggering) until the triggering signal disappears (returns to a low level). 

Link: https://docs.m5stack.com/en/hat/hat-pir

## Data Modeling
![image](https://github.com/user-attachments/assets/8cc97575-b6e0-4d2d-b1e2-fd4e018f42a0)


## Monitoring Alert
https://github.com/user-attachments/assets/14e72c6b-53b2-45a2-b5fb-a3ebaab5bc09






![Screenshot 2025-03-25 165854](https://github.com/user-attachments/assets/938cb2b8-38c1-4703-9471-f6cf29da2572)

### Telegram Notification
![image](https://github.com/user-attachments/assets/9b5e1f3b-6392-4d6b-8ca6-88d50f97e9e5) 

## Future Plan 
- Implementing the system on the real machine where it can be turn on/off automatically when it detect motion
- The user (supervisor) can manually check and controll the machine
- Using AI models to enhacing the motion and differentiate between humans, animals, and objects to reduce false alarms.
- Using AI model to Detect unusual behavior in motion patterns and machine operation.
- Making AI to summarize the logs and suggest corrective actions.







