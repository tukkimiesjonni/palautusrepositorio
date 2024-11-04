from player_reader import PlayerReader
from enum import Enum

class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3


class StatisticsService:
    def __init__(self, playerreader: PlayerReader):
        reader = playerreader

        self._players = reader.get_players()

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player

        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )

        return list(players_of_team)

    def top(self, how_many, sort_by):
        if sort_by == 1:
            keys = lambda player: player.points
        elif sort_by == 2:
            keys = lambda player: player.goals
        elif sort_by == 3:
            keys = lambda player: player.assists
        else:
            raise ValueError("Wrong number")

        # Järjestetään pelaajat määritellyn kriteerin mukaan
        sorted_players = sorted(
            self._players,
            reverse=True,
            key=keys
        )

        return sorted_players[:how_many]