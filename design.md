# System Design

Architecture:
Sensors -> Ingestion -> Data Lake -> Memory Graph -> MEN Model -> API -> App

Key Technologies:
- AWS
- Python
- Graph DB
- Deep Learning
  # JeevaSankalpa – System Design

## 1. Overview
**JeevaSankalpa** is a disaster-resilient emergency alert and response system designed to function even during **network outages**. It combines IoT wearables/tags, edge devices, and long-range communication to deliver **early warnings**, **location tracking**, and **critical alerts**.

## 2. Objectives
- Provide alerts without dependency on cellular/Wi‑Fi
- Enable real-time disaster warnings
- Support victim identification & tracking
- Ensure low-power & scalable deployment

## 3. High-Level Architecture
Sensors/Tags → Edge Gateway → Long‑Range Communication → Command Center / Cloud

## 4. Components
### • Smart Emergency Tag
- Low-power microcontroller
- GPS / BLE / LoRa module
- SOS trigger button

### • Edge Gateway
- Aggregates nearby tag/sensor data
- Performs local decision-making
- Relays alerts via LoRa / Mesh / Satellite

### • Communication Layer
- LoRa / LoRaWAN
- Mesh networking
- Optional satellite fallback

### • Command & Control Center
- Receives alerts
- Visualizes disaster & victim data
- Triggers response workflow

## 5. Novelty
Unlike conventional systems, JeevaSankalpa:
- Works **offline-first**
- Uses **multi-layer communication fallback**
- Prioritizes **low-cost deployability for developing regions**

## 6. Scalability
Supports deployment across campuses, cities, and disaster-prone zones.

## 7. Security
- Encrypted communication
- Secure device identity
- Tamper resistance

## 8. Future Enhancements
- AI-based anomaly prediction
- Integration with government disaster APIs
- Drone-assisted relay nodes
