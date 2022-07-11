import requests

'''params and default values
 id,
 name,
 country,
 season,
 type,
 search
'''
def main(dict):
    
    url = "https://v1.basketball.api-sports.io/leagues"
    headers = {
    'x-rapidapi-key': '7f31bcaea1acc7e331e4356d2bf9072f',
    'x-rapidapi-host': 'v1.basketball.api-sports.io'
    }

    response = requests.request("GET", url, headers=headers, params=dict)

    ids = []
    for i in response.json()['response']:
        ids.append(i["id"])
    return {"league" : ids}

