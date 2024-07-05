# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .game_official import GameOfficial
from .game_boxscore_team import GameBoxscoreTeam


@JsonMap({})
class GameBoxscoreTeams(BaseModel):
    """GameBoxscoreTeams

    :param away: away, defaults to None
    :type away: GameBoxscoreTeam, optional
    :param home: home, defaults to None
    :type home: GameBoxscoreTeam, optional
    """

    def __init__(self, away: GameBoxscoreTeam = None, home: GameBoxscoreTeam = None):
        if away is not None:
            self.away = self._define_object(away, GameBoxscoreTeam)
        if home is not None:
            self.home = self._define_object(home, GameBoxscoreTeam)


@JsonMap({})
class GameBoxscore(BaseModel):
    """GameBoxscore

    :param teams: teams, defaults to None
    :type teams: GameBoxscoreTeams, optional
    :param officials: officials, defaults to None
    :type officials: List[GameOfficial], optional
    """

    def __init__(
        self, teams: GameBoxscoreTeams = None, officials: List[GameOfficial] = None
    ):
        if teams is not None:
            self.teams = self._define_object(teams, GameBoxscoreTeams)
        if officials is not None:
            self.officials = self._define_list(officials, GameOfficial)
