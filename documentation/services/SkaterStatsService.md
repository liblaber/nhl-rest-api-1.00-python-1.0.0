# SkaterStatsService

A list of all methods in the `SkaterStatsService` service. Click on the method name to view detailed information about that method.

| Methods                                                               | Description                                                        |
| :-------------------------------------------------------------------- | :----------------------------------------------------------------- |
| [get_current_skater_stats_leaders](#get_current_skater_stats_leaders) | Retrieve current skater stats leaders.                             |
| [get_skater_stats_leaders](#get_skater_stats_leaders)                 | Retrieve skater stats leaders for a specific season and game type. |

## get_current_skater_stats_leaders

Retrieve current skater stats leaders.

- HTTP Method: `GET`
- Endpoint: `/v1/skater-stats-leaders/current`

**Parameters**

| Name       | Type | Required | Description                                                 |
| :--------- | :--- | :------- | :---------------------------------------------------------- |
| categories | str  | ❌       | Categories to filter by                                     |
| limit      | int  | ❌       | Limit results (Note: a limit of -1 will return all results) |

**Return Type**

`dict`

**Example Usage Code Snippet**

```python
from nhl import Nhl, Environment

sdk = Nhl(
    base_url=Environment.DEFAULT.value
)

result = sdk.skater_stats.get_current_skater_stats_leaders(
    categories="categories",
    limit=2
)

print(result)
```

## get_skater_stats_leaders

Retrieve skater stats leaders for a specific season and game type.

- HTTP Method: `GET`
- Endpoint: `/v1/skater-stats-leaders/{season}/{game-type}`

**Parameters**

| Name       | Type | Required | Description                                                 |
| :--------- | :--- | :------- | :---------------------------------------------------------- |
| season     | int  | ✅       | Season in YYYYYYYY format                                   |
| game_type  | int  | ✅       | Game type (2 for regular season, 3 for playoffs)            |
| categories | str  | ❌       | Categories to filter by                                     |
| limit      | int  | ❌       | Limit results (Note: a limit of -1 will return all results) |

**Return Type**

`dict`

**Example Usage Code Snippet**

```python
from nhl import Nhl, Environment

sdk = Nhl(
    base_url=Environment.DEFAULT.value
)

result = sdk.skater_stats.get_skater_stats_leaders(
    season=6,
    game_type=2,
    categories="categories",
    limit=1
)

print(result)
```
