#!usr/bin/env python
# -*- coding: utf-8 -*-

import paho.mqtt.client as mqtt
from time import sleep
import random

def on_connect(client, userdata, flag, rc):
    print("Connected with result code " + str(rc))


def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpected disconnection.")


def on_publish(client, userdata, mid):
    print("publish: {0}".format(mid))


def main():
    client_id = f'python-mqtt-{random.randint(0, 1000)}'
    client = mqtt.Client(client_id)        # クラスのインスタンス(実体)の作成
    client.on_connect = on_connect         # 接続時のコールバック関数を登録
    client.on_disconnect = on_disconnect   # 切断時のコールバックを登録
    client.on_publish = on_publish         # メッセージ送信時のコールバック

    client.connect("shiftrio", 1883, 60)  # 接続先は自分自身

    client.loop_start()

    # 永久に繰り返す
    while True:
        client.publish("msg", "Hello!")
        sleep(0.5)
        client.publish("foge", "Hello!")
        sleep(0.5)

if __name__ == '__main__':
    main()