# This file was generated by liblab | https://liblab.com/

from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models.game_content import GameContent
from ..models.game_boxscores import GameBoxscores
from ..models.game import Game


class GamesService(BaseService):

    @cast_models
    def get_game_boxscore(self, id_: float) -> GameBoxscores:
        """If you want detailed play information, you should use `/game/{id}/feed/live` or `/game/{id}/feed/live/diffPatch`.

        :param id_: The ID of the game. The first 4 digits identify the season of the game (ie. 2017 for the 2017-2018 season). The next 2 digits give the type of game, where 01 = preseason, 02 = regular season, 03 = playoffs, 04 = all-star. The final 4 digits identify the specific game number. For regular season and preseason games, this ranges from 0001 to the number of games played. (1271 for seasons with 31 teams (2017 and onwards) and 1230 for seasons with 30 teams). For playoff games, the 2nd digit of the specific number gives the round of the playoffs, the 3rd digit specifies the matchup, and the 4th digit specifies the game (out of 7).
        :type id_: float
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: OK
        :rtype: GameBoxscores
        """

        Validator(float).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url}/game/{{id}}/boxscore", self.get_default_headers()
            )
            .add_path("id", id_)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return GameBoxscores._unmap(response)

    @cast_models
    def get_game_content(self, id_: float) -> GameContent:
        """get_game_content

        :param id_: The ID of the game. The first 4 digits identify the season of the game (ie. 2017 for the 2017-2018 season). The next 2 digits give the type of game, where 01 = preseason, 02 = regular season, 03 = playoffs, 04 = all-star. The final 4 digits identify the specific game number. For regular season and preseason games, this ranges from 0001 to the number of games played. (1271 for seasons with 31 teams (2017 and onwards) and 1230 for seasons with 30 teams). For playoff games, the 2nd digit of the specific number gives the round of the playoffs, the 3rd digit specifies the matchup, and the 4th digit specifies the game (out of 7).
        :type id_: float
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: OK
        :rtype: GameContent
        """

        Validator(float).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url}/game/{{id}}/content", self.get_default_headers()
            )
            .add_path("id", id_)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return GameContent._unmap(response)

    @cast_models
    def get_game(self, id_: float) -> Game:
        """This contains all data related to a game, from the boxscore, to play data and even on-ice coordinates. Be forewarned that, depending on the game, this endpoint can return a **lot** of data.

        :param id_: The ID of the game. The first 4 digits identify the season of the game (ie. 2017 for the 2017-2018 season). The next 2 digits give the type of game, where 01 = preseason, 02 = regular season, 03 = playoffs, 04 = all-star. The final 4 digits identify the specific game number. For regular season and preseason games, this ranges from 0001 to the number of games played. (1271 for seasons with 31 teams (2017 and onwards) and 1230 for seasons with 30 teams). For playoff games, the 2nd digit of the specific number gives the round of the playoffs, the 3rd digit specifies the matchup, and the 4th digit specifies the game (out of 7).
        :type id_: float
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: OK
        :rtype: Game
        """

        Validator(float).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url}/game/{{id}}/feed/live", self.get_default_headers()
            )
            .add_path("id", id_)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return Game._unmap(response)

    @cast_models
    def get_game_diff(self, id_: float, start_time_code: str) -> Game:
        """You can use this to return a small subset of data relating to game.

        :param id_: The ID of the game. The first 4 digits identify the season of the game (ie. 2017 for the 2017-2018 season). The next 2 digits give the type of game, where 01 = preseason, 02 = regular season, 03 = playoffs, 04 = all-star. The final 4 digits identify the specific game number. For regular season and preseason games, this ranges from 0001 to the number of games played. (1271 for seasons with 31 teams (2017 and onwards) and 1230 for seasons with 30 teams). For playoff games, the 2nd digit of the specific number gives the round of the playoffs, the 3rd digit specifies the matchup, and the 4th digit specifies the game (out of 7).
        :type id_: float
        :param start_time_code: The prospect ID.
        :type start_time_code: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: OK
        :rtype: Game
        """

        Validator(float).validate(id_)
        Validator(str).pattern("^(\d{8})_(\d{4})$").validate(start_time_code)

        serialized_request = (
            Serializer(
                f"{self.base_url}/game/{{id}}/feed/live/diffPatch",
                self.get_default_headers(),
            )
            .add_path("id", id_)
            .add_query("startTimeCode", start_time_code)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return Game._unmap(response)
