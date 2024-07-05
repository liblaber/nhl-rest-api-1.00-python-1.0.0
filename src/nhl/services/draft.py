# This file was generated by liblab | https://liblab.com/

from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models.draft_prospects import DraftProspects
from ..models.draft import Draft


class DraftService(BaseService):

    @cast_models
    def get_draft(self) -> Draft:
        """get_draft

        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: OK
        :rtype: Draft
        """

        serialized_request = (
            Serializer(f"{self.base_url}/draft", self.get_default_headers())
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return Draft._unmap(response)

    @cast_models
    def get_draft_by_year(self, year: float) -> Draft:
        """get_draft_by_year

        :param year: The draft year.
        :type year: float
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: OK
        :rtype: Draft
        """

        Validator(float).validate(year)

        serialized_request = (
            Serializer(f"{self.base_url}/draft/{{year}}", self.get_default_headers())
            .add_path("year", year)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return Draft._unmap(response)

    @cast_models
    def get_draft_prospects(self) -> DraftProspects:
        """Be forewarned that this endpoint returns a **lot** of data and there does not appear to be a way to paginate results.

        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: OK
        :rtype: DraftProspects
        """

        serialized_request = (
            Serializer(f"{self.base_url}/draft/prospects", self.get_default_headers())
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return DraftProspects._unmap(response)

    @cast_models
    def get_draft_prospect(self, id_: float) -> DraftProspects:
        """get_draft_prospect

        :param id_: The prospect ID.
        :type id_: float
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: OK
        :rtype: DraftProspects
        """

        Validator(float).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url}/draft/prospects/{{id}}", self.get_default_headers()
            )
            .add_path("id", id_)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return DraftProspects._unmap(response)