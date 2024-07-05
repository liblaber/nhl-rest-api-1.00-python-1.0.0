# This file was generated by liblab | https://liblab.com/

from enum import Enum
from .utils.json_map import JsonMap
from .base import BaseModel


class StatTypesDisplayName(Enum):
    """An enumeration representing different categories.

    :cvar BYDAYOFWEEK: "byDayOfWeek"
    :vartype BYDAYOFWEEK: str
    :cvar BYDAYOFWEEKPLAYOFFS: "byDayOfWeekPlayoffs"
    :vartype BYDAYOFWEEKPLAYOFFS: str
    :cvar BYMONTH: "byMonth"
    :vartype BYMONTH: str
    :cvar BYMONTHPLAYOFFS: "byMonthPlayoffs"
    :vartype BYMONTHPLAYOFFS: str
    :cvar CAREERPLAYOFFS: "careerPlayoffs"
    :vartype CAREERPLAYOFFS: str
    :cvar CAREERREGULARSEASON: "careerRegularSeason"
    :vartype CAREERREGULARSEASON: str
    :cvar GAMELOG: "gameLog"
    :vartype GAMELOG: str
    :cvar GOALSBYGAMESITUATION: "goalsByGameSituation"
    :vartype GOALSBYGAMESITUATION: str
    :cvar GOALSBYGAMESITUATIONPLAYOFFS: "goalsByGameSituationPlayoffs"
    :vartype GOALSBYGAMESITUATIONPLAYOFFS: str
    :cvar HOMEANDAWAY: "homeAndAway"
    :vartype HOMEANDAWAY: str
    :cvar HOMEANDAWAYPLAYOFFS: "homeAndAwayPlayoffs"
    :vartype HOMEANDAWAYPLAYOFFS: str
    :cvar ONPACEREGULARSEASON: "onPaceRegularSeason"
    :vartype ONPACEREGULARSEASON: str
    :cvar PLAYOFFGAMELOG: "playoffGameLog"
    :vartype PLAYOFFGAMELOG: str
    :cvar PLAYOFFSTATRANKINGS: "playoffStatRankings"
    :vartype PLAYOFFSTATRANKINGS: str
    :cvar REGULARSEASONSTATRANKINGS: "regularSeasonStatRankings"
    :vartype REGULARSEASONSTATRANKINGS: str
    :cvar STATSSINGLESEASON: "statsSingleSeason"
    :vartype STATSSINGLESEASON: str
    :cvar STATSSINGLESEASONPLAYOFFS: "statsSingleSeasonPlayoffs"
    :vartype STATSSINGLESEASONPLAYOFFS: str
    :cvar VSCONFERENCE: "vsConference"
    :vartype VSCONFERENCE: str
    :cvar VSCONFERENCEPLAYOFFS: "vsConferencePlayoffs"
    :vartype VSCONFERENCEPLAYOFFS: str
    :cvar VSDIVISION: "vsDivision"
    :vartype VSDIVISION: str
    :cvar VSDIVISIONPLAYOFFS: "vsDivisionPlayoffs"
    :vartype VSDIVISIONPLAYOFFS: str
    :cvar VSTEAM: "vsTeam"
    :vartype VSTEAM: str
    :cvar VSTEAMPLAYOFFS: "vsTeamPlayoffs"
    :vartype VSTEAMPLAYOFFS: str
    :cvar WINLOSS: "winLoss"
    :vartype WINLOSS: str
    :cvar WINLOSSPLAYOFFS: "winLossPlayoffs"
    :vartype WINLOSSPLAYOFFS: str
    :cvar YEARBYYEAR: "yearByYear"
    :vartype YEARBYYEAR: str
    :cvar YEARBYYEARPLAYOFFS: "yearByYearPlayoffs"
    :vartype YEARBYYEARPLAYOFFS: str
    :cvar YEARBYYEARPLAYOFFSRANK: "yearByYearPlayoffsRank"
    :vartype YEARBYYEARPLAYOFFSRANK: str
    :cvar YEARBYYEARRANK: "yearByYearRank"
    :vartype YEARBYYEARRANK: str
    """

    BYDAYOFWEEK = "byDayOfWeek"
    BYDAYOFWEEKPLAYOFFS = "byDayOfWeekPlayoffs"
    BYMONTH = "byMonth"
    BYMONTHPLAYOFFS = "byMonthPlayoffs"
    CAREERPLAYOFFS = "careerPlayoffs"
    CAREERREGULARSEASON = "careerRegularSeason"
    GAMELOG = "gameLog"
    GOALSBYGAMESITUATION = "goalsByGameSituation"
    GOALSBYGAMESITUATIONPLAYOFFS = "goalsByGameSituationPlayoffs"
    HOMEANDAWAY = "homeAndAway"
    HOMEANDAWAYPLAYOFFS = "homeAndAwayPlayoffs"
    ONPACEREGULARSEASON = "onPaceRegularSeason"
    PLAYOFFGAMELOG = "playoffGameLog"
    PLAYOFFSTATRANKINGS = "playoffStatRankings"
    REGULARSEASONSTATRANKINGS = "regularSeasonStatRankings"
    STATSSINGLESEASON = "statsSingleSeason"
    STATSSINGLESEASONPLAYOFFS = "statsSingleSeasonPlayoffs"
    VSCONFERENCE = "vsConference"
    VSCONFERENCEPLAYOFFS = "vsConferencePlayoffs"
    VSDIVISION = "vsDivision"
    VSDIVISIONPLAYOFFS = "vsDivisionPlayoffs"
    VSTEAM = "vsTeam"
    VSTEAMPLAYOFFS = "vsTeamPlayoffs"
    WINLOSS = "winLoss"
    WINLOSSPLAYOFFS = "winLossPlayoffs"
    YEARBYYEAR = "yearByYear"
    YEARBYYEARPLAYOFFS = "yearByYearPlayoffs"
    YEARBYYEARPLAYOFFSRANK = "yearByYearPlayoffsRank"
    YEARBYYEARRANK = "yearByYearRank"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, StatTypesDisplayName._member_map_.values()))


@JsonMap({"display_name": "displayName"})
class StatTypes(BaseModel):
    """StatTypes

    :param display_name: display_name, defaults to None
    :type display_name: StatTypesDisplayName, optional
    """

    def __init__(self, display_name: StatTypesDisplayName = None):
        if display_name is not None:
            self.display_name = self._enum_matching(
                display_name, StatTypesDisplayName.list(), "display_name"
            )
