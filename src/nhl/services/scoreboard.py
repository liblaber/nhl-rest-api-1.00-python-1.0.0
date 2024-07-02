from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models


class ScoreboardService(BaseService):
    
    @cast_models
    def get_current_team_scoreboard(self,team: str) -> dict:
        """Retrieve the scoreboard for a specific team as of the current moment.

:param team: Three-letter team code
:type team: str
...
:raises RequestError: Raised when a request fails, with optional HTTP status code and details.
...
:return: Successful response
:rtype: dict
"""

        Validator(str).validate(team)

        serialized_request = Serializer(f"{self.base_url}/v1/scoreboard/{{team}}/now", self.get_default_headers()).add_path("team", team  ).serialize().set_method("GET")

        response = self.send_request(serialized_request)

        return response
