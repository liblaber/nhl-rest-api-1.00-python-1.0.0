from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models


class ClubStatsService(BaseService):
    
    @cast_models
    def get_current_club_stats(self,team: str) -> dict:
        """Retrieve current statistics for a specific club.

:param team: Three-letter team code
:type team: str
...
:raises RequestError: Raised when a request fails, with optional HTTP status code and details.
...
:return: Successful response
:rtype: dict
"""

        Validator(str).validate(team)

        serialized_request = Serializer(f"{self.base_url}/v1/club-stats/{{team}}/now", self.get_default_headers()).add_path("team", team  ).serialize().set_method("GET")

        response = self.send_request(serialized_request)

        return response
    
    @cast_models
    def get_team_club_stats_season(self,team: str) -> dict:
        """Returns an overview of the stats for each season for a specific club.

:param team: Three-letter team code
:type team: str
...
:raises RequestError: Raised when a request fails, with optional HTTP status code and details.
...
:return: Successful response
:rtype: dict
"""

        Validator(str).validate(team)

        serialized_request = Serializer(f"{self.base_url}/v1/club-stats-season/{{team}}", self.get_default_headers()).add_path("team", team  ).serialize().set_method("GET")

        response = self.send_request(serialized_request)

        return response
    
    @cast_models
    def get_club_stats_by_season(self,team: str,season: int,game_type: int) -> dict:
        """Retrieve the stats for a specific team, season, and game type.

:param team: Three-letter team code
:type team: str
:param season: Season in YYYYYYYY format
:type season: int
:param game_type: Game type (2 for regular season, 3 for playoffs)
:type game_type: int
...
:raises RequestError: Raised when a request fails, with optional HTTP status code and details.
...
:return: Successful response
:rtype: dict
"""

        Validator(str).validate(team)
        Validator(int).validate(season)
        Validator(int).validate(game_type)

        serialized_request = Serializer(f"{self.base_url}/v1/club-stats/{{team}}/{{season}}/{{game-type}}", self.get_default_headers()).add_path("team", team  ).add_path("season", season  ).add_path("game-type", game_type  ).serialize().set_method("GET")

        response = self.send_request(serialized_request)

        return response
