import requests
import json

url = "http://127.0.0.1:8000/crd/"

def get_data(id = None):
 data = {}
 if id is not None:
   data = {'id':id}
 json_data =  json.dumps(data) 
 r = requests.get(url = url,data=json_data)
 data = r.json()
 print(data)

get_data(1)

def post_data():
  data ={
    'name': 'pawan',
    'roll': 3,
    'city': 'btwl'

  }
  json_data = json.dumps(data)
  r = requests.post(url = url,data=json_data)
  data = r.json()
  print(data)

post_data()

def update():
  data ={
    'id':1,
    'name': 'Devi_Mata',
    'city': 'butwal'
  }

  json_data = json.dumps(data)
  r = requests.put(url = url,data=json_data)
  data = r.json()
  print(data)

update()


