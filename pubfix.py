import requests # untuk melakukan panggilan API TheMovieDB
import paho.mqtt.client as mqtt #library paho untuk koneksi MQTT
import json#library json
def on_publish(pub, userdata, message):# Dipanggil ketika pesan telah dikirim
    print("film: ")
pub = mqtt.Client() #constructor
pub.on_publish = on_publish
pub.connect("mqtt.eclipse.org", 1883, 60)#broker dan port
print("Jalankan pub")
requ = requests.get("https://api.themoviedb.org/3/movie/upcoming?api_key=baca93b3263855251ecbd8813e4188df&language=en-US&page=1")#mengambil data API
data = requ.json()#memilih data
film = data["results"]
skip = "#########################################################"
print("Publisher mengirim pesan")


for i in film:
      
      pub.publish("judul01", i["title"])
      pub.publish("tanggalrilis02", i["release_date"])
      pub.publish("popularity03", i["popularity"])
      pub.publish("skip04", str(skip))
#mengirim data ke broker
