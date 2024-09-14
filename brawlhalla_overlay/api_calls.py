import requests

API_URL = "https://brawlhalla.fly.dev/v1/"


def fetch_glory_stats(player_id):
    response = requests.get(f'{API_URL}glory/id?brawlhalla_id={player_id}')
    if response.status_code == 200:
        glory_data = response.json()

        return glory_data
    else:
        print(f'Failed to fetch data for Player ID: {player_id}')
        