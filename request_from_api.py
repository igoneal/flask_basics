import requests
import json

url = 'http://127.0.0.1:5000/'


def get_data(endpoint=''):
    response = requests.get(url+endpoint)
    # print(response.__dict__)
    data = json.loads(response.content)
    print(data)


def post_data(data, endpoint=''):
    # response = requests.post(url+endpoint, data='mama', json=data)
    response = requests.post(url + endpoint, json=data)
    # print(response.__dict__)
    data = json.loads(response.content)
    print(data)


get_data(endpoint='times5/12')
get_data(endpoint='')
get_data(endpoint='multiply/7,8')
post_data(data={'name': 'emeka'})
