# StatsService

A list of all methods in the `StatsService` service. Click on the method name to view detailed information about that method.

| Methods                           | Description |
| :-------------------------------- | :---------- |
| [get_stat_types](#get_stat_types) |             |

## get_stat_types

- HTTP Method: `GET`
- Endpoint: `/statTypes`

**Return Type**

`List[StatTypes]`

**Example Usage Code Snippet**

```python
from nhl import Nhl, Environment

sdk = Nhl(
    base_url=Environment.DEFAULT.value
)

result = sdk.stats.get_stat_types()

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->