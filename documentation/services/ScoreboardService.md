# ScoreboardService

A list of all methods in the `ScoreboardService` service. Click on the method name to view detailed information about that method.

| Methods                                                     | Description                                                           |
| :---------------------------------------------------------- | :-------------------------------------------------------------------- |
| [get_current_team_scoreboard](#get_current_team_scoreboard) | Retrieve the scoreboard for a specific team as of the current moment. |

## get_current_team_scoreboard

Retrieve the scoreboard for a specific team as of the current moment.

- HTTP Method: `GET`
- Endpoint: `/v1/scoreboard/{team}/now`

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

result = sdk.scoreboard.get_current_team_scoreboard(team="team")

print(result)
```
