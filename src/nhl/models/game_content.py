# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .game_editorials import GameEditorials
from .game_highlight import GameHighlight
from .game_highlights import GameHighlights


@JsonMap({})
class Editorial(BaseModel):
    """Editorial

    :param preview: preview, defaults to None
    :type preview: GameEditorials, optional
    :param articles: articles, defaults to None
    :type articles: GameEditorials, optional
    :param recap: recap, defaults to None
    :type recap: GameEditorials, optional
    """

    def __init__(
        self,
        preview: GameEditorials = None,
        articles: GameEditorials = None,
        recap: GameEditorials = None,
    ):
        if preview is not None:
            self.preview = self._define_object(preview, GameEditorials)
        if articles is not None:
            self.articles = self._define_object(articles, GameEditorials)
        if recap is not None:
            self.recap = self._define_object(recap, GameEditorials)


class Title(Enum):
    """An enumeration representing different categories.

    :cvar MILESTONES: "Milestones"
    :vartype MILESTONES: str
    """

    MILESTONES = "Milestones"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, Title._member_map_.values()))


class ItemsType(Enum):
    """An enumeration representing different categories.

    :cvar BROADCAST_START: "BROADCAST_START"
    :vartype BROADCAST_START: str
    :cvar BROADCAST_END: "BROADCAST_END"
    :vartype BROADCAST_END: str
    :cvar GOAL: "GOAL"
    :vartype GOAL: str
    :cvar PERIOD_END: "PERIOD_END"
    :vartype PERIOD_END: str
    :cvar PERIOD_START: "PERIOD_START"
    :vartype PERIOD_START: str
    :cvar SHOT: "SHOT"
    :vartype SHOT: str
    """

    BROADCAST_START = "BROADCAST_START"
    BROADCAST_END = "BROADCAST_END"
    GOAL = "GOAL"
    PERIOD_END = "PERIOD_END"
    PERIOD_START = "PERIOD_START"
    SHOT = "SHOT"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, ItemsType._member_map_.values()))


@JsonMap(
    {
        "type_": "type",
        "time_absolute": "timeAbsolute",
        "time_offset": "timeOffset",
        "stats_event_id": "statsEventId",
        "team_id": "teamId",
        "player_id": "playerId",
        "period_time": "periodTime",
        "ordinal_num": "ordinalNum",
    }
)
class Items(BaseModel):
    """Items

    :param title: title, defaults to None
    :type title: str, optional
    :param description: description, defaults to None
    :type description: str, optional
    :param type_: type_, defaults to None
    :type type_: ItemsType, optional
    :param time_absolute: time_absolute, defaults to None
    :type time_absolute: str, optional
    :param time_offset: time_offset, defaults to None
    :type time_offset: str, optional
    :param period: period, defaults to None
    :type period: str, optional
    :param stats_event_id: stats_event_id, defaults to None
    :type stats_event_id: str, optional
    :param team_id: team_id, defaults to None
    :type team_id: str, optional
    :param player_id: player_id, defaults to None
    :type player_id: str, optional
    :param period_time: period_time, defaults to None
    :type period_time: str, optional
    :param ordinal_num: ordinal_num, defaults to None
    :type ordinal_num: str, optional
    :param highlight: highlight, defaults to None
    :type highlight: GameHighlight, optional
    """

    def __init__(
        self,
        title: str = None,
        description: str = None,
        type_: ItemsType = None,
        time_absolute: str = None,
        time_offset: str = None,
        period: str = None,
        stats_event_id: str = None,
        team_id: str = None,
        player_id: str = None,
        period_time: str = None,
        ordinal_num: str = None,
        highlight: GameHighlight = None,
    ):
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        if type_ is not None:
            self.type_ = self._enum_matching(type_, ItemsType.list(), "type_")
        if time_absolute is not None:
            self.time_absolute = time_absolute
        if time_offset is not None:
            self.time_offset = time_offset
        if period is not None:
            self.period = period
        if stats_event_id is not None:
            self.stats_event_id = stats_event_id
        if team_id is not None:
            self.team_id = team_id
        if player_id is not None:
            self.player_id = player_id
        if period_time is not None:
            self.period_time = period_time
        if ordinal_num is not None:
            self.ordinal_num = ordinal_num
        if highlight is not None:
            self.highlight = self._define_object(highlight, GameHighlight)


@JsonMap({"stream_start": "streamStart"})
class Milestones(BaseModel):
    """Milestones

    :param title: title, defaults to None
    :type title: Title, optional
    :param stream_start: stream_start, defaults to None
    :type stream_start: str, optional
    :param items: items, defaults to None
    :type items: List[Items], optional
    """

    def __init__(
        self, title: Title = None, stream_start: str = None, items: List[Items] = None
    ):
        if title is not None:
            self.title = self._enum_matching(title, Title.list(), "title")
        if stream_start is not None:
            self.stream_start = stream_start
        if items is not None:
            self.items = self._define_list(items, Items)


@JsonMap({})
class GameContentMedia(BaseModel):
    """GameContentMedia

    :param epg: epg, defaults to None
    :type epg: List[dict], optional
    :param milestones: milestones, defaults to None
    :type milestones: Milestones, optional
    """

    def __init__(self, epg: List[dict] = None, milestones: Milestones = None):
        if epg is not None:
            self.epg = epg
        if milestones is not None:
            self.milestones = self._define_object(milestones, Milestones)


@JsonMap({"game_center": "gameCenter"})
class Highlights(BaseModel):
    """Highlights

    :param scoreboard: scoreboard, defaults to None
    :type scoreboard: GameHighlights, optional
    :param game_center: game_center, defaults to None
    :type game_center: GameHighlights, optional
    """

    def __init__(
        self, scoreboard: GameHighlights = None, game_center: GameHighlights = None
    ):
        if scoreboard is not None:
            self.scoreboard = self._define_object(scoreboard, GameHighlights)
        if game_center is not None:
            self.game_center = self._define_object(game_center, GameHighlights)


@JsonMap({})
class GameContent(BaseModel):
    """GameContent

    :param copyright: copyright, defaults to None
    :type copyright: str, optional
    :param link: link, defaults to None
    :type link: str, optional
    :param editorial: editorial, defaults to None
    :type editorial: Editorial, optional
    :param media: media, defaults to None
    :type media: GameContentMedia, optional
    :param highlights: highlights, defaults to None
    :type highlights: Highlights, optional
    """

    def __init__(
        self,
        copyright: str = None,
        link: str = None,
        editorial: Editorial = None,
        media: GameContentMedia = None,
        highlights: Highlights = None,
    ):
        if copyright is not None:
            self.copyright = copyright
        if link is not None:
            self.link = link
        if editorial is not None:
            self.editorial = self._define_object(editorial, Editorial)
        if media is not None:
            self.media = self._define_object(media, GameContentMedia)
        if highlights is not None:
            self.highlights = self._define_object(highlights, Highlights)
