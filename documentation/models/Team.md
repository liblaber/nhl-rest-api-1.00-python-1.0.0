# Team

**Properties**

| Name               | Type             | Required | Description |
| :----------------- | :--------------- | :------- | :---------- |
| id\_               | float            | ❌       |             |
| name               | str              | ❌       |             |
| link               | str              | ❌       |             |
| venue              | Venue            | ❌       |             |
| abbreviation       | str              | ❌       |             |
| tri_code           | str              | ❌       |             |
| team_name          | str              | ❌       |             |
| location_name      | str              | ❌       |             |
| first_year_of_play | float            | ❌       |             |
| division           | TeamDivision     | ❌       |             |
| conference         | TeamConference   | ❌       |             |
| franchise          | Franchise        | ❌       |             |
| roster             | TeamRoster       | ❌       |             |
| next_game_schedule | NextGameSchedule | ❌       |             |
| short_name         | str              | ❌       |             |
| official_site_url  | str              | ❌       |             |
| franchise_id       | float            | ❌       |             |
| active             | bool             | ❌       |             |

# TeamDivision

**Properties**

| Name | Type  | Required | Description |
| :--- | :---- | :------- | :---------- |
| id\_ | float | ❌       |             |
| name | str   | ❌       |             |
| link | str   | ❌       |             |

# TeamConference

**Properties**

| Name | Type  | Required | Description |
| :--- | :---- | :------- | :---------- |
| id\_ | float | ❌       |             |
| name | str   | ❌       |             |
| link | str   | ❌       |             |

# TeamRoster

**Properties**

| Name   | Type         | Required | Description |
| :----- | :----------- | :------- | :---------- |
| roster | List[Roster] | ❌       |             |

# NextGameSchedule

**Properties**

| Name          | Type        | Required | Description |
| :------------ | :---------- | :------- | :---------- |
| total_items   | float       | ❌       |             |
| total_events  | float       | ❌       |             |
| total_games   | float       | ❌       |             |
| total_matches | float       | ❌       |             |
| dates         | List[Dates] | ❌       |             |

# Dates

**Properties**

| Name          | Type        | Required | Description |
| :------------ | :---------- | :------- | :---------- |
| date\_        | str         | ❌       |             |
| total_items   | float       | ❌       |             |
| total_events  | float       | ❌       |             |
| total_games   | float       | ❌       |             |
| total_matches | float       | ❌       |             |
| games         | List[Games] | ❌       |             |
| events        | List[dict]  | ❌       |             |
| matches       | List[dict]  | ❌       |             |

# Games

**Properties**

| Name      | Type         | Required | Description |
| :-------- | :----------- | :------- | :---------- |
| game_pk   | float        | ❌       |             |
| link      | str          | ❌       |             |
| game_type | str          | ❌       |             |
| season    | str          | ❌       |             |
| game_date | str          | ❌       |             |
| status    | GamesStatus  | ❌       |             |
| teams     | GamesTeams   | ❌       |             |
| venue     | GamesVenue   | ❌       |             |
| content   | GamesContent | ❌       |             |

# GamesStatus

**Properties**

| Name                | Type              | Required | Description |
| :------------------ | :---------------- | :------- | :---------- |
| abstract_game_state | AbstractGameState | ❌       |             |
| coded_game_state    | CodedGameState    | ❌       |             |
| detailed_state      | DetailedState     | ❌       |             |
| status_code         | StatusCode        | ❌       |             |
| start_time_tbd      | bool              | ❌       |             |

# AbstractGameState

**Properties**

| Name    | Type | Required | Description |
| :------ | :--- | :------- | :---------- |
| LIVE    | str  | ✅       | "Live"      |
| PREVIEW | str  | ✅       | "Preview"   |

# CodedGameState

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| \_2  | str  | ✅       | "2"         |
| \_3  | str  | ✅       | "3"         |

# DetailedState

**Properties**

| Name        | Type | Required | Description   |
| :---------- | :--- | :------- | :------------ |
| IN_PROGRESS | str  | ✅       | "In Progress" |
| PRE_GAME    | str  | ✅       | "Pre-Game"    |

# StatusCode

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| \_2  | str  | ✅       | "2"         |
| \_3  | str  | ✅       | "3"         |

# GamesTeams

**Properties**

| Name | Type       | Required | Description |
| :--- | :--------- | :------- | :---------- |
| away | TeamsAway1 | ❌       |             |
| home | TeamsHome1 | ❌       |             |

# TeamsAway_1

**Properties**

| Name          | Type              | Required | Description |
| :------------ | :---------------- | :------- | :---------- |
| league_record | AwayLeagueRecord1 | ❌       |             |
| score         | float             | ❌       |             |
| team          | AwayTeam1         | ❌       |             |

# AwayLeagueRecord_1

**Properties**

| Name   | Type  | Required | Description |
| :----- | :---- | :------- | :---------- |
| wins   | float | ❌       |             |
| losses | float | ❌       |             |
| ot     | float | ❌       |             |
| type\_ | str   | ❌       |             |

# AwayTeam_1

**Properties**

| Name | Type  | Required | Description |
| :--- | :---- | :------- | :---------- |
| id\_ | float | ❌       |             |
| name | str   | ❌       |             |
| link | str   | ❌       |             |

# TeamsHome_1

**Properties**

| Name          | Type              | Required | Description |
| :------------ | :---------------- | :------- | :---------- |
| league_record | HomeLeagueRecord1 | ❌       |             |
| score         | float             | ❌       |             |
| team          | HomeTeam1         | ❌       |             |

# HomeLeagueRecord_1

**Properties**

| Name   | Type  | Required | Description |
| :----- | :---- | :------- | :---------- |
| wins   | float | ❌       |             |
| losses | float | ❌       |             |
| ot     | float | ❌       |             |
| type\_ | str   | ❌       |             |

# HomeTeam_1

**Properties**

| Name | Type  | Required | Description |
| :--- | :---- | :------- | :---------- |
| id\_ | float | ❌       |             |
| name | str   | ❌       |             |
| link | str   | ❌       |             |

# GamesVenue

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| name | str  | ❌       |             |
| link | str  | ❌       |             |

# GamesContent

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| link | str  | ❌       |             |

<!-- This file was generated by liblab | https://liblab.com/ -->
