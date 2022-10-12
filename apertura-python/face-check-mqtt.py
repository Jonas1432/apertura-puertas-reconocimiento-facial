#Bibliotecas
import json, random, time, argparse
from paho.mqtt import client as mqtt_client
from deepface import DeepFace
import pandas as pd

#Parser
parser = argparse.ArgumentParser()
parser.add_argument ("img_src", help="Imagen a buscar en la BD de caras")
parser.add_argument ("db_path", help="Ruta de la base de datos de caras")
args = parser.parse_args()

#Datos del broker
broker = '127.0.0.1'
port = 1883
topic = "codigoIoT/mqtt/python"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'
# username = 'emqx'
# password = 'public'

#Conexión
def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    #client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

#Funciones
def publicarSinWhile(client, mensaje):
    time.sleep(1)
    msg = mensaje
    result = client.publish(topic, msg)
    time.sleep(1)
    print(result)
    status = result[0]
    if status == 0:
        print(f"Send `{msg}` to topic `{topic}`")
    else:
        print(f"Failed to send message to topic {topic}")

#Buscar rostro
df = DeepFace.find (img_path = args.img_src, db_path = args.db_path, enforce_detection = "false")
print ("Resultado ")
print (df)
json_view = df.to_json(orient="index")
print("La expresion en JSON de los resultados es: ")

#Envio
client = connect_mqtt()
client.loop_start()
publicarSinWhile(client, json_view)