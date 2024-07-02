# PlayerService

A list of all methods in the `PlayerService` service. Click on the method name to view detailed information about that method.

| Methods                                       | Description                                                           |
| :-------------------------------------------- | :-------------------------------------------------------------------- |
| [get_game_log](#get_game_log)                 | Retrieve the game log for a specific player, season, and game type.   |
| [get_player_info](#get_player_info)           | Retrieve information for a specific player.                           |
| [get_game_log_current](#get_game_log_current) | Retrieve the game log for a specific player as of the current moment. |

## get_game_log

Retrieve the game log for a specific player, season, and game type.

- HTTP Method: `GET`
- Endpoint: `/v1/player/{player}/game-log/{season}/{game-type}`

**Parameters**

| Name      | Type | Required | Description                                      |
| :-------- | :--- | :------- | :----------------------------------------------- |
| player    | int  | ✅       | Player ID                                        |
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

result = sdk.player.get_game_log(
    player=3,
    season=1,
    game_type=5
)

print(result)
```

## get_player_info

Retrieve information for a specific player.

- HTTP Method: `GET`
- Endpoint: `/v1/player/{player}/landing`

**Parameters**

| Name   | Type | Required | Description |
| :----- | :--- | :------- | :---------- |
| player | int  | ✅       | Player ID   |

**Return Type**

`dict`

**Example Usage Code Snippet**

```python
from nhl import Nhl, Environment

sdk = Nhl(
    base_url=Environment.DEFAULT.value
)

result = sdk.player.get_player_info(player=4)

print(result)
```

## get_game_log_current

Retrieve the game log for a specific player as of the current moment.

- HTTP Method: `GET`
- Endpoint: `/v1/player/{player}/game-log/now`

**Parameters**

| Name   | Type | Required | Description |
| :----- | :--- | :------- | :---------- |
| player | int  | ✅       | Player ID   |

**Return Type**

`dict`

**Example Usage Code Snippet**

```python
from nhl import Nhl, Environment

sdk = Nhl(
    base_url=Environment.DEFAULT.value
)

result = sdk.player.get_game_log_current(player=2)

print(result)
```
