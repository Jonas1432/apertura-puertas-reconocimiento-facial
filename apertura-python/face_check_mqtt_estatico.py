#Bibliotecas
import json
import random
import time
from paho.mqtt import client as mqtt_client
from deepface import DeepFace
import pandas as pd

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
df = DeepFace.find (img_path = "/home/jonathan/apertura-puertas-reconocimiento-facial/DeepFace/Fotos/foto1.png", db_path = "/home/jonathan/apertura-puertas-reconocimiento-facial/DeepFace/my_db", enforce_detection = "false")
print ("Resultado ")
print (df)
print ("Seleccion")
print (df.identity[0])

#Conexión con el Broker
print("Conectandose al Broker")
client = connect_mqtt()
client.loop_start()
print("Enviando datos")
publicarSinWhile(client, df.identity[0])
print("Mensaje enviado")