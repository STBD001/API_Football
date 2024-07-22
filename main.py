import requests
import json

def get_league_standings(league_id, api_key):
    url=f"https://api.football-data.org/v2/competitions/{league_id}/standings"
    headers = {'X-Auth-Token': api_key}
    response=requests.get(url, headers=headers)
    data=response.json()
    return data

def get_team_stats(team_id, api_key):
    url = f"https://api.football-data.org/v2/teams/{team_id}"
    headers = {'X-Auth-Token': api_key}
    response = requests.get(url, headers=headers)
    data = response.json()
    return data

def get_maych_results(team_id, api_key):
    url = f"https://api.football-data.org/v2/teams/{team_id}/matches"
    headers={'X-Auth-Token': api_key}
    response = requests.get(url, headers=headers)
    data=response.json()
    return data

def dispaly_standings(data):
    if 'standings' in data:
        standings=data['standings'][0]['table']
        print("Tabela ligowa: ")
        for team in standings:
            position = team["position"]
            name=team['team']['name']
            points=team['points']
            print(f"{position}. {name} - {points} pkt")
        else:
            print("Error")

def display_team_stats(data):
    pass

def dispaly_match_results(data):
    pass

def main():
    pass

if __name__=="__main__":
    main()