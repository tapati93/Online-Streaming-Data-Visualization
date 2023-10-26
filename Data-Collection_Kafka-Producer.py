from tmdbv3api import TMDb
import requests
import json
from tmdbv3api import Movie
from kafka import KafkaProducer
from json import dumps
from time import sleep
from kafka import KafkaConsumer


producer = KafkaProducer(
 bootstrap_servers='kafka-main-service-brianfernandes1493-a113.aivencloud.com:10428',
 security_protocol="SSL",
 ssl_cafile="./ca.pem",
 ssl_certfile="./service.cert",
 ssl_keyfile="./service.key",
 #value_serializer=lambda v: json.dumps(v).encode('ascii')
 value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

#print(producer)


pageLimit = 200

for i in range(1, pageLimit+1):
  url1 = f'https://api.themoviedb.org/3/movie/top_rated?api_key=cb5139c390a37b18506ff7ec44c1ad8a&language=en-US&page={i}'
  r = requests.get(url1)
  myData = json.loads(r.text)

  for movieRecord in myData['results']:
      producer.send(
          'MovieData',
          #value= rate_list
          # #value = myData['results']
          value = movieRecord
          )
      producer.flush()
    
      print(movieRecord)



































# count = 0
# for item in myData['results']:
#     if count < 5:
#         producer.send(
#             'MovieData',
#             #value= rate_list
#             #value = myData['results']
#             value = item
#             )
#         producer.flush()    
#     count += 1



# consumer = KafkaConsumer(
#  bootstrap_servers='kafka-371fd745-brianfernandes1493-a113.aivencloud.com:10428',
#  security_protocol="SSL",
#  ssl_cafile="./ca.pem",
#  ssl_certfile="./service.cert",
#  ssl_keyfile="./service.key",
#  value_deserializer = lambda v: json.loads(v.decode('utf-8')),
#  auto_offset_reset='earliest'
# )


# consumer.subscribe(topics='MovieData')

# for message in consumer:
#   print ("%d:%d: v=%s" % (message.partition,
#                           message.offset,
#                           message.value))

