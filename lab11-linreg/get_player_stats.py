# get player game logs
from nba_api.stats.endpoints import playergamelog
# from scipy import stats
import nba_api.stats.endpoints as nba

# get player id from player name
from nba_api.stats.static import players
import pandas as pd

def get_player_id(player_name):
    player_dict = players.get_players()
    return [p['id'] for p in player_dict if p['full_name'] == player_name][0]


def get_player_stats(player_id, season):

    player_gamelog = playergamelog.PlayerGameLog(player_id=player_id, season=season)
    return player_gamelog.get_data_frames()[0]

def get_all_player_stats(season):

    player_stats = nba.LeagueDashPlayerStats(season=season).get_data_frames()[0]

    return player_stats

if __name__ == "__main__":

    df = get_all_player_stats("2025-26")
    df.to_csv('data/league_stats.csv', index=False)

    # player_name = 'Jayson Tatum'
    # player_id = get_player_id(player_name)
    # season = "2025-26"

    # player_stats = get_player_stats(player_id, season)

    # lname = player_name.split(' ')[1].lower().replace(' ', '_')

    # pd.DataFrame(player_stats).to_csv(f'data/{lname}_stats.csv', index=False)#, header)