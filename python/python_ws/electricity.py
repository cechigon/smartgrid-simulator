import paho.mqtt.client as mqtt
from time import sleep
import pandas as pd
import random
import json

json_data = None

def on_connect(client, userdata, flag, rc):
    print("Connected with result code " + str(rc))


def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpected disconnection.")


def on_publish(client, userdata, mid):
    # print("publish: {0}".format(mid))
    pass


def get_forecast():
    global json_data

    df = pd.read_csv("https://www.tepco.co.jp/forecast/html/images/juyo-d1-j.csv", encoding="shift-jis", skiprows=14, nrows=24, header=None)

    for i, forecast in df.iterrows():

        if pd.isnull(forecast[4]):

            forecast_data = {
                "date": input[0],
                "time": input[1],
                "use": input[2],
                "prediction": input[3],
                "use_rate": input[4],
                "supply": input[5]
            }

            json_data = json.dumps(forecast_data)

            print(json_data)

            break
        else:
            input = forecast

def main():
    client_id = f'python-mqtt-{random.randint(0, 1000)}'
    client = mqtt.Client(client_id)
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_publish = on_publish

    client.connect("shiftrio", 1883, 60)

    client.loop_start()

    get_forecast()

    while True:
        client.publish("forecast", json_data)
        sleep(0.5)


if __name__ == '__main__':
    main()