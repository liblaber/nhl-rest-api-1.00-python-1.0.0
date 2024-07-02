from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models


class StandingsService(BaseService):
    
    @cast_models
    def get_current_standings(self) -> dict:
        """Retrieve the standings as of the current moment.

...
:raises RequestError: Raised when a request fails, with optional HTTP status code and details.
...
:return: Successful response
:rtype: dict
"""


        serialized_request = Serializer(f"{self.base_url}/v1/standings/now", self.get_default_headers()).serialize().set_method("GET")

        response = self.send_request(serialized_request)

        return response
    
    @cast_models
    def get_standings_by_date(self,date_: str) -> dict:
        """Retrieve the standings for a specific date.

:param date_: Date in YYYY-MM-DD format
:type date_: str
...
:raises RequestError: Raised when a request fails, with optional HTTP status code and details.
...
:return: Successful response
:rtype: dict
"""

        Validator(str).validate(date_)

        serialized_request = Serializer(f"{self.base_url}/v1/standings/{{date}}", self.get_default_headers()).add_path("date", date_  ).serialize().set_method("GET")

        response = self.send_request(serialized_request)

        return response
    
    @cast_models
    def get_standings_season(self) -> dict:
        """Retrieves information for each season's standings.

...
:raises RequestError: Raised when a request fails, with optional HTTP status code and details.
...
:return: Successful response
:rtype: dict
"""


        serialized_request = Serializer(f"{self.base_url}/v1/standings-season", self.get_default_headers()).serialize().set_method("GET")

        response = self.send_request(serialized_request)

        return response
