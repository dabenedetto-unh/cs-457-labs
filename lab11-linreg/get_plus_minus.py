# get player game logs
from nba_api.stats.endpoints import playergamelog
from scipy import stats

# get player id from player name
from nba_api.stats.static import players
import pandas as pd

def get_player_id(player_name):
    player_dict = players.get_players()
    return [p['id'] for p in player_dict if p['full_name'] == player_name][0]


def get_player_stats(player_id, season):
    player_gamelog = playergamelog.PlayerGameLog(player_id=player_id, season=season)
    return player_gamelog.get_data_frames()[0]

if __name__ == "__main__":

    player_name = 'Jayson Tatum'
    player_id = get_player_id(player_name)
    season = "2025-26"

    player_stats = get_player_stats(player_id, season)
    tatum_plus_minus = player_stats['PLUS_MINUS']

    pd.DataFrame(tatum_plus_minus).to_csv('tatum_plus_minus.csv', index=False)