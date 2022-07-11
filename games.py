import requests
from datetime import date

def main(dict):
    url = "https://v1.basketball.api-sports.io/games"
    headers = {
    'x-rapidapi-key': '7f31bcaea1acc7e331e4356d2bf9072f',
    'x-rapidapi-host': 'v1.basketball.api-sports.io'
    }


    today = date.today()
    if dict.get('date', None) is None and dict.get('league', None) is None and dict.get('season', None) is None and dict.get('team', None) is None:
        ##se não forem passados parametros, busca os jogos do dia        
        dict['date'] = today.strftime("%Y-%m-%d")
        
    
    if dict.get('date', None) is None and dict.get('league', None) is not None: 
        #se for buscar por liga, so pode buscar pelos jogos de um dia, se não tiver esse dia é o dia de hoje
        dict['date'] = today.strftime("%Y-%m-%d")    


    if dict.get('season', None) is None and (dict.get('league', None) is not None or dict.get('team', None) is not None):
        #Se for buscar por time ou liga e não tiver temporada, coloca a do ano atual
            dict['season'] = date.today().year
            
            

    responseList = [];
    if isinstance(dict.get('team', None), list):
        for i in dict.get('team', None):
            newDict = dict.copy()
            newDict["team"] = i;
            responseList.append(requests.request("GET", url, headers=headers, params=newDict))
    elif isinstance(dict.get('league', None), list):
        for i in dict.get('league', None):
            newDict = dict.copy()
            newDict["team"] = i;
            responseList.append(requests.request("GET", url, headers=headers, params=newDict))
    else:
        responseList.append(requests.request("GET", url, headers=headers, params=dict))
    #print(responseList[0].json())

    res ={"results": 0, "response":[]}
    for i in responseList:
        #print(i.json()['results'])
        res['results'] = res['results'] + i.json()['results']
        res['response'] = res['response'] + i.json()['response']
    
    print(res)
    return res

#main({"team": [145]})