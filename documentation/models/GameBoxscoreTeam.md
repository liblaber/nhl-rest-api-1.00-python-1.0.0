# GameBoxscoreTeam

**Properties**

| Name        | Type                      | Required | Description |
| :---------- | :------------------------ | :------- | :---------- |
| team        | GameBoxscoreTeamTeam      | ❌       |             |
| team_stats  | GameBoxscoreTeamTeamStats | ❌       |             |
| players     | GameBoxscoreTeamPlayers   | ❌       |             |
| goalies     | List[float]               | ❌       |             |
| skaters     | List[float]               | ❌       |             |
| on_ice      | List[float]               | ❌       |             |
| on_ice_plus | List[OnIcePlus]           | ❌       |             |
| scratches   | List[float]               | ❌       |             |
| penalty_box | List[float]               | ❌       |             |
| coaches     | List[Coaches]             | ❌       |             |

# GameBoxscoreTeamTeam

**Properties**

| Name         | Type  | Required | Description |
| :----------- | :---- | :------- | :---------- |
| id\_         | float | ❌       |             |
| name         | str   | ❌       |             |
| link         | str   | ❌       |             |
| abbreviation | str   | ❌       |             |
| tri_code     | str   | ❌       |             |

# GameBoxscoreTeamTeamStats

**Properties**

| Name              | Type            | Required | Description |
| :---------------- | :-------------- | :------- | :---------- |
| team_skater_stats | TeamSkaterStats | ❌       |             |

# TeamSkaterStats

**Properties**

| Name                     | Type  | Required | Description |
| :----------------------- | :---- | :------- | :---------- |
| goals                    | float | ❌       |             |
| pim                      | float | ❌       |             |
| shots                    | float | ❌       |             |
| power_play_percentage    | str   | ❌       |             |
| power_play_goals         | float | ❌       |             |
| power_play_opportunities | float | ❌       |             |
| face_off_win_percentage  | str   | ❌       |             |
| blocked                  | float | ❌       |             |
| takeaways                | float | ❌       |             |
| giveaways                | float | ❌       |             |
| hits                     | float | ❌       |             |

# GameBoxscoreTeamPlayers

**Properties**

| Name          | Type            | Required | Description |
| :------------ | :-------------- | :------- | :---------- |
| person        | PlayersPerson   | ❌       |             |
| jersey_number | str             | ❌       |             |
| position      | PlayersPosition | ❌       |             |
| stats         | PlayersStats    | ❌       |             |

# PlayersPerson

**Properties**

| Name           | Type  | Required | Description |
| :------------- | :---- | :------- | :---------- |
| id\_           | float | ❌       |             |
| full_name      | str   | ❌       |             |
| link           | str   | ❌       |             |
| shoots_catches | str   | ❌       |             |
| roster_status  | str   | ❌       |             |

# PlayersPosition

**Properties**

| Name         | Type | Required | Description |
| :----------- | :--- | :------- | :---------- |
| code         | str  | ❌       |             |
| name         | str  | ❌       |             |
| type\_       | str  | ❌       |             |
| abbreviation | str  | ❌       |             |

# PlayersStats

**Properties**

| Name         | Type        | Required | Description |
| :----------- | :---------- | :------- | :---------- |
| skater_stats | SkaterStats | ❌       |             |

# SkaterStats

**Properties**

| Name                     | Type  | Required | Description |
| :----------------------- | :---- | :------- | :---------- |
| time_on_ice              | str   | ❌       |             |
| assists                  | float | ❌       |             |
| goals                    | float | ❌       |             |
| shots                    | float | ❌       |             |
| hits                     | float | ❌       |             |
| power_play_goals         | float | ❌       |             |
| power_play_assists       | float | ❌       |             |
| penalty_minutes          | float | ❌       |             |
| face_off_wins            | float | ❌       |             |
| faceoff_taken            | float | ❌       |             |
| takeaways                | float | ❌       |             |
| giveaways                | float | ❌       |             |
| short_handed_goals       | float | ❌       |             |
| short_handed_assists     | float | ❌       |             |
| blocked                  | float | ❌       |             |
| plus_minus               | float | ❌       |             |
| even_time_on_ice         | str   | ❌       |             |
| power_play_time_on_ice   | str   | ❌       |             |
| short_handed_time_on_ice | str   | ❌       |             |

# OnIcePlus

**Properties**

| Name           | Type  | Required | Description |
| :------------- | :---- | :------- | :---------- |
| player_id      | float | ❌       |             |
| shift_duration | float | ❌       |             |
| stamina        | float | ❌       |             |

# Coaches

**Properties**

| Name     | Type            | Required | Description |
| :------- | :-------------- | :------- | :---------- |
| person   | CoachesPerson   | ❌       |             |
| position | CoachesPosition | ❌       |             |

# CoachesPerson

**Properties**

| Name      | Type | Required | Description |
| :-------- | :--- | :------- | :---------- |
| full_name | str  | ❌       |             |
| link      | str  | ❌       |             |

# CoachesPosition

**Properties**

| Name         | Type | Required | Description |
| :----------- | :--- | :------- | :---------- |
| code         | str  | ❌       |             |
| name         | str  | ❌       |             |
| type\_       | str  | ❌       |             |
| abbreviation | str  | ❌       |             |

<!-- This file was generated by liblab | https://liblab.com/ -->
