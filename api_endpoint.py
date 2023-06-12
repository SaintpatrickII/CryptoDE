#%%
from ensurepip import bootstrap
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from json import dumps
from kafka import KafkaProducer, KafkaAdminClient
from kafka.admin import NewTopic

app = FastAPI()


admin_client = KafkaAdminClient(
    bootstrap_servers='localhost:9092',
    client_id='KafkatoPython'
)


topic_list = []
topic_list.append(NewTopic(name='coin_list', num_partitions=3, replication_factor=1))
admin_client.create_topics(new_topics=topic_list)
admin_client.list_topics()
#%%

producer = KafkaProducer(
    bootstrap_servers='localhost:9092'
    value_serializer= lambda u = dumps(u).encode('ascii')
)

class coin_data(BaseModel):
     id: int
     name: str
     symbol: str 
     max_supply: int
     circulating_supply: int
     self_reported_market_cap: str


@app.post('/coins/')
def get_coins(item: coin_data):
    data = dict(item)
    producer.send('coin_data', data)

if __name__ == '__main__':
    uvicorn.run('coin_project_API:app', host ='localhost', port=2077)