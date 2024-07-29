from confluent_kafka import Consumer
from elasticsearch import Elasticsearch
import json

################

c = Consumer({'bootstrap.servers': 'localhost:9092', 'group.id': 'python-consumer', 'auto.offset.reset': 'earliest'})
es = Elasticsearch(
    hosts=[{'host': 'localhost', 'port': 9200, 'scheme': 'http'}],
    headers={'Content-Type': 'application/json'}
)

print('Available topics to consume: ', c.list_topics().topics)

c.subscribe(['user-tracker'])

################

def main():
    while True:
        msg = c.poll(1.0)  # timeout
        if msg is None:
            continue
        if msg.error():
            print('Error: {}'.format(msg.error()))
            continue
        data = msg.value().decode('utf-8')
        print(data)

#         data2 = {
#         'user_id': 45235,
#         'user_name': 'John Doe',
#         'user_address': '1234 Elm Street | Springfield | US',
#         'platform': 'Mobile',
#         'signup_at': '2024-07-22T14:48:00'
# }
        
        # Index data into Elasticsearch
        es.index(index='user-tracker', body=data)

    c.close()

if __name__ == '__main__':
    main()
