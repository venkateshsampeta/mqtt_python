# MQTT Communication Test Using Python

## 📌 Project Overview

This project demonstrates **MQTT (Message Queuing Telemetry Transport)** communication using Python.

The project simulates an IoT device and a cloud/application using two Python programs:

* **Publisher** – Simulates an IoT device and publishes data.
* **Subscriber** – Simulates a cloud application and receives the data.
* **MQTT Broker** – Acts as an intermediate communication server between the publisher and subscriber.

An ESP32 or other hardware device is **not required** for this test. The complete MQTT communication can be tested on a PC using Python.

---

## 🏗️ System Architecture

```text
              Python Publisher
             (IoT Device)
                   |
                   | MQTT
                   ↓
             MQTT Broker
                   |
                   | MQTT
                   ↓
            Python Subscriber
          (Cloud/Application)
```

### Communication Flow

```text
Publisher
    ↓
Publish MQTT Message
    ↓
MQTT Broker
    ↓
Route Message Using Topic
    ↓
Subscriber
    ↓
Receive and Process Message
```

---

## 🎯 Objectives

The main objectives of this project are:

* Understand the basic MQTT communication model.
* Implement an MQTT publisher using Python.
* Implement an MQTT subscriber using Python.
* Understand MQTT topics and payloads.
* Understand MQTT Quality of Service (QoS).
* Verify communication between publisher and subscriber.
* Simulate IoT device-to-cloud communication without hardware.

---

## 🛠️ Technologies Used

| Technology  | Purpose                 |
| ----------- | ----------------------- |
| Python      | Application development |
| Paho MQTT   | MQTT client library     |
| MQTT        | IoT messaging protocol  |
| MQTT Broker | Message routing         |
| JSON        | Structured data format  |

---

## 📦 Required Software

### Python

Python 3.x is required.

Check the installed Python version:

```bash
python --version
```

or:

```bash
python3 --version
```

---

## 📥 Install Paho MQTT

Install the Python MQTT client library:

```bash
pip install paho-mqtt
```

Verify the installation:

```bash
pip show paho-mqtt
```

---

# 📤 MQTT Publisher

The publisher simulates an IoT device.

It connects to the MQTT broker and publishes messages to a specific topic.

Example:

```text
Topic:
venkatesh/test/mqtt

Payload:
Hello MQTT 1
```

The publisher sends messages periodically.

---

# 📥 MQTT Subscriber

The subscriber simulates a cloud application.

It connects to the MQTT broker and subscribes to the required topic.

When a message is published to that topic, the subscriber receives it.

Example:

```text
Topic   : venkatesh/test/mqtt
Payload : Hello MQTT 1
```

---

# 🔄 MQTT Communication

MQTT uses a **publish/subscribe architecture**.

### Publisher

The publisher sends a message to a topic.

```text
Publisher
    |
    | Publish
    ↓
MQTT Broker
```

### Subscriber

The subscriber subscribes to a topic.

```text
MQTT Broker
    |
    | Message
    ↓
Subscriber
```

The publisher and subscriber do not need to communicate directly.

The MQTT broker handles the message routing.

---

# 📌 MQTT Topic

A topic is used to identify where the message should be published.

Example:

```text
venkatesh/test/mqtt
```

Publisher:

```python
client.publish("venkatesh/test/mqtt", "Hello MQTT")
```

Subscriber:

```python
client.subscribe("venkatesh/test/mqtt")
```

Both must use the same topic to communicate.

---

# 📦 MQTT Payload

The payload is the actual data being transmitted.

Example:

```text
Hello MQTT
```

For an IoT application, the payload can contain structured data.

Example JSON:

```json
{
    "voltage": 230,
    "current": 1.5,
    "uv_status": "ON"
}
```

This type of payload can be used to simulate an IoT device sending sensor/device information to the cloud.

---

# 🔐 MQTT Security

MQTT itself is a messaging protocol. Secure MQTT communication can be implemented using **TLS**.

```text
MQTT + TLS = Secure MQTT / MQTTS
```

For example:

```text
Python Device
      |
      | MQTTS
      | TLS encrypted
      ↓
MQTT Broker
```

TLS can provide:

* Encryption
* Server authentication
* Certificate-based authentication
* Protection against data interception

The current basic test uses standard MQTT for learning and communication testing.

A later version can be extended to **MQTTS using TLS**.

---

# 📊 MQTT QoS

QoS stands for **Quality of Service**.

It defines the message delivery guarantee.

### QoS 0 — At Most Once

```text
Publisher → Broker
```

No acknowledgement is required.

The message may be lost.

### QoS 1 — At Least Once

```text
Publisher → Broker
             ↓
            PUBACK
```

The message is delivered at least once, but duplicates are possible.

### QoS 2 — Exactly Once

Provides exactly-once delivery with additional communication overhead.

### Summary

| QoS | Delivery      | Overhead |
| --- | ------------- | -------- |
| 0   | At most once  | Low      |
| 1   | At least once | Medium   |
| 2   | Exactly once  | High     |

For this project, **QoS 1** can be used to demonstrate reliable message delivery.

---

# 🧪 Testing Procedure

## Step 1 — Start the Subscriber

Open Terminal 1:

```bash
python subscriber.py
```

Expected output:

```text
Connected to MQTT broker
Subscribed to: venkatesh/test/mqtt
```

Keep the subscriber running.

---

## Step 2 — Start the Publisher

Open Terminal 2:

```bash
python publisher.py
```

Expected output:

```text
Published: Hello MQTT 1
Published: Hello MQTT 2
Published: Hello MQTT 3
Published: Hello MQTT 4
Published: Hello MQTT 5
```

---

## Step 3 — Verify Subscriber

The subscriber should display:

```text
Message received!
Topic   : venkatesh/test/mqtt
Payload : Hello MQTT 1

Message received!
Topic   : venkatesh/test/mqtt
Payload : Hello MQTT 2

Message received!
Topic   : venkatesh/test/mqtt
Payload : Hello MQTT 3
```

If the publisher messages are received by the subscriber, the MQTT communication is working correctly.

---

# 🧪 IoT Data Simulation

Instead of sending simple text, the publisher can simulate data from an IoT device.

Example:

```json
{
    "device_id": "UV_PURIFIER_01",
    "voltage": 230.0,
    "current": 1.5,
    "uv_status": "ON",
    "device_status": "RUNNING"
}
```

The Python publisher can periodically publish this data.

This simulates:

```text
IoT Device
    ↓
Sensor Data
    ↓
MQTT
    ↓
MQTT Broker
    ↓
Cloud Application
```

---

# 🌐 Application to UV Air Purifier IoT System

This MQTT test can be used as a software simulation of the communication architecture used in an IoT device such as a UV Air Purifier.

Example architecture:

```text
                 UV AIR PURIFIER
                       |
                    Wi-Fi
                       |
                    MQTTS
                       |
                       ↓
                MQTT Broker
                       |
                       ↓
                Cloud Platform
```

The device can publish:

* Voltage
* Current
* Device status
* UV status
* Fault status
* Other monitored parameters

The cloud can also publish commands to the device using MQTT topics.

---

# 🔁 Device-to-Cloud Communication

```text
Device
   |
   | Publish
   ↓
MQTT Broker
   |
   ↓
Cloud Application
```

Example:

```text
Topic:
uv_purifier/device01/status
```

Payload:

```json
{
    "voltage": 230,
    "current": 1.5,
    "status": "RUNNING"
}
```

---

# ☁️ Cloud-to-Device Communication

MQTT also supports communication in the opposite direction.

```text
Cloud Application
       |
       | Publish command
       ↓
  MQTT Broker
       |
       ↓
      Device
```

Example:

```text
Topic:
uv_purifier/device01/command
```

Payload:

```json
{
    "command": "START_UV"
}
```

The device subscribes to the command topic and processes the received command.

---

# ⚠️ Troubleshooting

## Connection Failed

Check:

* Internet connection
* MQTT broker address
* MQTT port
* Firewall settings
* Topic name

Example:

```text
Broker: test.mosquitto.org
Port: 1883
```

---

## Subscriber Not Receiving Messages

Check that:

1. Publisher and subscriber use the same broker.
2. Publisher and subscriber use the same topic.
3. Subscriber is connected before publishing.
4. Internet connection is available.
5. The MQTT broker is reachable.

---

# 🔍 Important MQTT Terms

| Term       | Description                        |
| ---------- | ---------------------------------- |
| MQTT       | Lightweight IoT messaging protocol |
| Broker     | Server that routes MQTT messages   |
| Publisher  | Client that sends messages         |
| Subscriber | Client that receives messages      |
| Topic      | Address/channel used for messages  |
| Payload    | Actual message/data                |
| QoS        | Message delivery guarantee         |
| MQTTS      | MQTT secured using TLS             |
| TLS        | Security/encryption protocol       |

---

# 🚀 Future Improvements

The project can be extended with:

* MQTTS using TLS
* Username/password authentication
* Client certificates
* JSON-based sensor data
* MQTT retained messages
* Last Will and Testament (LWT)
* Automatic reconnection
* Multiple IoT devices
* Device command handling
* Cloud database integration
* OTA firmware update simulation

---

# 📚 Learning Outcomes

Through this project, the following concepts are demonstrated:

* MQTT publish/subscribe architecture
* MQTT broker communication
* MQTT topics
* MQTT payloads
* MQTT QoS
* Python MQTT client programming
* IoT device-to-cloud communication
* Secure MQTT using TLS
* Basic IoT data simulation

---

## Author

**Venkatesh Sampeta**

Embedded Software Engineer

Focus Areas:

* Embedded C
* STM32
* ESP32
* IoT
* MQTT / MQTTS
* CAN / K-Line
* Firmware Development
* OTA / Bootloader
