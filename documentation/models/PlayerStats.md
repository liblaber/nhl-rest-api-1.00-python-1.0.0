# PlayerStats

**Properties**

| Name      | Type                   | Required | Description |
| :-------- | :--------------------- | :------- | :---------- |
| copyright | str                    | ❌       |             |
| stats     | List[PlayerStatsStats] | ❌       |             |

# PlayerStatsStats

**Properties**

| Name   | Type               | Required | Description |
| :----- | :----------------- | :------- | :---------- |
| type\_ | StatsType1         | ❌       |             |
| splits | List[StatsSplits1] | ❌       |             |

# StatsType_1

**Properties**

| Name         | Type            | Required | Description |
| :----------- | :-------------- | :------- | :---------- |
| display_name | TypeDisplayName | ❌       |             |

# TypeDisplayName

**Properties**

| Name                      | Type | Required | Description                 |
| :------------------------ | :--- | :------- | :-------------------------- |
| BYDAYOFWEEK               | str  | ✅       | "byDayOfWeek"               |
| BYMONTH                   | str  | ✅       | "byMonth"                   |
| GOALSBYGAMESITUATION      | str  | ✅       | "goalsByGameSituation"      |
| HOMEANDAWAY               | str  | ✅       | "homeAndAway"               |
| ONPACEREGULARSEASON       | str  | ✅       | "onPaceRegularSeason"       |
| REGULARSEASONSTATRANKINGS | str  | ✅       | "regularSeasonStatRankings" |
| STATSSINGLESEASON         | str  | ✅       | "statsSingleSeason"         |
| VSCONFERENCE              | str  | ✅       | "vsConference"              |
| VSDIVISION                | str  | ✅       | "vsDivision"                |
| VSTEAM                    | str  | ✅       | "vsTeam"                    |
| WINLOSS                   | str  | ✅       | "winLoss"                   |

# StatsSplits_1

**Properties**

| Name                | Type               | Required | Description |
| :------------------ | :----------------- | :------- | :---------- |
| season              | str                | ❌       |             |
| stat                | SplitsStat1        | ❌       |             |
| is_home             | bool               | ❌       |             |
| is_win              | bool               | ❌       |             |
| is_ot               | bool               | ❌       |             |
| month               | float              | ❌       |             |
| day_of_week         | float              | ❌       |             |
| opponent            | Opponent           | ❌       |             |
| opponent_division   | OpponentDivision   | ❌       |             |
| opponent_conference | OpponentConference | ❌       |             |

# SplitsStat_1

**Properties**

| Name                              | Type  | Required | Description |
| :-------------------------------- | :---- | :------- | :---------- |
| time_on_ice                       | str   | ❌       |             |
| assists                           | str   | ❌       |             |
| goals                             | float | ❌       |             |
| pim                               | float | ❌       |             |
| shots                             | float | ❌       |             |
| games                             | float | ❌       |             |
| hits                              | float | ❌       |             |
| power_play_goals                  | float | ❌       |             |
| power_play_points                 | float | ❌       |             |
| power_play_time_on_ice            | float | ❌       |             |
| even_time_on_ice                  | float | ❌       |             |
| penalty_minutes                   | float | ❌       |             |
| face_off_pct                      | float | ❌       |             |
| shot_pct                          | float | ❌       |             |
| game_winning_goals                | float | ❌       |             |
| over_time_goals                   | float | ❌       |             |
| short_handed_goals                | float | ❌       |             |
| short_handed_points               | float | ❌       |             |
| short_handed_time_on_ice          | str   | ❌       |             |
| blocked                           | float | ❌       |             |
| plus_minus                        | float | ❌       |             |
| points                            | float | ❌       |             |
| shifts                            | float | ❌       |             |
| time_on_ice_per_game              | str   | ❌       |             |
| even_time_on_ice_per_game         | str   | ❌       |             |
| short_handed_time_on_ice_per_game | str   | ❌       |             |
| power_play_time_on_ice_per_game   | str   | ❌       |             |
| rank_power_play_goals             | str   | ❌       |             |
| rank_blocked_shots                | str   | ❌       |             |
| rank_assists                      | str   | ❌       |             |
| rank_shot_pct                     | str   | ❌       |             |
| rank_goals                        | str   | ❌       |             |
| rank_hits                         | str   | ❌       |             |
| rank_penalty_minutes              | str   | ❌       |             |
| rank_short_handed_goals           | str   | ❌       |             |
| rank_plus_minus                   | str   | ❌       |             |
| rank_shots                        | str   | ❌       |             |
| rank_points                       | str   | ❌       |             |
| rank_overtime_goals               | str   | ❌       |             |
| rank_games_played                 | str   | ❌       |             |
| goals_in_first_period             | float | ❌       |             |
| goals_in_second_period            | float | ❌       |             |
| goals_in_third_period             | float | ❌       |             |
| goals_trailing_by_one             | float | ❌       |             |
| goals_trailing_by_two             | float | ❌       |             |
| goals_trailing_by_three_plus      | float | ❌       |             |
| goals_when_tied                   | float | ❌       |             |
| goals_leading_by_one              | float | ❌       |             |
| goals_leading_by_two              | float | ❌       |             |

# Opponent

**Properties**

| Name | Type  | Required | Description |
| :--- | :---- | :------- | :---------- |
| id\_ | float | ❌       |             |
| name | str   | ❌       |             |
| link | str   | ❌       |             |

# OpponentDivision

**Properties**

| Name | Type  | Required | Description |
| :--- | :---- | :------- | :---------- |
| id\_ | float | ❌       |             |
| name | str   | ❌       |             |
| link | str   | ❌       |             |

# OpponentConference

**Properties**

| Name | Type  | Required | Description |
| :--- | :---- | :------- | :---------- |
| id\_ | float | ❌       |             |
| name | str   | ❌       |             |
| link | str   | ❌       |             |

<!-- This file was generated by liblab | https://liblab.com/ -->
