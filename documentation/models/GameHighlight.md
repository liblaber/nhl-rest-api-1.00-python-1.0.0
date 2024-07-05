# GameHighlight

**Properties**

| Name              | Type                       | Required | Description |
| :---------------- | :------------------------- | :------- | :---------- |
| type\_            | GameHighlightType1         | ❌       |             |
| id\_              | str                        | ❌       |             |
| date\_            | str                        | ❌       |             |
| title             | str                        | ❌       |             |
| blurb             | str                        | ❌       |             |
| description       | str                        | ❌       |             |
| duration          | str                        | ❌       |             |
| auth_flow         | bool                       | ❌       |             |
| media_playback_id | str                        | ❌       |             |
| media_state       | str                        | ❌       |             |
| keywords          | List[GameEditorialKeyword] | ❌       |             |
| image             | Photo                      | ❌       |             |
| playbacks         | List[Playbacks]            | ❌       |             |

# GameHighlightType_1

**Properties**

| Name  | Type | Required | Description |
| :---- | :--- | :------- | :---------- |
| VIDEO | str  | ✅       | "video"     |

# Playbacks

**Properties**

| Name   | Type          | Required | Description |
| :----- | :------------ | :------- | :---------- |
| name   | PlaybacksName | ❌       |             |
| width  | str           | ❌       |             |
| height | str           | ❌       |             |
| url    | str           | ❌       |             |

# PlaybacksName

**Properties**

| Name                 | Type | Required | Description            |
| :------------------- | :--- | :------- | :--------------------- |
| FLASH_192K_320X180   | str  | ✅       | "FLASH_192K_320X180"   |
| FLASH_450K_400X224   | str  | ✅       | "FLASH_450K_400X224"   |
| FLASH_1200K_640X360  | str  | ✅       | "FLASH_1200K_640X360"  |
| FLASH_1800K_960X540  | str  | ✅       | "FLASH_1800K_960X540"  |
| HTTP_CLOUD_MOBILE    | str  | ✅       | "HTTP_CLOUD_MOBILE"    |
| HTTP_CLOUD_TABLET    | str  | ✅       | "HTTP_CLOUD_TABLET"    |
| HTTP_CLOUD_TABLET_60 | str  | ✅       | "HTTP_CLOUD_TABLET_60" |
| HTTP_CLOUD_WIRED     | str  | ✅       | "HTTP_CLOUD_WIRED"     |
| HTTP_CLOUD_WIRED_60  | str  | ✅       | "HTTP_CLOUD_WIRED_60"  |
| HTTP_CLOUD_WIRED_WEB | str  | ✅       | "HTTP_CLOUD_WIRED_WEB" |

<!-- This file was generated by liblab | https://liblab.com/ -->