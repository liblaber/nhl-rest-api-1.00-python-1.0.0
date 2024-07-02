from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models


class SkaterStatsService(BaseService):
    
    @cast_models
    def get_current_skater_stats_leaders(self,categories: str = None,limit: int = None) -> dict:
        """Retrieve current skater stats leaders.

:param categories: Categories to filter by, defaults to None
:type categories: str, optional
:param limit: Limit results (Note: a limit of -1 will return all results), defaults to None
:type limit: int, optional
...
:raises RequestError: Raised when a request fails, with optional HTTP status code and details.
...
:return: Successful response
:rtype: dict
"""

        Validator(str).is_optional().validate(categories)
        Validator(int).is_optional().validate(limit)

        serialized_request = Serializer(f"{self.base_url}/v1/skater-stats-leaders/current", self.get_default_headers()).add_query("categories", categories   ).add_query("limit", limit   ).serialize().set_method("GET")

        response = self.send_request(serialized_request)

        return response
    
    @cast_models
    def get_skater_stats_leaders(self,season: int,game_type: int,categories: str = None,limit: int = None) -> dict:
        """Retrieve skater stats leaders for a specific season and game type.

:param season: Season in YYYYYYYY format
:type season: int
:param game_type: Game type (2 for regular season, 3 for playoffs)
:type game_type: int
:param categories: Categories to filter by, defaults to None
:type categories: str, optional
:param limit: Limit results (Note: a limit of -1 will return all results), defaults to None
:type limit: int, optional
...
:raises RequestError: Raised when a request fails, with optional HTTP status code and details.
...
:return: Successful response
:rtype: dict
"""

        Validator(int).validate(season)
        Validator(int).validate(game_type)
        Validator(str).is_optional().validate(categories)
        Validator(int).is_optional().validate(limit)

        serialized_request = Serializer(f"{self.base_url}/v1/skater-stats-leaders/{{season}}/{{game-type}}", self.get_default_headers()).add_path("season", season  ).add_path("game-type", game_type  ).add_query("categories", categories   ).add_query("limit", limit   ).serialize().set_method("GET")

        response = self.send_request(serialized_request)

        return response
