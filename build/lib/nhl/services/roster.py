from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models


class RosterService(BaseService):
    
    @cast_models
    def get_current_team_roster(self,team: str) -> dict:
        """Retrieve the roster for a specific team as of the current moment.

:param team: Three-letter team code
:type team: str
...
:raises RequestError: Raised when a request fails, with optional HTTP status code and details.
...
:return: Successful response
:rtype: dict
"""

        Validator(str).validate(team)

        serialized_request = Serializer(f"{self.base_url}/v1/roster/{{team}}/current", self.get_default_headers()).add_path("team", team  ).serialize().set_method("GET")

        response = self.send_request(serialized_request)

        return response
    
    @cast_models
    def get_team_roster_by_season(self,team: str,season: int) -> dict:
        """Retrieve the roster for a specific team and season.

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

        serialized_request = Serializer(f"{self.base_url}/v1/roster/{{team}}/{{season}}", self.get_default_headers()).add_path("team", team  ).add_path("season", season  ).serialize().set_method("GET")

        response = self.send_request(serialized_request)

        return response
