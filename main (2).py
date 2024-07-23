import requests
import json
from tabulate import tabulate

def get_league_standings(league_id, api_key):
    url = f"https://api.football-data.org/v2/competitions/{league_id}/standings"
    headers = {'X-Auth-Token': api_key}
    try:
        print(f"Pobieranie tabeli ligowej dla ligi o ID: {league_id}")  # Debug
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Sprawdzenie błędów HTTP
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Błąd podczas pobierania tabeli ligowej: {e}")
        return {}

def get_team_stats(team_id, api_key):
    url = f"https://api.football-data.org/v2/teams/{team_id}"
    headers = {'X-Auth-Token': api_key}
    try:
        print(f"Pobieranie statystyk drużyny o ID: {team_id}")  # Debug
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Błąd podczas pobierania statystyk drużyny: {e}")
        return {}

def get_match_results(team_id, api_key):
    url = f"https://api.football-data.org/v2/teams/{team_id}/matches"
    headers = {'X-Auth-Token': api_key}
    try:
        print(f"Pobieranie wyników meczów dla drużyny o ID: {team_id}")  # Debug
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Błąd podczas pobierania wyników meczów: {e}")
        return {}

def get_all_matches(api_key):
    url = 'https://api.football-data.org/v4/matches'
    headers = {'X-Auth-Token': api_key}
    try:
        print("Pobieranie wszystkich meczów")  # Debug
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Błąd podczas pobierania wszystkich meczów: {e}")
        return {}

def display_standings(data):
    if 'standings' in data:
        standings = data['standings'][0]['table']
        table = [[team["position"], team['team']['name'], team['points']] for team in standings]
        print("Tabela ligowa:")
        print(tabulate(table, headers=["Pozycja", "Drużyna", "Punkty"], tablefmt="grid"))
    else:
        print("Błąd: Brak danych o tabeli ligowej")

def display_team_stats(data):
    if 'name' in data:
        name = data['name']
        founded = data['founded']
        venue = data['venue']
        table = [[name, founded, venue]]
        print("Statystyki drużyny:")
        print(tabulate(table, headers=["Nazwa drużyny", "Rok założenia", "Stadion"], tablefmt="grid"))
    else:
        print("Błąd: Brak danych o statystykach drużyny")

def display_match_results(data):
    if 'matches' in data:
        matches = data['matches']
        table = [[match['homeTeam']['name'], match['score']['fullTime']['homeTeam'], match['score']['fullTime']['awayTeam'], match['awayTeam']['name']] for match in matches]
        print("Wyniki meczów:")
        print(tabulate(table, headers=["Gospodarze", "Gole Gospodarzy", "Gole Gości", "Goście"], tablefmt="grid"))
    else:
        print("Błąd: Brak danych o wynikach meczów")

def display_all_matches(data):
    if 'matches' in data:
        matches = data['matches']
        table = [[match['homeTeam']['name'], match['awayTeam']['name'], match['utcDate']] for match in matches]
        print("Wszystkie mecze:")
        print(tabulate(table, headers=["Gospodarze", "Goście", "Data"], tablefmt="grid"))
    else:
        print("Błąd: Brak danych o meczach")

def main():
    api_key = "c2e7b75c063e46bbafe2e8c57b58192a"
    league_id = "PL"
    team_id = 64

    print("\nTabela ligowa")
    league_standings = get_league_standings(league_id, api_key)
    display_standings(league_standings)

    print("\nStatystyki drużyny")
    team_stats = get_team_stats(team_id, api_key)
    display_team_stats(team_stats)

    print("\nWyniki meczów")
    match_results = get_match_results(team_id, api_key)
    display_match_results(match_results)

    print("\nWszystkie mecze")
    all_matches = get_all_matches(api_key)
    display_all_matches(all_matches)

if __name__ == "__main__":
    main()
