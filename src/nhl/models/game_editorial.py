# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .game_editorial_keyword import GameEditorialKeyword
from .photo import Photo


class TokenDataType(Enum):
    """An enumeration representing different categories.

    :cvar HYPERLINK: "hyperLink"
    :vartype HYPERLINK: str
    :cvar PLAYERCARD: "playerCard"
    :vartype PLAYERCARD: str
    """

    HYPERLINK = "hyperLink"
    PLAYERCARD = "playerCard"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, TokenDataType._member_map_.values()))


@JsonMap(
    {
        "token_guid": "tokenGUID",
        "type_": "type",
        "id_": "id",
        "team_id": "teamId",
        "seo_name": "seoName",
        "href_mobile": "hrefMobile",
    }
)
class TokenData(BaseModel):
    """TokenData

    :param token_guid: token_guid, defaults to None
    :type token_guid: str, optional
    :param type_: type_, defaults to None
    :type type_: TokenDataType, optional
    :param id_: id_, defaults to None
    :type id_: str, optional
    :param team_id: team_id, defaults to None
    :type team_id: str, optional
    :param name: name, defaults to None
    :type name: str, optional
    :param seo_name: seo_name, defaults to None
    :type seo_name: str, optional
    :param href: href, defaults to None
    :type href: str, optional
    :param href_mobile: href_mobile, defaults to None
    :type href_mobile: str, optional
    """

    def __init__(
        self,
        token_guid: str = None,
        type_: TokenDataType = None,
        id_: str = None,
        team_id: str = None,
        name: str = None,
        seo_name: str = None,
        href: str = None,
        href_mobile: str = None,
    ):
        if token_guid is not None:
            self.token_guid = token_guid
        if type_ is not None:
            self.type_ = self._enum_matching(type_, TokenDataType.list(), "type_")
        if id_ is not None:
            self.id_ = id_
        if team_id is not None:
            self.team_id = team_id
        if name is not None:
            self.name = name
        if seo_name is not None:
            self.seo_name = seo_name
        if href is not None:
            self.href = href
        if href_mobile is not None:
            self.href_mobile = href_mobile


@JsonMap({})
class Contributors(BaseModel):
    """Contributors

    :param name: name, defaults to None
    :type name: str, optional
    :param twitter: twitter, defaults to None
    :type twitter: str, optional
    """

    def __init__(self, name: str = None, twitter: str = None):
        if name is not None:
            self.name = name
        if twitter is not None:
            self.twitter = twitter


@JsonMap({})
class Contributor(BaseModel):
    """Contributor

    :param contributors: contributors, defaults to None
    :type contributors: List[Contributors], optional
    :param source: source, defaults to None
    :type source: str, optional
    """

    def __init__(self, contributors: List[Contributors] = None, source: str = None):
        if contributors is not None:
            self.contributors = self._define_list(contributors, Contributors)
        if source is not None:
            self.source = source


@JsonMap({"type_": "type"})
class GameEditorialMedia(BaseModel):
    """GameEditorialMedia

    :param type_: type_, defaults to None
    :type type_: str, optional
    :param image: image, defaults to None
    :type image: Photo, optional
    """

    def __init__(self, type_: str = None, image: Photo = None):
        if type_ is not None:
            self.type_ = type_
        if image is not None:
            self.image = self._define_object(image, Photo)


@JsonMap(
    {
        "type_": "type",
        "date_": "date",
        "id_": "id",
        "seo_title": "seoTitle",
        "seo_description": "seoDescription",
        "seo_keywords": "seoKeywords",
        "token_data": "tokenData",
        "keywords_display": "keywordsDisplay",
        "keywords_all": "keywordsAll",
        "data_uri": "dataURI",
        "primary_keyword": "primaryKeyword",
    }
)
class GameEditorial(BaseModel):
    """GameEditorial

    :param type_: type_, defaults to None
    :type type_: str, optional
    :param state: state, defaults to None
    :type state: str, optional
    :param date_: date_, defaults to None
    :type date_: str, optional
    :param id_: id_, defaults to None
    :type id_: str, optional
    :param headline: headline, defaults to None
    :type headline: str, optional
    :param subhead: subhead, defaults to None
    :type subhead: str, optional
    :param seo_title: seo_title, defaults to None
    :type seo_title: str, optional
    :param seo_description: seo_description, defaults to None
    :type seo_description: str, optional
    :param seo_keywords: seo_keywords, defaults to None
    :type seo_keywords: str, optional
    :param slug: slug, defaults to None
    :type slug: str, optional
    :param commenting: commenting, defaults to None
    :type commenting: bool, optional
    :param tagline: tagline, defaults to None
    :type tagline: str, optional
    :param token_data: token_data, defaults to None
    :type token_data: TokenData, optional
    :param contributor: contributor, defaults to None
    :type contributor: Contributor, optional
    :param keywords_display: keywords_display, defaults to None
    :type keywords_display: List[GameEditorialKeyword], optional
    :param keywords_all: keywords_all, defaults to None
    :type keywords_all: List[GameEditorialKeyword], optional
    :param approval: approval, defaults to None
    :type approval: str, optional
    :param url: url, defaults to None
    :type url: str, optional
    :param data_uri: data_uri, defaults to None
    :type data_uri: str, optional
    :param primary_keyword: primary_keyword, defaults to None
    :type primary_keyword: GameEditorialKeyword, optional
    :param media: media, defaults to None
    :type media: GameEditorialMedia, optional
    :param preview: preview, defaults to None
    :type preview: str, optional
    """

    def __init__(
        self,
        type_: str = None,
        state: str = None,
        date_: str = None,
        id_: str = None,
        headline: str = None,
        subhead: str = None,
        seo_title: str = None,
        seo_description: str = None,
        seo_keywords: str = None,
        slug: str = None,
        commenting: bool = None,
        tagline: str = None,
        token_data: TokenData = None,
        contributor: Contributor = None,
        keywords_display: List[GameEditorialKeyword] = None,
        keywords_all: List[GameEditorialKeyword] = None,
        approval: str = None,
        url: str = None,
        data_uri: str = None,
        primary_keyword: GameEditorialKeyword = None,
        media: GameEditorialMedia = None,
        preview: str = None,
    ):
        if type_ is not None:
            self.type_ = type_
        if state is not None:
            self.state = state
        if date_ is not None:
            self.date_ = date_
        if id_ is not None:
            self.id_ = id_
        if headline is not None:
            self.headline = headline
        if subhead is not None:
            self.subhead = subhead
        if seo_title is not None:
            self.seo_title = seo_title
        if seo_description is not None:
            self.seo_description = seo_description
        if seo_keywords is not None:
            self.seo_keywords = seo_keywords
        if slug is not None:
            self.slug = slug
        if commenting is not None:
            self.commenting = commenting
        if tagline is not None:
            self.tagline = tagline
        if token_data is not None:
            self.token_data = self._define_object(token_data, TokenData)
        if contributor is not None:
            self.contributor = self._define_object(contributor, Contributor)
        if keywords_display is not None:
            self.keywords_display = self._define_list(
                keywords_display, GameEditorialKeyword
            )
        if keywords_all is not None:
            self.keywords_all = self._define_list(keywords_all, GameEditorialKeyword)
        if approval is not None:
            self.approval = approval
        if url is not None:
            self.url = url
        if data_uri is not None:
            self.data_uri = data_uri
        if primary_keyword is not None:
            self.primary_keyword = self._define_object(
                primary_keyword, GameEditorialKeyword
            )
        if media is not None:
            self.media = self._define_object(media, GameEditorialMedia)
        if preview is not None:
            self.preview = preview
