import requests

def main(dict):
    url = "https://v1.baseball.api-sports.io/leagues"

    headers = {
    'x-rapidapi-key': '7f31bcaea1acc7e331e4356d2bf9072f',
    'x-rapidapi-host': 'v1.baseball.api-sports.io'
    }

    response = requests.request("GET", url, headers=headers, params=dict)
    return response.json()

