# Nhl Python SDK 1.0.0

Welcome to the Nhl SDK documentation. This guide will help you get started with integrating and using the Nhl SDK in your project.

## Versions

- API version: `1.0.0`
- SDK version: `1.0.0`

## About the API

This section provides documentation for the NHL Web API. Based on the unofficial documentation https://github.com/Zmalski/NHL-API-Reference

## Table of Contents

- [Setup & Configuration](#setup--configuration)
  - [Supported Language Versions](#supported-language-versions)
  - [Installation](#installation)
- [Environments](#environments)
  - [Setting an Environment](#setting-an-environment)
- [Services](#services)
- [Models](#models)

## Setup & Configuration

### Supported Language Versions

This SDK is compatible with the following versions: `Python >= 3.7`

### Installation

To get started with the SDK, we recommend installing using `pip`:

```bash
pip install nhl-client
```

## Environments

The SDK supports different environments for various stages of development and deployment.

Here are the available environments:

```py
production = "https://api-web.nhle.com"
```

## Setting an Environment

To configure the SDK to use a specific environment, you can set the base URL as follows:

```py
from nhl import Environment

sdk.set_base_url(Environment.production.value)
```

## Services

The SDK provides various services to interact with the API.

<details> 
<summary>Below is a list of all available services with links to their detailed documentation:</summary>

| Name                                                                       |
| :------------------------------------------------------------------------- |
| [PlayerService](documentation/services/PlayerService.md)                   |
| [SkaterStatsService](documentation/services/SkaterStatsService.md)         |
| [GoalieStatsService](documentation/services/GoalieStatsService.md)         |
| [PlayerSpotlightService](documentation/services/PlayerSpotlightService.md) |
| [StandingsService](documentation/services/StandingsService.md)             |
| [ClubStatsService](documentation/services/ClubStatsService.md)             |
| [ScoreboardService](documentation/services/ScoreboardService.md)           |
| [RosterService](documentation/services/RosterService.md)                   |
| [ScheduleService](documentation/services/ScheduleService.md)               |

</details>
<br/>
