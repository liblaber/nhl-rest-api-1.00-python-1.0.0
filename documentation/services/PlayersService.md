# PlayersService

A list of all methods in the `PlayersService` service. Click on the method name to view detailed information about that method.

| Methods                               | Description |
| :------------------------------------ | :---------- |
| [get_player](#get_player)             |             |
| [get_player_stats](#get_player_stats) |             |

## get_player

- HTTP Method: `GET`
- Endpoint: `/people/{id}`

**Parameters**

| Name | Type  | Required | Description           |
| :--- | :---- | :------- | :-------------------- |
| id\_ | float | ✅       | The ID of the player. |

**Return Type**

`Players`

**Example Usage Code Snippet**

```python
from nhl import Nhl, Environment

sdk = Nhl(
    base_url=Environment.DEFAULT.value
)

result = sdk.players.get_player(id_=8466138)

print(result)
```

## get_player_stats

- HTTP Method: `GET`
- Endpoint: `/people/{id}/stats`

**Parameters**

| Name   | Type                                                    | Required | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| :----- | :------------------------------------------------------ | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| id\_   | float                                                   | ✅       | The ID of the player.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| stats  | [GetPlayerStatsStats](../models/GetPlayerStatsStats.md) | ✅       | Stats explanations: _ `homeAndAway` - Provides a split between home and away games. _ `byMonth` - Monthly split of stats. _ `byDayOfWeek` - Split done by day of the week. _ `goalsByGameSituation` - Shows number on when goals for a player happened like how many in the shootout, how many in each period, etc. _ `onPaceRegularSeason` - This only works with the current in-progress season and shows projected totals based on current onPaceRegularSeason. _ `regularSeasonStatRankings` - Returns where someone stands vs the rest of the league for a specific regularSeasonStatRankings _ `statsSingleSeason` - Obtains single season statistics for a player. _ `vsConference` - Conference stats split. _ `vsDivision` - Division stats split. _ `vsTeam` - Conference stats split. \* `winLoss` - Very similar to the previous modifier except it provides the W/L/OT split instead of Home and Away. |
| season | float                                                   | ❌       | Return a team's specific season.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

**Return Type**

`PlayerStats`

**Example Usage Code Snippet**

```python
from nhl import Nhl, Environment
from nhl.models import GetPlayerStatsStats

sdk = Nhl(
    base_url=Environment.DEFAULT.value
)

result = sdk.players.get_player_stats(
    id_=8466138,
    stats="homeAndAway",
    season=20172018
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
