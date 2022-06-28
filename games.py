import requests
from datetime import date

def main(dict):
    today = date.today()
    if dict.get('date', None) is None:        
        dict['date'] = today.strftime("%Y-%m-%d")
        print(dict['date'])
    url = "https://v1.baseball.api-sports.io/games"
    

    headers = {
    'x-rapidapi-key': '7f31bcaea1acc7e331e4356d2bf9072f',
    'x-rapidapi-host': 'v1.baseball.api-sports.io'
    }

    response = requests.request("GET", url, headers=headers, params=dict)
    return response.json()
