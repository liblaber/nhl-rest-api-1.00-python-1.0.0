from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models


class ScheduleService(BaseService):
    
    @cast_models
    def get_team_next_game(self,team: str) -> dict:
        """Retrieve the next game for a specific team.

:param team: Three-letter team code
:type team: str
...
:raises RequestError: Raised when a request fails, with optional HTTP status code and details.
...
:return: Successful response
:rtype: dict
"""

        Validator(str).validate(team)

        serialized_request = Serializer(f"{self.base_url}/v1/schedule/{{team}}/next", self.get_default_headers()).add_path("team", team  ).serialize().set_method("GET")

        response = self.send_request(serialized_request)

        return response
    
    @cast_models
    def get_team_schedule_by_season(self,team: str,season: int) -> dict:
        """Retrieve the schedule for a specific team and season.

:param team: Three-letter team code
:type team: str
:param season: Season in YYYYYYYY format
:type season: int
...
:raises RequestError: Raised when a request fails, with optional HTTP status code and details.
...
:return: Successful response
:rtype: dict
"""

        Validator(str).validate(team)
        Validator(int).validate(season)

        serialized_request = Serializer(f"{self.base_url}/v1/schedule/{{team}}/{{season}}", self.get_default_headers()).add_path("team", team  ).add_path("season", season  ).serialize().set_method("GET")

        response = self.send_request(serialized_request)

        return response
    
    @cast_models
    def get_game_stats(self,season: int,team: str,game: int) -> dict:
        """Retrieve the statistics for a specific game.

:param season: Season in YYYYYYYY format
:type season: int
:param team: Three-letter team code
:type team: str
:param game: Game ID
:type game: int
...
:raises RequestError: Raised when a request fails, with optional HTTP status code and details.
...
:return: Successful response
:rtype: dict
"""

        Validator(int).validate(season)
        Validator(str).validate(team)
        Validator(int).validate(game)

        serialized_request = Serializer(f"{self.base_url}/v1/schedule/{{season}}/team/{{team}}/game/{{game}}", self.get_default_headers()).add_path("season", season  ).add_path("team", team  ).add_path("game", game  ).serialize().set_method("GET")

        response = self.send_request(serialized_request)

        return response
