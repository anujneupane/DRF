import requests
import json

url = "http://127.0.0.1:8000/crd/"

def get_data(id = None):
 data = {}
 if id is not None:
   data = {'id':id}
 json_data =  json.dumps(data) 
 headers = {'content-Type': 'application/json'}
 r = requests.get(url = url,headers=headers,data=json_data)
 data = r.json()
 print(data)
 
# get_data()

def post_data():
  data ={
    'name': 'geet',
    'roll': 11,
    'city': 'balkumari'

  }
  
  headers = {'content-Type': 'application/json'}
  json_data = json.dumps(data)
  r = requests.post(url = url, headers=headers,data=json_data)
  data = r.json()
  print(data)

# post_data()

def update():
  data ={
    'id':4,
    'name': 'Gita',
    'city': 'butwal'
  }
  headers = {'content-Type': 'application/json'}
  json_data = json.dumps(data)
  r = requests.put(url = url,headers=headers,data=json_data)
  data = r.json()
  print(data)

#update()

def delete():
  data = {
    'id': 3
  }
  headers = {'content-Type': 'application/json'}
  json_data = json.dumps(data)
  r = requests.delete(url = url,headers=headers,data=json_data)
  data = r.json()
  print(data)
  
delete()  