from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models


class PlayerSpotlightService(BaseService):
    
    @cast_models
    def get_player_spotlight(self) -> dict:
        """Retrieve information about players in the "spotlight".

...
:raises RequestError: Raised when a request fails, with optional HTTP status code and details.
...
:return: Successful response
:rtype: dict
"""


        serialized_request = Serializer(f"{self.base_url}/v1/player-spotlight", self.get_default_headers()).serialize().set_method("GET")

        response = self.send_request(serialized_request)

        return response
