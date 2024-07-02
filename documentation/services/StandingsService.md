# StandingsService

A list of all methods in the `StandingsService` service. Click on the method name to view detailed information about that method.

| Methods                                         | Description                                        |
| :---------------------------------------------- | :------------------------------------------------- |
| [get_current_standings](#get_current_standings) | Retrieve the standings as of the current moment.   |
| [get_standings_by_date](#get_standings_by_date) | Retrieve the standings for a specific date.        |
| [get_standings_season](#get_standings_season)   | Retrieves information for each season's standings. |

## get_current_standings

Retrieve the standings as of the current moment.

- HTTP Method: `GET`
- Endpoint: `/v1/standings/now`

**Return Type**

`dict`

**Example Usage Code Snippet**

```python
from nhl import Nhl, Environment

sdk = Nhl(
    base_url=Environment.DEFAULT.value
)

result = sdk.standings.get_current_standings()

print(result)
```

## get_standings_by_date

Retrieve the standings for a specific date.

- HTTP Method: `GET`
- Endpoint: `/v1/standings/{date}`

**Parameters**

| Name   | Type | Required | Description               |
| :----- | :--- | :------- | :------------------------ |
| date\_ | str  | ✅       | Date in YYYY-MM-DD format |

**Return Type**

`dict`

**Example Usage Code Snippet**

```python
from nhl import Nhl, Environment

sdk = Nhl(
    base_url=Environment.DEFAULT.value
)

result = sdk.standings.get_standings_by_date(date_="date")

print(result)
```

## get_standings_season

Retrieves information for each season's standings.

- HTTP Method: `GET`
- Endpoint: `/v1/standings-season`

**Return Type**

`dict`

**Example Usage Code Snippet**

```python
from nhl import Nhl, Environment

sdk = Nhl(
    base_url=Environment.DEFAULT.value
)

result = sdk.standings.get_standings_season()

print(result)
```
