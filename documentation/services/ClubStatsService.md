# ClubStatsService

A list of all methods in the `ClubStatsService` service. Click on the method name to view detailed information about that method.

| Methods                                                   | Description                                                           |
| :-------------------------------------------------------- | :-------------------------------------------------------------------- |
| [get_current_club_stats](#get_current_club_stats)         | Retrieve current statistics for a specific club.                      |
| [get_team_club_stats_season](#get_team_club_stats_season) | Returns an overview of the stats for each season for a specific club. |
| [get_club_stats_by_season](#get_club_stats_by_season)     | Retrieve the stats for a specific team, season, and game type.        |

## get_current_club_stats

Retrieve current statistics for a specific club.

- HTTP Method: `GET`
- Endpoint: `/v1/club-stats/{team}/now`

**Parameters**

| Name | Type | Required | Description            |
| :--- | :--- | :------- | :--------------------- |
| team | str  | ✅       | Three-letter team code |

**Return Type**

`dict`

**Example Usage Code Snippet**

```python
from nhl import Nhl, Environment

sdk = Nhl(
    base_url=Environment.DEFAULT.value
)

result = sdk.club_stats.get_current_club_stats(team="team")

print(result)
```

## get_team_club_stats_season

Returns an overview of the stats for each season for a specific club.

- HTTP Method: `GET`
- Endpoint: `/v1/club-stats-season/{team}`

**Parameters**

| Name | Type | Required | Description            |
| :--- | :--- | :------- | :--------------------- |
| team | str  | ✅       | Three-letter team code |

**Return Type**

`dict`

**Example Usage Code Snippet**

```python
from nhl import Nhl, Environment

sdk = Nhl(
    base_url=Environment.DEFAULT.value
)

result = sdk.club_stats.get_team_club_stats_season(team="team")

print(result)
```

## get_club_stats_by_season

Retrieve the stats for a specific team, season, and game type.

- HTTP Method: `GET`
- Endpoint: `/v1/club-stats/{team}/{season}/{game-type}`

**Parameters**

| Name      | Type | Required | Description                                      |
| :-------- | :--- | :------- | :----------------------------------------------- |
| team      | str  | ✅       | Three-letter team code                           |
| season    | int  | ✅       | Season in YYYYYYYY format                        |
| game_type | int  | ✅       | Game type (2 for regular season, 3 for playoffs) |

**Return Type**

`dict`

**Example Usage Code Snippet**

```python
from nhl import Nhl, Environment

sdk = Nhl(
    base_url=Environment.DEFAULT.value
)

result = sdk.club_stats.get_club_stats_by_season(
    team="team",
    season=1,
    game_type=8
)

print(result)
```
