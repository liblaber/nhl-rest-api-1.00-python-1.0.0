# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .conference import Conference


@JsonMap({})
class Conferences(BaseModel):
    """Conferences

    :param copyright: copyright, defaults to None
    :type copyright: str, optional
    :param teams: teams, defaults to None
    :type teams: List[Conference], optional
    """

    def __init__(self, copyright: str = None, teams: List[Conference] = None):
        if copyright is not None:
            self.copyright = copyright
        if teams is not None:
            self.teams = self._define_list(teams, Conference)