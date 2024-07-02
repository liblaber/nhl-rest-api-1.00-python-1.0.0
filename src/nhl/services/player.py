from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models


class PlayerService(BaseService):
    
    @cast_models
    def get_game_log(self,player: int,season: int,game_type: int) -> dict:
        """Retrieve the game log for a specific player, season, and game type.

:param player: Player ID
:type player: int
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

        Validator(int).validate(player)
        Validator(int).validate(season)
        Validator(int).validate(game_type)

        serialized_request = Serializer(f"{self.base_url}/v1/player/{{player}}/game-log/{{season}}/{{game-type}}", self.get_default_headers()).add_path("player", player  ).add_path("season", season  ).add_path("game-type", game_type  ).serialize().set_method("GET")

        response = self.send_request(serialized_request)

        return response
    
    @cast_models
    def get_player_info(self,player: int) -> dict:
        """Retrieve information for a specific player.

:param player: Player ID
:type player: int
...
:raises RequestError: Raised when a request fails, with optional HTTP status code and details.
...
:return: Successful response
:rtype: dict
"""

        Validator(int).validate(player)

        serialized_request = Serializer(f"{self.base_url}/v1/player/{{player}}/landing", self.get_default_headers()).add_path("player", player  ).serialize().set_method("GET")

        response = self.send_request(serialized_request)

        return response
    
    @cast_models
    def get_game_log_current(self,player: int) -> dict:
        """Retrieve the game log for a specific player as of the current moment.

:param player: Player ID
:type player: int
...
:raises RequestError: Raised when a request fails, with optional HTTP status code and details.
...
:return: Successful response
:rtype: dict
"""

        Validator(int).validate(player)

        serialized_request = Serializer(f"{self.base_url}/v1/player/{{player}}/game-log/now", self.get_default_headers()).add_path("player", player  ).serialize().set_method("GET")

        response = self.send_request(serialized_request)

        return response
