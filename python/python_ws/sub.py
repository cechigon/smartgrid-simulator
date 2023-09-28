#!usr/bin/env python
# -*- coding: utf-8 -*- 

import paho.mqtt.client as mqtt
import random

def on_connect(client, userdata, flag, rc):
  print("Connected with result code " + str(rc)) 
  client.subscribe("car/+/input-power")
  client.subscribe("car/+/output-power")


def on_disconnect(client, userdata, rc):
  if  rc != 0:
    print("Unexpected disconnection.")


def on_message(client, userdata, msg):
  print("Received message '" + str(msg.payload) + "' on topic '" + msg.topic + "' with QoS " + str(msg.qos))


client_id = f'python-mqtt-{random.randint(0, 1000)}'
client = mqtt.Client(client_id)
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message
 
client.connect("shiftrio", 1883, 60) 
 
client.loop_forever()