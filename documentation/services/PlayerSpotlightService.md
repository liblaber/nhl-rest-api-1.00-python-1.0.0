# PlayerSpotlightService

A list of all methods in the `PlayerSpotlightService` service. Click on the method name to view detailed information about that method.

| Methods                                       | Description                                            |
| :-------------------------------------------- | :----------------------------------------------------- |
| [get_player_spotlight](#get_player_spotlight) | Retrieve information about players in the "spotlight". |

## get_player_spotlight

Retrieve information about players in the "spotlight".

- HTTP Method: `GET`
- Endpoint: `/v1/player-spotlight`

**Return Type**

`dict`

**Example Usage Code Snippet**

```python
from nhl import Nhl, Environment

sdk = Nhl(
    base_url=Environment.DEFAULT.value
)

result = sdk.player_spotlight.get_player_spotlight()

print(result)
```
