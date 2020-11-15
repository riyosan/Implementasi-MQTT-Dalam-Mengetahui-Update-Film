import requests# untuk melakukan panggilan API TheMovieDB
import paho.mqtt.client as mqtt#library paho untuk koneksi MQTT

def on_connect_sub(client, userdata, flags, rc):#fungsi untuk subscribe ke MQTT broker
    print("Subscriber connected with result code "+str(rc))

    client.subscribe("judul01")
    client.subscribe("tanggalrilis02")
    client.subscribe("popularity03")
    client.subscribe("skip04")
    #topik subscriber
def on_message_sub(client, userdata, msg):#ketika pesan telah diterima
    print("film yang akan keluar: "+msg.topic+" "+msg.topic+" "+str(msg.payload))


sub = mqtt.Client()
sub.on_connect = on_connect_sub
sub.on_message = on_message_sub #ketika sebuah pesan diterima

sub.connect("mqtt.eclipse.org", 1883, 60)#broker dan port
while True:
    sub.loop_forever()
