import requests
import json
import openwhisk

def main(dict):
    '''res = requests.get("https://172.22.254.115/api/v1/web/guest/sportInfo/games", params={'id': dict.get('id')})
    print(res.json()) 
    res_dict = json.loads(res.text)
'''
    headers = {
    'x-rapidapi-key': '7f31bcaea1acc7e331e4356d2bf9072f',
    'x-rapidapi-host': 'v1.basketball.api-sports.io'
    }

    res_dict = {'results':0}
    if(dict.get('gameId') is not None):
        res = requests.request("GET",  "https://v1.basketball.api-sports.io/games" , params={'id': dict.get('gameId')}, headers=headers)    
        res_dict = json.loads(res.text)

    #print(res_dict)
    url = "https://newsdata.io/api/1/news"
    payload ={'apikey':'pub_876812b857fda4400c6ef8420d9d8d50c83d',
        'category':'sports'}
    query = ""
    if res_dict['results'] == 1:       
        payload['country'] = res_dict['response'][0]['country']['code']
        query += "q=%20OR%20" + res_dict['response'][0]['teams']['home']['name'].replace(" ","%20")
        query+= "%20OR%20" + res_dict['response'][0]['teams']['away']['name'].replace(" ","%20")
   
    response = requests.request("GET", "https://newsdata.io/api/1/news?"+query, params=payload)
    print(response.json())
    return response.json()