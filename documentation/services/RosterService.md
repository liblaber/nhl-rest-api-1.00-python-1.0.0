# RosterService

A list of all methods in the `RosterService` service. Click on the method name to view detailed information about that method.

| Methods                                                 | Description                                                       |
| :------------------------------------------------------ | :---------------------------------------------------------------- |
| [get_current_team_roster](#get_current_team_roster)     | Retrieve the roster for a specific team as of the current moment. |
| [get_team_roster_by_season](#get_team_roster_by_season) | Retrieve the roster for a specific team and season.               |

## get_current_team_roster

Retrieve the roster for a specific team as of the current moment.

- HTTP Method: `GET`
- Endpoint: `/v1/roster/{team}/current`

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

result = sdk.roster.get_current_team_roster(team="team")

print(result)
```

## get_team_roster_by_season

Retrieve the roster for a specific team and season.

- HTTP Method: `GET`
- Endpoint: `/v1/roster/{team}/{season}`

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

result = sdk.roster.get_team_roster_by_season(
    team="team",
    season=5
)

print(result)
```
