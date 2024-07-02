# ScheduleService

A list of all methods in the `ScheduleService` service. Click on the method name to view detailed information about that method.

| Methods                                                     | Description                                           |
| :---------------------------------------------------------- | :---------------------------------------------------- |
| [get_team_next_game](#get_team_next_game)                   | Retrieve the next game for a specific team.           |
| [get_team_schedule_by_season](#get_team_schedule_by_season) | Retrieve the schedule for a specific team and season. |
| [get_game_stats](#get_game_stats)                           | Retrieve the statistics for a specific game.          |

## get_team_next_game

Retrieve the next game for a specific team.

- HTTP Method: `GET`
- Endpoint: `/v1/schedule/{team}/next`

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

result = sdk.schedule.get_team_next_game(team="team")

print(result)
```

## get_team_schedule_by_season

Retrieve the schedule for a specific team and season.

- HTTP Method: `GET`
- Endpoint: `/v1/schedule/{team}/{season}`

**Parameters**

| Name   | Type | Required | Description               |
| :----- | :--- | :------- | :------------------------ |
| team   | str  | ✅       | Three-letter team code    |
| season | int  | ✅       | Season in YYYYYYYY format |

**Return Type**

`dict`

**Example Usage Code Snippet**

```python
from nhl import Nhl, Environment

sdk = Nhl(
    base_url=Environment.DEFAULT.value
)

result = sdk.schedule.get_team_schedule_by_season(
    team="team",
    season=5
)

print(result)
```

## get_game_stats

Retrieve the statistics for a specific game.

- HTTP Method: `GET`
- Endpoint: `/v1/schedule/{season}/team/{team}/game/{game}`

**Parameters**

| Name   | Type | Required | Description               |
| :----- | :--- | :------- | :------------------------ |
| season | int  | ✅       | Season in YYYYYYYY format |
| team   | str  | ✅       | Three-letter team code    |
| game   | int  | ✅       | Game ID                   |

**Return Type**

`dict`

**Example Usage Code Snippet**

```python
from nhl import Nhl, Environment

sdk = Nhl(
    base_url=Environment.DEFAULT.value
)

result = sdk.schedule.get_game_stats(
    season=5,
    team="team",
    game=8
)

print(result)
```
