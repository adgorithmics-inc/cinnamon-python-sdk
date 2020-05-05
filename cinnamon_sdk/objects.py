from typing import Union, List, Any
from datetime import datetime
from .internals.base_classes import BaseCinnamonObject, BaseCinnamonEdgesObject, BaseCinnamonField
from .internals.constants import CinnamonUndefined
from .internals import scalars
from . import enums

class CampaignTemplate(BaseCinnamonObject):
    class _API_FIELDS:
        class id(BaseCinnamonField):
            api_name = "id"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = None
            python_name = "id"
            scalar = scalars.ObjectId

        class creationDate(BaseCinnamonField):
            api_name = "creationDate"
            api_kind = "SCALAR"
            api_kind_name = "DateISO"
            python_iterable = None
            python_name = "creation_date"
            scalar = scalars.DateISO

        class lastChangeDate(BaseCinnamonField):
            api_name = "lastChangeDate"
            api_kind = "SCALAR"
            api_kind_name = "DateISO"
            python_iterable = None
            python_name = "last_change_date"
            scalar = scalars.DateISO

        class name(BaseCinnamonField):
            api_name = "name"
            api_kind = "SCALAR"
            api_kind_name = "NonEmptyString"
            python_iterable = None
            python_name = "name"
            scalar = scalars.NonEmptyString

        class description(BaseCinnamonField):
            api_name = "description"
            api_kind = "SCALAR"
            api_kind_name = "String"
            python_iterable = None
            python_name = "description"
            scalar = scalars.String

        class platform(BaseCinnamonField):
            api_name = "platform"
            api_kind = "ENUM"
            api_kind_name = "Platform"
            python_iterable = None
            python_name = "platform"

        class remoteId(BaseCinnamonField):
            api_name = "remoteId"
            api_kind = "SCALAR"
            api_kind_name = "String"
            python_iterable = None
            python_name = "remote_id"
            scalar = scalars.String

        class systemStatus(BaseCinnamonField):
            api_name = "systemStatus"
            api_kind = "ENUM"
            api_kind_name = "SystemStatus"
            python_iterable = None
            python_name = "system_status"

        class errors(BaseCinnamonField):
            api_name = "errors"
            api_kind = "SCALAR"
            api_kind_name = "JSONObject"
            python_iterable = list
            python_name = "errors"
            scalar = scalars.JSONObject

        class warnings(BaseCinnamonField):
            api_name = "warnings"
            api_kind = "SCALAR"
            api_kind_name = "JSONObject"
            python_iterable = list
            python_name = "warnings"
            scalar = scalars.JSONObject

        class kpi(BaseCinnamonField):
            api_name = "kpi"
            api_kind = "SCALAR"
            api_kind_name = "String"
            python_iterable = None
            python_name = "kpi"
            scalar = scalars.String

        class marketplace(BaseCinnamonField):
            api_name = "marketplace"
            api_kind = "OBJECT"
            api_kind_name = "Marketplace"
            python_iterable = None
            python_name = "marketplace"

        class marketingCampaigns(BaseCinnamonField):
            api_name = "marketingCampaigns"
            api_kind = "OBJECT"
            api_kind_name = "MarketingCampaignConnection"
            python_iterable = None
            python_name = "marketing_campaigns"

        class GCPXHistory(BaseCinnamonField):
            api_name = "GCPXHistory"
            api_kind = "OBJECT"
            api_kind_name = "GCPXConnection"
            python_iterable = None
            python_name = "gcpx_history"

        class currentGCPX(BaseCinnamonField):
            api_name = "currentGCPX"
            api_kind = "OBJECT"
            api_kind_name = "GCPX"
            python_iterable = None
            python_name = "current_gcpx"

    id: str
    creation_date: datetime
    last_change_date: datetime
    name: str
    description: str
    platform: enums.Platform
    remote_id: str
    system_status: enums.SystemStatus
    errors: List[dict]
    warnings: List[dict]
    kpi: Union[str, None, CinnamonUndefined]
    marketplace: "Marketplace"
    marketing_campaigns: "MarketingCampaignConnection"
    gcpx_history: "GCPXConnection"
    current_gcpx: Union["GCPX", None, CinnamonUndefined]


class Marketplace(BaseCinnamonObject):
    class _API_FIELDS:
        class id(BaseCinnamonField):
            api_name = "id"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = None
            python_name = "id"
            scalar = scalars.ObjectId

        class creationDate(BaseCinnamonField):
            api_name = "creationDate"
            api_kind = "SCALAR"
            api_kind_name = "DateISO"
            python_iterable = None
            python_name = "creation_date"
            scalar = scalars.DateISO

        class lastChangeDate(BaseCinnamonField):
            api_name = "lastChangeDate"
            api_kind = "SCALAR"
            api_kind_name = "DateISO"
            python_iterable = None
            python_name = "last_change_date"
            scalar = scalars.DateISO

        class name(BaseCinnamonField):
            api_name = "name"
            api_kind = "SCALAR"
            api_kind_name = "NonEmptyString"
            python_iterable = None
            python_name = "name"
            scalar = scalars.NonEmptyString

        class systemStatus(BaseCinnamonField):
            api_name = "systemStatus"
            api_kind = "ENUM"
            api_kind_name = "SystemStatus"
            python_iterable = None
            python_name = "system_status"

        class errors(BaseCinnamonField):
            api_name = "errors"
            api_kind = "SCALAR"
            api_kind_name = "JSONObject"
            python_iterable = list
            python_name = "errors"
            scalar = scalars.JSONObject

        class warnings(BaseCinnamonField):
            api_name = "warnings"
            api_kind = "SCALAR"
            api_kind_name = "JSONObject"
            python_iterable = list
            python_name = "warnings"
            scalar = scalars.JSONObject

        class currencyCode(BaseCinnamonField):
            api_name = "currencyCode"
            api_kind = "SCALAR"
            api_kind_name = "String"
            python_iterable = None
            python_name = "currency_code"
            scalar = scalars.String

        class currencySymbol(BaseCinnamonField):
            api_name = "currencySymbol"
            api_kind = "SCALAR"
            api_kind_name = "String"
            python_iterable = None
            python_name = "currency_symbol"
            scalar = scalars.String

        class currencyOffset(BaseCinnamonField):
            api_name = "currencyOffset"
            api_kind = "SCALAR"
            api_kind_name = "Int"
            python_iterable = None
            python_name = "currency_offset"
            scalar = scalars.Int

        class organization(BaseCinnamonField):
            api_name = "organization"
            api_kind = "OBJECT"
            api_kind_name = "Organization"
            python_iterable = None
            python_name = "organization"

        class mediaChannels(BaseCinnamonField):
            api_name = "mediaChannels"
            api_kind = "OBJECT"
            api_kind_name = "MediaChannelConnection"
            python_iterable = None
            python_name = "media_channels"

        class campaignTemplates(BaseCinnamonField):
            api_name = "campaignTemplates"
            api_kind = "OBJECT"
            api_kind_name = "CampaignTemplateConnection"
            python_iterable = None
            python_name = "campaign_templates"

        class vendors(BaseCinnamonField):
            api_name = "vendors"
            api_kind = "OBJECT"
            api_kind_name = "VendorConnection"
            python_iterable = None
            python_name = "vendors"

        class vendorTokens(BaseCinnamonField):
            api_name = "vendorTokens"
            api_kind = "OBJECT"
            api_kind_name = "VendorTokenConnection"
            python_iterable = None
            python_name = "vendor_tokens"

        class creativeTemplates(BaseCinnamonField):
            api_name = "creativeTemplates"
            api_kind = "OBJECT"
            api_kind_name = "CreativeTemplateConnection"
            python_iterable = None
            python_name = "creative_templates"

        class products(BaseCinnamonField):
            api_name = "products"
            api_kind = "OBJECT"
            api_kind_name = "ProductConnection"
            python_iterable = None
            python_name = "products"

    id: str
    creation_date: datetime
    last_change_date: datetime
    name: str
    system_status: enums.SystemStatus
    errors: List[dict]
    warnings: List[dict]
    currency_code: Union[str, None, CinnamonUndefined]
    currency_symbol: Union[str, None, CinnamonUndefined]
    currency_offset: Union[int, None, CinnamonUndefined]
    organization: Union["Organization", None, CinnamonUndefined]
    media_channels: "MediaChannelConnection"
    campaign_templates: "CampaignTemplateConnection"
    vendors: "VendorConnection"
    vendor_tokens: "VendorTokenConnection"
    creative_templates: "CreativeTemplateConnection"
    products: "ProductConnection"


class EntitlementResource(BaseCinnamonObject):
    class _API_FIELDS:
        class id(BaseCinnamonField):
            api_name = "id"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = None
            python_name = "id"
            scalar = scalars.ObjectId

        class creationDate(BaseCinnamonField):
            api_name = "creationDate"
            api_kind = "SCALAR"
            api_kind_name = "DateISO"
            python_iterable = None
            python_name = "creation_date"
            scalar = scalars.DateISO

        class lastChangeDate(BaseCinnamonField):
            api_name = "lastChangeDate"
            api_kind = "SCALAR"
            api_kind_name = "DateISO"
            python_iterable = None
            python_name = "last_change_date"
            scalar = scalars.DateISO

        class name(BaseCinnamonField):
            api_name = "name"
            api_kind = "SCALAR"
            api_kind_name = "NonEmptyString"
            python_iterable = None
            python_name = "name"
            scalar = scalars.NonEmptyString

        class systemStatus(BaseCinnamonField):
            api_name = "systemStatus"
            api_kind = "ENUM"
            api_kind_name = "SystemStatus"
            python_iterable = None
            python_name = "system_status"

        class errors(BaseCinnamonField):
            api_name = "errors"
            api_kind = "SCALAR"
            api_kind_name = "JSONObject"
            python_iterable = list
            python_name = "errors"
            scalar = scalars.JSONObject

        class warnings(BaseCinnamonField):
            api_name = "warnings"
            api_kind = "SCALAR"
            api_kind_name = "JSONObject"
            python_iterable = list
            python_name = "warnings"
            scalar = scalars.JSONObject

    id: str
    creation_date: datetime
    last_change_date: datetime
    name: str
    system_status: enums.SystemStatus
    errors: List[dict]
    warnings: List[dict]


class Organization(BaseCinnamonObject):
    class _API_FIELDS:
        class id(BaseCinnamonField):
            api_name = "id"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = None
            python_name = "id"
            scalar = scalars.ObjectId

        class creationDate(BaseCinnamonField):
            api_name = "creationDate"
            api_kind = "SCALAR"
            api_kind_name = "DateISO"
            python_iterable = None
            python_name = "creation_date"
            scalar = scalars.DateISO

        class lastChangeDate(BaseCinnamonField):
            api_name = "lastChangeDate"
            api_kind = "SCALAR"
            api_kind_name = "DateISO"
            python_iterable = None
            python_name = "last_change_date"
            scalar = scalars.DateISO

        class name(BaseCinnamonField):
            api_name = "name"
            api_kind = "SCALAR"
            api_kind_name = "NonEmptyString"
            python_iterable = None
            python_name = "name"
            scalar = scalars.NonEmptyString

        class systemStatus(BaseCinnamonField):
            api_name = "systemStatus"
            api_kind = "ENUM"
            api_kind_name = "SystemStatus"
            python_iterable = None
            python_name = "system_status"

        class errors(BaseCinnamonField):
            api_name = "errors"
            api_kind = "SCALAR"
            api_kind_name = "JSONObject"
            python_iterable = list
            python_name = "errors"
            scalar = scalars.JSONObject

        class warnings(BaseCinnamonField):
            api_name = "warnings"
            api_kind = "SCALAR"
            api_kind_name = "JSONObject"
            python_iterable = list
            python_name = "warnings"
            scalar = scalars.JSONObject

        class tier(BaseCinnamonField):
            api_name = "tier"
            api_kind = "ENUM"
            api_kind_name = "OrganizationTierEnum"
            python_iterable = None
            python_name = "tier"

        class users(BaseCinnamonField):
            api_name = "users"
            api_kind = "OBJECT"
            api_kind_name = "UserConnection"
            python_iterable = None
            python_name = "users"

        class marketplaces(BaseCinnamonField):
            api_name = "marketplaces"
            api_kind = "OBJECT"
            api_kind_name = "MarketplaceConnection"
            python_iterable = None
            python_name = "marketplaces"

    id: str
    creation_date: datetime
    last_change_date: datetime
    name: str
    system_status: enums.SystemStatus
    errors: List[dict]
    warnings: List[dict]
    tier: enums.OrganizationTierEnum
    users: "UserConnection"
    marketplaces: "MarketplaceConnection"


class UserConnection(BaseCinnamonObject, BaseCinnamonEdgesObject):
    class _API_FIELDS:
        class edges(BaseCinnamonField):
            api_name = "edges"
            api_kind = "OBJECT"
            api_kind_name = "UserEdge"
            python_iterable = list
            python_name = "edges"

        class pageInfo(BaseCinnamonField):
            api_name = "pageInfo"
            api_kind = "OBJECT"
            api_kind_name = "PageInfo"
            python_iterable = None
            python_name = "page_info"

        class totalCount(BaseCinnamonField):
            api_name = "totalCount"
            api_kind = "SCALAR"
            api_kind_name = "Int"
            python_iterable = None
            python_name = "total_count"
            scalar = scalars.Int

    edges: List["UserEdge"]
    page_info: "PageInfo"
    total_count: int


class UserEdge(BaseCinnamonObject):
    class _API_FIELDS:
        class node(BaseCinnamonField):
            api_name = "node"
            api_kind = "OBJECT"
            api_kind_name = "User"
            python_iterable = None
            python_name = "node"

        class cursor(BaseCinnamonField):
            api_name = "cursor"
            api_kind = "SCALAR"
            api_kind_name = "String"
            python_iterable = None
            python_name = "cursor"
            scalar = scalars.String

    node: "User"
    cursor: str


class User(BaseCinnamonObject):
    class _API_FIELDS:
        class id(BaseCinnamonField):
            api_name = "id"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = None
            python_name = "id"
            scalar = scalars.ObjectId

        class creationDate(BaseCinnamonField):
            api_name = "creationDate"
            api_kind = "SCALAR"
            api_kind_name = "DateISO"
            python_iterable = None
            python_name = "creation_date"
            scalar = scalars.DateISO

        class lastChangeDate(BaseCinnamonField):
            api_name = "lastChangeDate"
            api_kind = "SCALAR"
            api_kind_name = "DateISO"
            python_iterable = None
            python_name = "last_change_date"
            scalar = scalars.DateISO

        class email(BaseCinnamonField):
            api_name = "email"
            api_kind = "SCALAR"
            api_kind_name = "NonEmptyString"
            python_iterable = None
            python_name = "email"
            scalar = scalars.NonEmptyString

        class firstName(BaseCinnamonField):
            api_name = "firstName"
            api_kind = "SCALAR"
            api_kind_name = "NonEmptyString"
            python_iterable = None
            python_name = "first_name"
            scalar = scalars.NonEmptyString

        class lastName(BaseCinnamonField):
            api_name = "lastName"
            api_kind = "SCALAR"
            api_kind_name = "NonEmptyString"
            python_iterable = None
            python_name = "last_name"
            scalar = scalars.NonEmptyString

        class organizations(BaseCinnamonField):
            api_name = "organizations"
            api_kind = "OBJECT"
            api_kind_name = "OrganizationConnection"
            python_iterable = None
            python_name = "organizations"

        class entitlements(BaseCinnamonField):
            api_name = "entitlements"
            api_kind = "OBJECT"
            api_kind_name = "EntitlementConnection"
            python_iterable = None
            python_name = "entitlements"

        class noticeOptIn(BaseCinnamonField):
            api_name = "noticeOptIn"
            api_kind = "SCALAR"
            api_kind_name = "Boolean"
            python_iterable = None
            python_name = "notice_opt_in"
            scalar = scalars.Boolean

        class newsletterOptIn(BaseCinnamonField):
            api_name = "newsletterOptIn"
            api_kind = "SCALAR"
            api_kind_name = "Boolean"
            python_iterable = None
            python_name = "newsletter_opt_in"
            scalar = scalars.Boolean

    id: str
    creation_date: datetime
    last_change_date: datetime
    email: str
    first_name: Union[str, None, CinnamonUndefined]
    last_name: Union[str, None, CinnamonUndefined]
    organizations: "OrganizationConnection"
    entitlements: "EntitlementConnection"
    notice_opt_in: bool
    newsletter_opt_in: bool


class Me(BaseCinnamonObject):
    class _API_FIELDS:
        class id(BaseCinnamonField):
            api_name = "id"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = None
            python_name = "id"
            scalar = scalars.ObjectId

        class creationDate(BaseCinnamonField):
            api_name = "creationDate"
            api_kind = "SCALAR"
            api_kind_name = "DateISO"
            python_iterable = None
            python_name = "creation_date"
            scalar = scalars.DateISO

        class lastChangeDate(BaseCinnamonField):
            api_name = "lastChangeDate"
            api_kind = "SCALAR"
            api_kind_name = "DateISO"
            python_iterable = None
            python_name = "last_change_date"
            scalar = scalars.DateISO

    id: str
    creation_date: datetime
    last_change_date: datetime


class OrganizationConnection(BaseCinnamonObject, BaseCinnamonEdgesObject):
    class _API_FIELDS:
        class edges(BaseCinnamonField):
            api_name = "edges"
            api_kind = "OBJECT"
            api_kind_name = "OrganizationEdge"
            python_iterable = list
            python_name = "edges"

        class pageInfo(BaseCinnamonField):
            api_name = "pageInfo"
            api_kind = "OBJECT"
            api_kind_name = "PageInfo"
            python_iterable = None
            python_name = "page_info"

        class totalCount(BaseCinnamonField):
            api_name = "totalCount"
            api_kind = "SCALAR"
            api_kind_name = "Int"
            python_iterable = None
            python_name = "total_count"
            scalar = scalars.Int

    edges: List["OrganizationEdge"]
    page_info: "PageInfo"
    total_count: int


class OrganizationEdge(BaseCinnamonObject):
    class _API_FIELDS:
        class node(BaseCinnamonField):
            api_name = "node"
            api_kind = "OBJECT"
            api_kind_name = "Organization"
            python_iterable = None
            python_name = "node"

        class cursor(BaseCinnamonField):
            api_name = "cursor"
            api_kind = "SCALAR"
            api_kind_name = "String"
            python_iterable = None
            python_name = "cursor"
            scalar = scalars.String

    node: "Organization"
    cursor: str


class PageInfo(BaseCinnamonObject):
    class _API_FIELDS:
        class endCursor(BaseCinnamonField):
            api_name = "endCursor"
            api_kind = "SCALAR"
            api_kind_name = "String"
            python_iterable = None
            python_name = "end_cursor"
            scalar = scalars.String

        class startCursor(BaseCinnamonField):
            api_name = "startCursor"
            api_kind = "SCALAR"
            api_kind_name = "String"
            python_iterable = None
            python_name = "start_cursor"
            scalar = scalars.String

        class hasNextPage(BaseCinnamonField):
            api_name = "hasNextPage"
            api_kind = "SCALAR"
            api_kind_name = "Boolean"
            python_iterable = None
            python_name = "has_next_page"
            scalar = scalars.Boolean

        class hasPreviousPage(BaseCinnamonField):
            api_name = "hasPreviousPage"
            api_kind = "SCALAR"
            api_kind_name = "Boolean"
            python_iterable = None
            python_name = "has_previous_page"
            scalar = scalars.Boolean

    end_cursor: Union[str, None, CinnamonUndefined]
    start_cursor: Union[str, None, CinnamonUndefined]
    has_next_page: bool
    has_previous_page: bool


class EntitlementConnection(BaseCinnamonObject, BaseCinnamonEdgesObject):
    class _API_FIELDS:
        class edges(BaseCinnamonField):
            api_name = "edges"
            api_kind = "OBJECT"
            api_kind_name = "EntitlementEdge"
            python_iterable = list
            python_name = "edges"

        class pageInfo(BaseCinnamonField):
            api_name = "pageInfo"
            api_kind = "OBJECT"
            api_kind_name = "PageInfo"
            python_iterable = None
            python_name = "page_info"

        class totalCount(BaseCinnamonField):
            api_name = "totalCount"
            api_kind = "SCALAR"
            api_kind_name = "Int"
            python_iterable = None
            python_name = "total_count"
            scalar = scalars.Int

    edges: List["EntitlementEdge"]
    page_info: "PageInfo"
    total_count: int


class EntitlementEdge(BaseCinnamonObject):
    class _API_FIELDS:
        class node(BaseCinnamonField):
            api_name = "node"
            api_kind = "OBJECT"
            api_kind_name = "Entitlement"
            python_iterable = None
            python_name = "node"

        class cursor(BaseCinnamonField):
            api_name = "cursor"
            api_kind = "SCALAR"
            api_kind_name = "String"
            python_iterable = None
            python_name = "cursor"
            scalar = scalars.String

    node: "Entitlement"
    cursor: str


class Entitlement(BaseCinnamonObject):
    class _API_FIELDS:
        class id(BaseCinnamonField):
            api_name = "id"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = None
            python_name = "id"
            scalar = scalars.ObjectId

        class creationDate(BaseCinnamonField):
            api_name = "creationDate"
            api_kind = "SCALAR"
            api_kind_name = "DateISO"
            python_iterable = None
            python_name = "creation_date"
            scalar = scalars.DateISO

        class lastChangeDate(BaseCinnamonField):
            api_name = "lastChangeDate"
            api_kind = "SCALAR"
            api_kind_name = "DateISO"
            python_iterable = None
            python_name = "last_change_date"
            scalar = scalars.DateISO

        class type(BaseCinnamonField):
            api_name = "type"
            api_kind = "ENUM"
            api_kind_name = "EntitlementResourceTypeEnum"
            python_iterable = None
            python_name = "type"

        class permissions(BaseCinnamonField):
            api_name = "permissions"
            api_kind = "ENUM"
            api_kind_name = "AuthPermission"
            python_iterable = list
            python_name = "permissions"

        class user(BaseCinnamonField):
            api_name = "user"
            api_kind = "OBJECT"
            api_kind_name = "User"
            python_iterable = None
            python_name = "user"

        class resource(BaseCinnamonField):
            api_name = "resource"
            api_kind = "INTERFACE"
            api_kind_name = "EntitlementResource"
            python_iterable = None
            python_name = "resource"

    id: str
    creation_date: datetime
    last_change_date: datetime
    type: enums.EntitlementResourceTypeEnum
    permissions: List[enums.AuthPermission]
    user: "User"
    resource: Any


class MarketplaceConnection(BaseCinnamonObject, BaseCinnamonEdgesObject):
    class _API_FIELDS:
        class edges(BaseCinnamonField):
            api_name = "edges"
            api_kind = "OBJECT"
            api_kind_name = "MarketplaceEdge"
            python_iterable = list
            python_name = "edges"

        class pageInfo(BaseCinnamonField):
            api_name = "pageInfo"
            api_kind = "OBJECT"
            api_kind_name = "PageInfo"
            python_iterable = None
            python_name = "page_info"

        class totalCount(BaseCinnamonField):
            api_name = "totalCount"
            api_kind = "SCALAR"
            api_kind_name = "Int"
            python_iterable = None
            python_name = "total_count"
            scalar = scalars.Int

    edges: List["MarketplaceEdge"]
    page_info: "PageInfo"
    total_count: int


class MarketplaceEdge(BaseCinnamonObject):
    class _API_FIELDS:
        class node(BaseCinnamonField):
            api_name = "node"
            api_kind = "OBJECT"
            api_kind_name = "Marketplace"
            python_iterable = None
            python_name = "node"

        class cursor(BaseCinnamonField):
            api_name = "cursor"
            api_kind = "SCALAR"
            api_kind_name = "String"
            python_iterable = None
            python_name = "cursor"
            scalar = scalars.String

    node: "Marketplace"
    cursor: str


class MediaChannelConnection(BaseCinnamonObject, BaseCinnamonEdgesObject):
    class _API_FIELDS:
        class edges(BaseCinnamonField):
            api_name = "edges"
            api_kind = "OBJECT"
            api_kind_name = "MediaChannelEdge"
            python_iterable = list
            python_name = "edges"

        class pageInfo(BaseCinnamonField):
            api_name = "pageInfo"
            api_kind = "OBJECT"
            api_kind_name = "PageInfo"
            python_iterable = None
            python_name = "page_info"

        class totalCount(BaseCinnamonField):
            api_name = "totalCount"
            api_kind = "SCALAR"
            api_kind_name = "Int"
            python_iterable = None
            python_name = "total_count"
            scalar = scalars.Int

    edges: List["MediaChannelEdge"]
    page_info: "PageInfo"
    total_count: int


class MediaChannelEdge(BaseCinnamonObject):
    class _API_FIELDS:
        class node(BaseCinnamonField):
            api_name = "node"
            api_kind = "OBJECT"
            api_kind_name = "MediaChannel"
            python_iterable = None
            python_name = "node"

        class cursor(BaseCinnamonField):
            api_name = "cursor"
            api_kind = "SCALAR"
            api_kind_name = "String"
            python_iterable = None
            python_name = "cursor"
            scalar = scalars.String

    node: "MediaChannel"
    cursor: str


class MediaChannel(BaseCinnamonObject):
    class _API_FIELDS:
        class id(BaseCinnamonField):
            api_name = "id"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = None
            python_name = "id"
            scalar = scalars.ObjectId

        class creationDate(BaseCinnamonField):
            api_name = "creationDate"
            api_kind = "SCALAR"
            api_kind_name = "DateISO"
            python_iterable = None
            python_name = "creation_date"
            scalar = scalars.DateISO

        class lastChangeDate(BaseCinnamonField):
            api_name = "lastChangeDate"
            api_kind = "SCALAR"
            api_kind_name = "DateISO"
            python_iterable = None
            python_name = "last_change_date"
            scalar = scalars.DateISO

        class name(BaseCinnamonField):
            api_name = "name"
            api_kind = "SCALAR"
            api_kind_name = "NonEmptyString"
            python_iterable = None
            python_name = "name"
            scalar = scalars.NonEmptyString

        class systemStatus(BaseCinnamonField):
            api_name = "systemStatus"
            api_kind = "ENUM"
            api_kind_name = "SystemStatus"
            python_iterable = None
            python_name = "system_status"

        class errors(BaseCinnamonField):
            api_name = "errors"
            api_kind = "SCALAR"
            api_kind_name = "JSONObject"
            python_iterable = list
            python_name = "errors"
            scalar = scalars.JSONObject

        class warnings(BaseCinnamonField):
            api_name = "warnings"
            api_kind = "SCALAR"
            api_kind_name = "JSONObject"
            python_iterable = list
            python_name = "warnings"
            scalar = scalars.JSONObject

        class platform(BaseCinnamonField):
            api_name = "platform"
            api_kind = "ENUM"
            api_kind_name = "Platform"
            python_iterable = None
            python_name = "platform"

        class remoteId(BaseCinnamonField):
            api_name = "remoteId"
            api_kind = "SCALAR"
            api_kind_name = "String"
            python_iterable = None
            python_name = "remote_id"
            scalar = scalars.String

        class remoteState(BaseCinnamonField):
            api_name = "remoteState"
            api_kind = "SCALAR"
            api_kind_name = "JSONObject"
            python_iterable = None
            python_name = "remote_state"
            scalar = scalars.JSONObject

        class currencyCode(BaseCinnamonField):
            api_name = "currencyCode"
            api_kind = "SCALAR"
            api_kind_name = "String"
            python_iterable = None
            python_name = "currency_code"
            scalar = scalars.String

        class currencySymbol(BaseCinnamonField):
            api_name = "currencySymbol"
            api_kind = "SCALAR"
            api_kind_name = "NonEmptyString"
            python_iterable = None
            python_name = "currency_symbol"
            scalar = scalars.NonEmptyString

        class currencyOffset(BaseCinnamonField):
            api_name = "currencyOffset"
            api_kind = "SCALAR"
            api_kind_name = "Int"
            python_iterable = None
            python_name = "currency_offset"
            scalar = scalars.Int

        class timezone(BaseCinnamonField):
            api_name = "timezone"
            api_kind = "SCALAR"
            api_kind_name = "NonEmptyString"
            python_iterable = None
            python_name = "timezone"
            scalar = scalars.NonEmptyString

        class tokenStatus(BaseCinnamonField):
            api_name = "tokenStatus"
            api_kind = "ENUM"
            api_kind_name = "TokenStatus"
            python_iterable = None
            python_name = "token_status"

        class catalogs(BaseCinnamonField):
            api_name = "catalogs"
            api_kind = "OBJECT"
            api_kind_name = "CatalogConnection"
            python_iterable = None
            python_name = "catalogs"

        class marketplace(BaseCinnamonField):
            api_name = "marketplace"
            api_kind = "OBJECT"
            api_kind_name = "Marketplace"
            python_iterable = None
            python_name = "marketplace"

    id: str
    creation_date: datetime
    last_change_date: datetime
    name: str
    system_status: enums.SystemStatus
    errors: List[dict]
    warnings: List[dict]
    platform: enums.Platform
    remote_id: Union[str, None, CinnamonUndefined]
    remote_state: dict
    currency_code: Union[str, None, CinnamonUndefined]
    currency_symbol: Union[str, None, CinnamonUndefined]
    currency_offset: Union[int, None, CinnamonUndefined]
    timezone: Union[str, None, CinnamonUndefined]
    token_status: enums.TokenStatus
    catalogs: "CatalogConnection"
    marketplace: Union["Marketplace", None, CinnamonUndefined]


class CatalogConnection(BaseCinnamonObject, BaseCinnamonEdgesObject):
    class _API_FIELDS:
        class edges(BaseCinnamonField):
            api_name = "edges"
            api_kind = "OBJECT"
            api_kind_name = "CatalogEdge"
            python_iterable = list
            python_name = "edges"

        class pageInfo(BaseCinnamonField):
            api_name = "pageInfo"
            api_kind = "OBJECT"
            api_kind_name = "PageInfo"
            python_iterable = None
            python_name = "page_info"

        class totalCount(BaseCinnamonField):
            api_name = "totalCount"
            api_kind = "SCALAR"
            api_kind_name = "Int"
            python_iterable = None
            python_name = "total_count"
            scalar = scalars.Int

    edges: List["CatalogEdge"]
    page_info: "PageInfo"
    total_count: int


class CatalogEdge(BaseCinnamonObject):
    class _API_FIELDS:
        class node(BaseCinnamonField):
            api_name = "node"
            api_kind = "OBJECT"
            api_kind_name = "Catalog"
            python_iterable = None
            python_name = "node"

        class cursor(BaseCinnamonField):
            api_name = "cursor"
            api_kind = "SCALAR"
            api_kind_name = "String"
            python_iterable = None
            python_name = "cursor"
            scalar = scalars.String

    node: "Catalog"
    cursor: str


class Catalog(BaseCinnamonObject):
    class _API_FIELDS:
        class id(BaseCinnamonField):
            api_name = "id"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = None
            python_name = "id"
            scalar = scalars.ObjectId

        class creationDate(BaseCinnamonField):
            api_name = "creationDate"
            api_kind = "SCALAR"
            api_kind_name = "DateISO"
            python_iterable = None
            python_name = "creation_date"
            scalar = scalars.DateISO

        class lastChangeDate(BaseCinnamonField):
            api_name = "lastChangeDate"
            api_kind = "SCALAR"
            api_kind_name = "DateISO"
            python_iterable = None
            python_name = "last_change_date"
            scalar = scalars.DateISO

        class name(BaseCinnamonField):
            api_name = "name"
            api_kind = "SCALAR"
            api_kind_name = "NonEmptyString"
            python_iterable = None
            python_name = "name"
            scalar = scalars.NonEmptyString

        class catalogType(BaseCinnamonField):
            api_name = "catalogType"
            api_kind = "ENUM"
            api_kind_name = "CatalogType"
            python_iterable = None
            python_name = "catalog_type"

        class remoteId(BaseCinnamonField):
            api_name = "remoteId"
            api_kind = "SCALAR"
            api_kind_name = "String"
            python_iterable = None
            python_name = "remote_id"
            scalar = scalars.String

        class systemStatus(BaseCinnamonField):
            api_name = "systemStatus"
            api_kind = "ENUM"
            api_kind_name = "SystemStatus"
            python_iterable = None
            python_name = "system_status"

        class remoteState(BaseCinnamonField):
            api_name = "remoteState"
            api_kind = "SCALAR"
            api_kind_name = "JSONObject"
            python_iterable = None
            python_name = "remote_state"
            scalar = scalars.JSONObject

        class dataFeedId(BaseCinnamonField):
            api_name = "dataFeedId"
            api_kind = "SCALAR"
            api_kind_name = "String"
            python_iterable = None
            python_name = "data_feed_id"
            scalar = scalars.String

        class externalEventSourceIds(BaseCinnamonField):
            api_name = "externalEventSourceIds"
            api_kind = "SCALAR"
            api_kind_name = "String"
            python_iterable = list
            python_name = "external_event_source_ids"
            scalar = scalars.String

        class productSource(BaseCinnamonField):
            api_name = "productSource"
            api_kind = "ENUM"
            api_kind_name = "PRODUCT_SOURCE"
            python_iterable = None
            python_name = "product_source"

        class errors(BaseCinnamonField):
            api_name = "errors"
            api_kind = "SCALAR"
            api_kind_name = "JSONObject"
            python_iterable = list
            python_name = "errors"
            scalar = scalars.JSONObject

        class warnings(BaseCinnamonField):
            api_name = "warnings"
            api_kind = "SCALAR"
            api_kind_name = "JSONObject"
            python_iterable = list
            python_name = "warnings"
            scalar = scalars.JSONObject

        class mediaChannel(BaseCinnamonField):
            api_name = "mediaChannel"
            api_kind = "OBJECT"
            api_kind_name = "MediaChannel"
            python_iterable = None
            python_name = "media_channel"

        class products(BaseCinnamonField):
            api_name = "products"
            api_kind = "OBJECT"
            api_kind_name = "ProductConnection"
            python_iterable = None
            python_name = "products"

    id: str
    creation_date: datetime
    last_change_date: datetime
    name: str
    catalog_type: enums.CatalogType
    remote_id: Union[str, None, CinnamonUndefined]
    system_status: enums.SystemStatus
    remote_state: dict
    data_feed_id: Union[str, None, CinnamonUndefined]
    external_event_source_ids: List[str]
    product_source: enums.PRODUCT_SOURCE
    errors: List[dict]
    warnings: List[dict]
    media_channel: "MediaChannel"
    products: "ProductConnection"


class ProductConnection(BaseCinnamonObject, BaseCinnamonEdgesObject):
    class _API_FIELDS:
        class edges(BaseCinnamonField):
            api_name = "edges"
            api_kind = "OBJECT"
            api_kind_name = "ProductEdge"
            python_iterable = list
            python_name = "edges"

        class pageInfo(BaseCinnamonField):
            api_name = "pageInfo"
            api_kind = "OBJECT"
            api_kind_name = "PageInfo"
            python_iterable = None
            python_name = "page_info"

        class totalCount(BaseCinnamonField):
            api_name = "totalCount"
            api_kind = "SCALAR"
            api_kind_name = "Int"
            python_iterable = None
            python_name = "total_count"
            scalar = scalars.Int

    edges: List["ProductEdge"]
    page_info: "PageInfo"
    total_count: int


class ProductEdge(BaseCinnamonObject):
    class _API_FIELDS:
        class node(BaseCinnamonField):
            api_name = "node"
            api_kind = "OBJECT"
            api_kind_name = "Product"
            python_iterable = None
            python_name = "node"

        class cursor(BaseCinnamonField):
            api_name = "cursor"
            api_kind = "SCALAR"
            api_kind_name = "String"
            python_iterable = None
            python_name = "cursor"
            scalar = scalars.String

    node: "Product"
    cursor: str


class Product(BaseCinnamonObject):
    class _API_FIELDS:
        class id(BaseCinnamonField):
            api_name = "id"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = None
            python_name = "id"
            scalar = scalars.ObjectId

        class creationDate(BaseCinnamonField):
            api_name = "creationDate"
            api_kind = "SCALAR"
            api_kind_name = "DateISO"
            python_iterable = None
            python_name = "creation_date"
            scalar = scalars.DateISO

        class lastChangeDate(BaseCinnamonField):
            api_name = "lastChangeDate"
            api_kind = "SCALAR"
            api_kind_name = "DateISO"
            python_iterable = None
            python_name = "last_change_date"
            scalar = scalars.DateISO

        class resultsSource(BaseCinnamonField):
            api_name = "resultsSource"
            api_kind = "SCALAR"
            api_kind_name = "NonEmptyString"
            python_iterable = list
            python_name = "results_source"
            scalar = scalars.NonEmptyString

        class kpi(BaseCinnamonField):
            api_name = "kpi"
            api_kind = "SCALAR"
            api_kind_name = "String"
            python_iterable = None
            python_name = "kpi"
            scalar = scalars.String

        class vendor(BaseCinnamonField):
            api_name = "vendor"
            api_kind = "OBJECT"
            api_kind_name = "Vendor"
            python_iterable = None
            python_name = "vendor"

        class systemStatus(BaseCinnamonField):
            api_name = "systemStatus"
            api_kind = "ENUM"
            api_kind_name = "SystemStatus"
            python_iterable = None
            python_name = "system_status"

        class errors(BaseCinnamonField):
            api_name = "errors"
            api_kind = "SCALAR"
            api_kind_name = "JSONObject"
            python_iterable = list
            python_name = "errors"
            scalar = scalars.JSONObject

        class warnings(BaseCinnamonField):
            api_name = "warnings"
            api_kind = "SCALAR"
            api_kind_name = "JSONObject"
            python_iterable = list
            python_name = "warnings"
            scalar = scalars.JSONObject

        class name(BaseCinnamonField):
            api_name = "name"
            api_kind = "SCALAR"
            api_kind_name = "NonEmptyString"
            python_iterable = None
            python_name = "name"
            scalar = scalars.NonEmptyString

        class sku(BaseCinnamonField):
            api_name = "sku"
            api_kind = "SCALAR"
            api_kind_name = "NonEmptyString"
            python_iterable = None
            python_name = "sku"
            scalar = scalars.NonEmptyString

        class remoteState(BaseCinnamonField):
            api_name = "remoteState"
            api_kind = "SCALAR"
            api_kind_name = "JSONObject"
            python_iterable = None
            python_name = "remote_state"
            scalar = scalars.JSONObject

        class metadata(BaseCinnamonField):
            api_name = "metadata"
            api_kind = "SCALAR"
            api_kind_name = "JSONObject"
            python_iterable = None
            python_name = "metadata"
            scalar = scalars.JSONObject

        class imported(BaseCinnamonField):
            api_name = "imported"
            api_kind = "SCALAR"
            api_kind_name = "Boolean"
            python_iterable = None
            python_name = "imported"
            scalar = scalars.Boolean

        class results(BaseCinnamonField):
            api_name = "results"
            api_kind = "OBJECT"
            api_kind_name = "ResultConnection"
            python_iterable = None
            python_name = "results"

        class marketingCampaigns(BaseCinnamonField):
            api_name = "marketingCampaigns"
            api_kind = "OBJECT"
            api_kind_name = "MarketingCampaignConnection"
            python_iterable = None
            python_name = "marketing_campaigns"

        class catalog(BaseCinnamonField):
            api_name = "catalog"
            api_kind = "OBJECT"
            api_kind_name = "Catalog"
            python_iterable = None
            python_name = "catalog"

    id: str
    creation_date: datetime
    last_change_date: datetime
    results_source: List[str]
    kpi: Union[str, None, CinnamonUndefined]
    vendor: Union["Vendor", None, CinnamonUndefined]
    system_status: enums.SystemStatus
    errors: List[dict]
    warnings: List[dict]
    name: str
    sku: str
    remote_state: Union[dict, None, CinnamonUndefined]
    metadata: dict
    imported: bool
    results: "ResultConnection"
    marketing_campaigns: "MarketingCampaignConnection"
    catalog: "Catalog"


class ResultResource(BaseCinnamonObject):
    class _API_FIELDS:
        class id(BaseCinnamonField):
            api_name = "id"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = None
            python_name = "id"
            scalar = scalars.ObjectId

        class creationDate(BaseCinnamonField):
            api_name = "creationDate"
            api_kind = "SCALAR"
            api_kind_name = "DateISO"
            python_iterable = None
            python_name = "creation_date"
            scalar = scalars.DateISO

        class lastChangeDate(BaseCinnamonField):
            api_name = "lastChangeDate"
            api_kind = "SCALAR"
            api_kind_name = "DateISO"
            python_iterable = None
            python_name = "last_change_date"
            scalar = scalars.DateISO

        class resultsSource(BaseCinnamonField):
            api_name = "resultsSource"
            api_kind = "SCALAR"
            api_kind_name = "NonEmptyString"
            python_iterable = list
            python_name = "results_source"
            scalar = scalars.NonEmptyString

        class kpi(BaseCinnamonField):
            api_name = "kpi"
            api_kind = "SCALAR"
            api_kind_name = "String"
            python_iterable = None
            python_name = "kpi"
            scalar = scalars.String

        class vendor(BaseCinnamonField):
            api_name = "vendor"
            api_kind = "OBJECT"
            api_kind_name = "Vendor"
            python_iterable = None
            python_name = "vendor"

        class systemStatus(BaseCinnamonField):
            api_name = "systemStatus"
            api_kind = "ENUM"
            api_kind_name = "SystemStatus"
            python_iterable = None
            python_name = "system_status"

        class errors(BaseCinnamonField):
            api_name = "errors"
            api_kind = "SCALAR"
            api_kind_name = "JSONObject"
            python_iterable = list
            python_name = "errors"
            scalar = scalars.JSONObject

        class warnings(BaseCinnamonField):
            api_name = "warnings"
            api_kind = "SCALAR"
            api_kind_name = "JSONObject"
            python_iterable = list
            python_name = "warnings"
            scalar = scalars.JSONObject

    id: str
    creation_date: datetime
    last_change_date: datetime
    results_source: List[str]
    kpi: Union[str, None, CinnamonUndefined]
    vendor: Union["Vendor", None, CinnamonUndefined]
    system_status: enums.SystemStatus
    errors: List[dict]
    warnings: List[dict]


class Vendor(BaseCinnamonObject):
    class _API_FIELDS:
        class id(BaseCinnamonField):
            api_name = "id"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = None
            python_name = "id"
            scalar = scalars.ObjectId

        class creationDate(BaseCinnamonField):
            api_name = "creationDate"
            api_kind = "SCALAR"
            api_kind_name = "DateISO"
            python_iterable = None
            python_name = "creation_date"
            scalar = scalars.DateISO

        class lastChangeDate(BaseCinnamonField):
            api_name = "lastChangeDate"
            api_kind = "SCALAR"
            api_kind_name = "DateISO"
            python_iterable = None
            python_name = "last_change_date"
            scalar = scalars.DateISO

        class name(BaseCinnamonField):
            api_name = "name"
            api_kind = "SCALAR"
            api_kind_name = "NonEmptyString"
            python_iterable = None
            python_name = "name"
            scalar = scalars.NonEmptyString

        class systemStatus(BaseCinnamonField):
            api_name = "systemStatus"
            api_kind = "ENUM"
            api_kind_name = "SystemStatus"
            python_iterable = None
            python_name = "system_status"

        class errors(BaseCinnamonField):
            api_name = "errors"
            api_kind = "SCALAR"
            api_kind_name = "JSONObject"
            python_iterable = list
            python_name = "errors"
            scalar = scalars.JSONObject

        class warnings(BaseCinnamonField):
            api_name = "warnings"
            api_kind = "SCALAR"
            api_kind_name = "JSONObject"
            python_iterable = list
            python_name = "warnings"
            scalar = scalars.JSONObject

        class marketplace(BaseCinnamonField):
            api_name = "marketplace"
            api_kind = "OBJECT"
            api_kind_name = "Marketplace"
            python_iterable = None
            python_name = "marketplace"

        class vendorTokens(BaseCinnamonField):
            api_name = "vendorTokens"
            api_kind = "OBJECT"
            api_kind_name = "VendorTokenConnection"
            python_iterable = None
            python_name = "vendor_tokens"

        class products(BaseCinnamonField):
            api_name = "products"
            api_kind = "OBJECT"
            api_kind_name = "ProductConnection"
            python_iterable = None
            python_name = "products"

    id: str
    creation_date: datetime
    last_change_date: datetime
    name: str
    system_status: enums.SystemStatus
    errors: List[dict]
    warnings: List[dict]
    marketplace: "Marketplace"
    vendor_tokens: "VendorTokenConnection"
    products: "ProductConnection"


class VendorTokenConnection(BaseCinnamonObject, BaseCinnamonEdgesObject):
    class _API_FIELDS:
        class edges(BaseCinnamonField):
            api_name = "edges"
            api_kind = "OBJECT"
            api_kind_name = "VendorTokenEdge"
            python_iterable = list
            python_name = "edges"

        class pageInfo(BaseCinnamonField):
            api_name = "pageInfo"
            api_kind = "OBJECT"
            api_kind_name = "PageInfo"
            python_iterable = None
            python_name = "page_info"

        class totalCount(BaseCinnamonField):
            api_name = "totalCount"
            api_kind = "SCALAR"
            api_kind_name = "Int"
            python_iterable = None
            python_name = "total_count"
            scalar = scalars.Int

    edges: List["VendorTokenEdge"]
    page_info: "PageInfo"
    total_count: int


class VendorTokenEdge(BaseCinnamonObject):
    class _API_FIELDS:
        class node(BaseCinnamonField):
            api_name = "node"
            api_kind = "OBJECT"
            api_kind_name = "VendorToken"
            python_iterable = None
            python_name = "node"

        class cursor(BaseCinnamonField):
            api_name = "cursor"
            api_kind = "SCALAR"
            api_kind_name = "String"
            python_iterable = None
            python_name = "cursor"
            scalar = scalars.String

    node: "VendorToken"
    cursor: str


class VendorToken(BaseCinnamonObject):
    class _API_FIELDS:
        class id(BaseCinnamonField):
            api_name = "id"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = None
            python_name = "id"
            scalar = scalars.ObjectId

        class creationDate(BaseCinnamonField):
            api_name = "creationDate"
            api_kind = "SCALAR"
            api_kind_name = "DateISO"
            python_iterable = None
            python_name = "creation_date"
            scalar = scalars.DateISO

        class lastChangeDate(BaseCinnamonField):
            api_name = "lastChangeDate"
            api_kind = "SCALAR"
            api_kind_name = "DateISO"
            python_iterable = None
            python_name = "last_change_date"
            scalar = scalars.DateISO

        class token(BaseCinnamonField):
            api_name = "token"
            api_kind = "SCALAR"
            api_kind_name = "String"
            python_iterable = None
            python_name = "token"
            scalar = scalars.String

        class vendor(BaseCinnamonField):
            api_name = "vendor"
            api_kind = "OBJECT"
            api_kind_name = "Vendor"
            python_iterable = None
            python_name = "vendor"

        class marketplace(BaseCinnamonField):
            api_name = "marketplace"
            api_kind = "OBJECT"
            api_kind_name = "Marketplace"
            python_iterable = None
            python_name = "marketplace"

        class email(BaseCinnamonField):
            api_name = "email"
            api_kind = "SCALAR"
            api_kind_name = "NonEmptyString"
            python_iterable = None
            python_name = "email"
            scalar = scalars.NonEmptyString

    id: str
    creation_date: datetime
    last_change_date: datetime
    token: str
    vendor: "Vendor"
    marketplace: "Marketplace"
    email: Union[str, None, CinnamonUndefined]


class ResultConnection(BaseCinnamonObject, BaseCinnamonEdgesObject):
    class _API_FIELDS:
        class edges(BaseCinnamonField):
            api_name = "edges"
            api_kind = "OBJECT"
            api_kind_name = "ResultEdge"
            python_iterable = list
            python_name = "edges"

        class pageInfo(BaseCinnamonField):
            api_name = "pageInfo"
            api_kind = "OBJECT"
            api_kind_name = "PageInfo"
            python_iterable = None
            python_name = "page_info"

        class totalCount(BaseCinnamonField):
            api_name = "totalCount"
            api_kind = "SCALAR"
            api_kind_name = "Int"
            python_iterable = None
            python_name = "total_count"
            scalar = scalars.Int

    edges: List["ResultEdge"]
    page_info: "PageInfo"
    total_count: int


class ResultEdge(BaseCinnamonObject):
    class _API_FIELDS:
        class node(BaseCinnamonField):
            api_name = "node"
            api_kind = "OBJECT"
            api_kind_name = "Result"
            python_iterable = None
            python_name = "node"

        class cursor(BaseCinnamonField):
            api_name = "cursor"
            api_kind = "SCALAR"
            api_kind_name = "String"
            python_iterable = None
            python_name = "cursor"
            scalar = scalars.String

    node: "Result"
    cursor: str


class Result(BaseCinnamonObject):
    class _API_FIELDS:
        class id(BaseCinnamonField):
            api_name = "id"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = None
            python_name = "id"
            scalar = scalars.ObjectId

        class creationDate(BaseCinnamonField):
            api_name = "creationDate"
            api_kind = "SCALAR"
            api_kind_name = "DateISO"
            python_iterable = None
            python_name = "creation_date"
            scalar = scalars.DateISO

        class lastChangeDate(BaseCinnamonField):
            api_name = "lastChangeDate"
            api_kind = "SCALAR"
            api_kind_name = "DateISO"
            python_iterable = None
            python_name = "last_change_date"
            scalar = scalars.DateISO

        class date(BaseCinnamonField):
            api_name = "date"
            api_kind = "SCALAR"
            api_kind_name = "DateISO"
            python_iterable = None
            python_name = "date"
            scalar = scalars.DateISO

        class analytics(BaseCinnamonField):
            api_name = "analytics"
            api_kind = "OBJECT"
            api_kind_name = "ResultAnalytics"
            python_iterable = None
            python_name = "analytics"

        class type(BaseCinnamonField):
            api_name = "type"
            api_kind = "ENUM"
            api_kind_name = "ResultResourceTypeEnum"
            python_iterable = None
            python_name = "type"

        class breakdownType(BaseCinnamonField):
            api_name = "breakdownType"
            api_kind = "ENUM"
            api_kind_name = "ResultBreakdownTypeEnum"
            python_iterable = None
            python_name = "breakdown_type"

        class resource(BaseCinnamonField):
            api_name = "resource"
            api_kind = "INTERFACE"
            api_kind_name = "ResultResource"
            python_iterable = None
            python_name = "resource"

        class breakdown(BaseCinnamonField):
            api_name = "breakdown"
            api_kind = "INTERFACE"
            api_kind_name = "ResultResource"
            python_iterable = None
            python_name = "breakdown"

        class vendor(BaseCinnamonField):
            api_name = "vendor"
            api_kind = "OBJECT"
            api_kind_name = "Vendor"
            python_iterable = None
            python_name = "vendor"

    id: str
    creation_date: datetime
    last_change_date: datetime
    date: datetime
    analytics: "ResultAnalytics"
    type: enums.ResultResourceTypeEnum
    breakdown_type: enums.ResultBreakdownTypeEnum
    resource: Any
    breakdown: Any
    vendor: Union["Vendor", None, CinnamonUndefined]


class ResultAnalytics(BaseCinnamonObject):
    class _API_FIELDS:
        class results(BaseCinnamonField):
            api_name = "results"
            api_kind = "SCALAR"
            api_kind_name = "Int"
            python_iterable = None
            python_name = "results"
            scalar = scalars.Int

        class impressions(BaseCinnamonField):
            api_name = "impressions"
            api_kind = "SCALAR"
            api_kind_name = "Int"
            python_iterable = None
            python_name = "impressions"
            scalar = scalars.Int

        class clicks(BaseCinnamonField):
            api_name = "clicks"
            api_kind = "SCALAR"
            api_kind_name = "Int"
            python_iterable = None
            python_name = "clicks"
            scalar = scalars.Int

        class spend(BaseCinnamonField):
            api_name = "spend"
            api_kind = "SCALAR"
            api_kind_name = "Float"
            python_iterable = None
            python_name = "spend"
            scalar = scalars.Float

        class purchases(BaseCinnamonField):
            api_name = "purchases"
            api_kind = "SCALAR"
            api_kind_name = "Int"
            python_iterable = None
            python_name = "purchases"
            scalar = scalars.Int

        class purchasesValue(BaseCinnamonField):
            api_name = "purchasesValue"
            api_kind = "SCALAR"
            api_kind_name = "Float"
            python_iterable = None
            python_name = "purchases_value"
            scalar = scalars.Float

    results: Union[int, None, CinnamonUndefined]
    impressions: Union[int, None, CinnamonUndefined]
    clicks: Union[int, None, CinnamonUndefined]
    spend: Union[float, None, CinnamonUndefined]
    purchases: Union[int, None, CinnamonUndefined]
    purchases_value: Union[float, None, CinnamonUndefined]


class MarketingCampaignConnection(BaseCinnamonObject, BaseCinnamonEdgesObject):
    class _API_FIELDS:
        class edges(BaseCinnamonField):
            api_name = "edges"
            api_kind = "OBJECT"
            api_kind_name = "MarketingCampaignEdge"
            python_iterable = list
            python_name = "edges"

        class pageInfo(BaseCinnamonField):
            api_name = "pageInfo"
            api_kind = "OBJECT"
            api_kind_name = "PageInfo"
            python_iterable = None
            python_name = "page_info"

        class totalCount(BaseCinnamonField):
            api_name = "totalCount"
            api_kind = "SCALAR"
            api_kind_name = "Int"
            python_iterable = None
            python_name = "total_count"
            scalar = scalars.Int

    edges: List["MarketingCampaignEdge"]
    page_info: "PageInfo"
    total_count: int


class MarketingCampaignEdge(BaseCinnamonObject):
    class _API_FIELDS:
        class node(BaseCinnamonField):
            api_name = "node"
            api_kind = "OBJECT"
            api_kind_name = "MarketingCampaign"
            python_iterable = None
            python_name = "node"

        class cursor(BaseCinnamonField):
            api_name = "cursor"
            api_kind = "SCALAR"
            api_kind_name = "String"
            python_iterable = None
            python_name = "cursor"
            scalar = scalars.String

    node: "MarketingCampaign"
    cursor: str


class MarketingCampaign(BaseCinnamonObject):
    class _API_FIELDS:
        class id(BaseCinnamonField):
            api_name = "id"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = None
            python_name = "id"
            scalar = scalars.ObjectId

        class creationDate(BaseCinnamonField):
            api_name = "creationDate"
            api_kind = "SCALAR"
            api_kind_name = "DateISO"
            python_iterable = None
            python_name = "creation_date"
            scalar = scalars.DateISO

        class lastChangeDate(BaseCinnamonField):
            api_name = "lastChangeDate"
            api_kind = "SCALAR"
            api_kind_name = "DateISO"
            python_iterable = None
            python_name = "last_change_date"
            scalar = scalars.DateISO

        class resultsSource(BaseCinnamonField):
            api_name = "resultsSource"
            api_kind = "SCALAR"
            api_kind_name = "NonEmptyString"
            python_iterable = list
            python_name = "results_source"
            scalar = scalars.NonEmptyString

        class kpi(BaseCinnamonField):
            api_name = "kpi"
            api_kind = "SCALAR"
            api_kind_name = "String"
            python_iterable = None
            python_name = "kpi"
            scalar = scalars.String

        class vendor(BaseCinnamonField):
            api_name = "vendor"
            api_kind = "OBJECT"
            api_kind_name = "Vendor"
            python_iterable = None
            python_name = "vendor"

        class systemStatus(BaseCinnamonField):
            api_name = "systemStatus"
            api_kind = "ENUM"
            api_kind_name = "SystemStatus"
            python_iterable = None
            python_name = "system_status"

        class errors(BaseCinnamonField):
            api_name = "errors"
            api_kind = "SCALAR"
            api_kind_name = "JSONObject"
            python_iterable = list
            python_name = "errors"
            scalar = scalars.JSONObject

        class warnings(BaseCinnamonField):
            api_name = "warnings"
            api_kind = "SCALAR"
            api_kind_name = "JSONObject"
            python_iterable = list
            python_name = "warnings"
            scalar = scalars.JSONObject

        class name(BaseCinnamonField):
            api_name = "name"
            api_kind = "SCALAR"
            api_kind_name = "NonEmptyString"
            python_iterable = None
            python_name = "name"
            scalar = scalars.NonEmptyString

        class status(BaseCinnamonField):
            api_name = "status"
            api_kind = "ENUM"
            api_kind_name = "MarketingCampaignStatus"
            python_iterable = None
            python_name = "status"

        class creativeSpec(BaseCinnamonField):
            api_name = "creativeSpec"
            api_kind = "SCALAR"
            api_kind_name = "JSONObject"
            python_iterable = None
            python_name = "creative_spec"
            scalar = scalars.JSONObject

        class runTimeSpec(BaseCinnamonField):
            api_name = "runTimeSpec"
            api_kind = "SCALAR"
            api_kind_name = "JSONObject"
            python_iterable = None
            python_name = "run_time_spec"
            scalar = scalars.JSONObject

        class locationSpec(BaseCinnamonField):
            api_name = "locationSpec"
            api_kind = "SCALAR"
            api_kind_name = "JSONObject"
            python_iterable = None
            python_name = "location_spec"
            scalar = scalars.JSONObject

        class conversionSpec(BaseCinnamonField):
            api_name = "conversionSpec"
            api_kind = "SCALAR"
            api_kind_name = "JSONObject"
            python_iterable = None
            python_name = "conversion_spec"
            scalar = scalars.JSONObject

        class startDate(BaseCinnamonField):
            api_name = "startDate"
            api_kind = "SCALAR"
            api_kind_name = "DateISO"
            python_iterable = None
            python_name = "start_date"
            scalar = scalars.DateISO

        class endDate(BaseCinnamonField):
            api_name = "endDate"
            api_kind = "SCALAR"
            api_kind_name = "DateISO"
            python_iterable = None
            python_name = "end_date"
            scalar = scalars.DateISO

        class GCPX(BaseCinnamonField):
            api_name = "GCPX"
            api_kind = "OBJECT"
            api_kind_name = "GCPX"
            python_iterable = None
            python_name = "gcpx"

        class delivering(BaseCinnamonField):
            api_name = "delivering"
            api_kind = "SCALAR"
            api_kind_name = "Boolean"
            python_iterable = None
            python_name = "delivering"
            scalar = scalars.Boolean

        class marketingAds(BaseCinnamonField):
            api_name = "marketingAds"
            api_kind = "OBJECT"
            api_kind_name = "MarketingAdConnection"
            python_iterable = None
            python_name = "marketing_ads"

        class products(BaseCinnamonField):
            api_name = "products"
            api_kind = "OBJECT"
            api_kind_name = "ProductConnection"
            python_iterable = None
            python_name = "products"

        class catalog(BaseCinnamonField):
            api_name = "catalog"
            api_kind = "OBJECT"
            api_kind_name = "Catalog"
            python_iterable = None
            python_name = "catalog"

        class campaignTemplate(BaseCinnamonField):
            api_name = "campaignTemplate"
            api_kind = "OBJECT"
            api_kind_name = "CampaignTemplate"
            python_iterable = None
            python_name = "campaign_template"

        class mediaChannel(BaseCinnamonField):
            api_name = "mediaChannel"
            api_kind = "OBJECT"
            api_kind_name = "MediaChannel"
            python_iterable = None
            python_name = "media_channel"

        class results(BaseCinnamonField):
            api_name = "results"
            api_kind = "OBJECT"
            api_kind_name = "ResultConnection"
            python_iterable = None
            python_name = "results"

        class notifications(BaseCinnamonField):
            api_name = "notifications"
            api_kind = "OBJECT"
            api_kind_name = "NotificationConnection"
            python_iterable = None
            python_name = "notifications"

    id: str
    creation_date: datetime
    last_change_date: datetime
    results_source: List[str]
    kpi: Union[str, None, CinnamonUndefined]
    vendor: Union["Vendor", None, CinnamonUndefined]
    system_status: enums.SystemStatus
    errors: List[dict]
    warnings: List[dict]
    name: str
    status: enums.MarketingCampaignStatus
    creative_spec: dict
    run_time_spec: Union[dict, None, CinnamonUndefined]
    location_spec: dict
    conversion_spec: Union[dict, None, CinnamonUndefined]
    start_date: datetime
    end_date: Union[datetime, None, CinnamonUndefined]
    gcpx: Union["GCPX", None, CinnamonUndefined]
    delivering: bool
    marketing_ads: "MarketingAdConnection"
    products: "ProductConnection"
    catalog: "Catalog"
    campaign_template: Union["CampaignTemplate", None, CinnamonUndefined]
    media_channel: "MediaChannel"
    results: "ResultConnection"
    notifications: "NotificationConnection"


class NotificationResource(BaseCinnamonObject):
    class _API_FIELDS:
        class id(BaseCinnamonField):
            api_name = "id"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = None
            python_name = "id"
            scalar = scalars.ObjectId

        class creationDate(BaseCinnamonField):
            api_name = "creationDate"
            api_kind = "SCALAR"
            api_kind_name = "DateISO"
            python_iterable = None
            python_name = "creation_date"
            scalar = scalars.DateISO

        class lastChangeDate(BaseCinnamonField):
            api_name = "lastChangeDate"
            api_kind = "SCALAR"
            api_kind_name = "DateISO"
            python_iterable = None
            python_name = "last_change_date"
            scalar = scalars.DateISO

        class systemStatus(BaseCinnamonField):
            api_name = "systemStatus"
            api_kind = "ENUM"
            api_kind_name = "SystemStatus"
            python_iterable = None
            python_name = "system_status"

        class errors(BaseCinnamonField):
            api_name = "errors"
            api_kind = "SCALAR"
            api_kind_name = "JSONObject"
            python_iterable = list
            python_name = "errors"
            scalar = scalars.JSONObject

        class warnings(BaseCinnamonField):
            api_name = "warnings"
            api_kind = "SCALAR"
            api_kind_name = "JSONObject"
            python_iterable = list
            python_name = "warnings"
            scalar = scalars.JSONObject

    id: str
    creation_date: datetime
    last_change_date: datetime
    system_status: enums.SystemStatus
    errors: List[dict]
    warnings: List[dict]


class GCPX(BaseCinnamonObject):
    class _API_FIELDS:
        class id(BaseCinnamonField):
            api_name = "id"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = None
            python_name = "id"
            scalar = scalars.ObjectId

        class creationDate(BaseCinnamonField):
            api_name = "creationDate"
            api_kind = "SCALAR"
            api_kind_name = "DateISO"
            python_iterable = None
            python_name = "creation_date"
            scalar = scalars.DateISO

        class lastChangeDate(BaseCinnamonField):
            api_name = "lastChangeDate"
            api_kind = "SCALAR"
            api_kind_name = "DateISO"
            python_iterable = None
            python_name = "last_change_date"
            scalar = scalars.DateISO

        class kpi(BaseCinnamonField):
            api_name = "kpi"
            api_kind = "SCALAR"
            api_kind_name = "String"
            python_iterable = None
            python_name = "kpi"
            scalar = scalars.String

        class price(BaseCinnamonField):
            api_name = "price"
            api_kind = "SCALAR"
            api_kind_name = "Int"
            python_iterable = None
            python_name = "price"
            scalar = scalars.Int

        class startDate(BaseCinnamonField):
            api_name = "startDate"
            api_kind = "SCALAR"
            api_kind_name = "DateISO"
            python_iterable = None
            python_name = "start_date"
            scalar = scalars.DateISO

        class endDate(BaseCinnamonField):
            api_name = "endDate"
            api_kind = "SCALAR"
            api_kind_name = "DateISO"
            python_iterable = None
            python_name = "end_date"
            scalar = scalars.DateISO

        class minConversions(BaseCinnamonField):
            api_name = "minConversions"
            api_kind = "SCALAR"
            api_kind_name = "Int"
            python_iterable = None
            python_name = "min_conversions"
            scalar = scalars.Int

        class maxConversions(BaseCinnamonField):
            api_name = "maxConversions"
            api_kind = "SCALAR"
            api_kind_name = "Int"
            python_iterable = None
            python_name = "max_conversions"
            scalar = scalars.Int

        class campaignTemplate(BaseCinnamonField):
            api_name = "campaignTemplate"
            api_kind = "OBJECT"
            api_kind_name = "CampaignTemplate"
            python_iterable = None
            python_name = "campaign_template"

        class marketplace(BaseCinnamonField):
            api_name = "marketplace"
            api_kind = "OBJECT"
            api_kind_name = "Marketplace"
            python_iterable = None
            python_name = "marketplace"

        class marketingCampaigns(BaseCinnamonField):
            api_name = "marketingCampaigns"
            api_kind = "OBJECT"
            api_kind_name = "MarketingCampaignConnection"
            python_iterable = None
            python_name = "marketing_campaigns"

    id: str
    creation_date: datetime
    last_change_date: datetime
    kpi: str
    price: int
    start_date: datetime
    end_date: datetime
    min_conversions: int
    max_conversions: int
    campaign_template: "CampaignTemplate"
    marketplace: "Marketplace"
    marketing_campaigns: "MarketingCampaignConnection"


class MarketingAdConnection(BaseCinnamonObject, BaseCinnamonEdgesObject):
    class _API_FIELDS:
        class edges(BaseCinnamonField):
            api_name = "edges"
            api_kind = "OBJECT"
            api_kind_name = "MarketingAdEdge"
            python_iterable = list
            python_name = "edges"

        class pageInfo(BaseCinnamonField):
            api_name = "pageInfo"
            api_kind = "OBJECT"
            api_kind_name = "PageInfo"
            python_iterable = None
            python_name = "page_info"

        class totalCount(BaseCinnamonField):
            api_name = "totalCount"
            api_kind = "SCALAR"
            api_kind_name = "Int"
            python_iterable = None
            python_name = "total_count"
            scalar = scalars.Int

    edges: List["MarketingAdEdge"]
    page_info: "PageInfo"
    total_count: int


class MarketingAdEdge(BaseCinnamonObject):
    class _API_FIELDS:
        class node(BaseCinnamonField):
            api_name = "node"
            api_kind = "OBJECT"
            api_kind_name = "MarketingAd"
            python_iterable = None
            python_name = "node"

        class cursor(BaseCinnamonField):
            api_name = "cursor"
            api_kind = "SCALAR"
            api_kind_name = "String"
            python_iterable = None
            python_name = "cursor"
            scalar = scalars.String

    node: "MarketingAd"
    cursor: str


class MarketingAd(BaseCinnamonObject):
    class _API_FIELDS:
        class id(BaseCinnamonField):
            api_name = "id"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = None
            python_name = "id"
            scalar = scalars.ObjectId

        class creationDate(BaseCinnamonField):
            api_name = "creationDate"
            api_kind = "SCALAR"
            api_kind_name = "DateISO"
            python_iterable = None
            python_name = "creation_date"
            scalar = scalars.DateISO

        class lastChangeDate(BaseCinnamonField):
            api_name = "lastChangeDate"
            api_kind = "SCALAR"
            api_kind_name = "DateISO"
            python_iterable = None
            python_name = "last_change_date"
            scalar = scalars.DateISO

        class resultsSource(BaseCinnamonField):
            api_name = "resultsSource"
            api_kind = "SCALAR"
            api_kind_name = "NonEmptyString"
            python_iterable = list
            python_name = "results_source"
            scalar = scalars.NonEmptyString

        class kpi(BaseCinnamonField):
            api_name = "kpi"
            api_kind = "SCALAR"
            api_kind_name = "String"
            python_iterable = None
            python_name = "kpi"
            scalar = scalars.String

        class vendor(BaseCinnamonField):
            api_name = "vendor"
            api_kind = "OBJECT"
            api_kind_name = "Vendor"
            python_iterable = None
            python_name = "vendor"

        class systemStatus(BaseCinnamonField):
            api_name = "systemStatus"
            api_kind = "ENUM"
            api_kind_name = "SystemStatus"
            python_iterable = None
            python_name = "system_status"

        class errors(BaseCinnamonField):
            api_name = "errors"
            api_kind = "SCALAR"
            api_kind_name = "JSONObject"
            python_iterable = list
            python_name = "errors"
            scalar = scalars.JSONObject

        class warnings(BaseCinnamonField):
            api_name = "warnings"
            api_kind = "SCALAR"
            api_kind_name = "JSONObject"
            python_iterable = list
            python_name = "warnings"
            scalar = scalars.JSONObject

        class remoteId(BaseCinnamonField):
            api_name = "remoteId"
            api_kind = "SCALAR"
            api_kind_name = "String"
            python_iterable = None
            python_name = "remote_id"
            scalar = scalars.String

        class adPreviews(BaseCinnamonField):
            api_name = "adPreviews"
            api_kind = "OBJECT"
            api_kind_name = "AdPreview"
            python_iterable = list
            python_name = "ad_previews"

        class results(BaseCinnamonField):
            api_name = "results"
            api_kind = "OBJECT"
            api_kind_name = "ResultConnection"
            python_iterable = None
            python_name = "results"

        class marketingCampaign(BaseCinnamonField):
            api_name = "marketingCampaign"
            api_kind = "OBJECT"
            api_kind_name = "MarketingCampaign"
            python_iterable = None
            python_name = "marketing_campaign"

    id: str
    creation_date: datetime
    last_change_date: datetime
    results_source: List[str]
    kpi: Union[str, None, CinnamonUndefined]
    vendor: Union["Vendor", None, CinnamonUndefined]
    system_status: enums.SystemStatus
    errors: List[dict]
    warnings: List[dict]
    remote_id: str
    ad_previews: List["AdPreview"]
    results: "ResultConnection"
    marketing_campaign: "MarketingCampaign"


class AdPreview(BaseCinnamonObject):
    class _API_FIELDS:
        class url(BaseCinnamonField):
            api_name = "url"
            api_kind = "SCALAR"
            api_kind_name = "String"
            python_iterable = None
            python_name = "url"
            scalar = scalars.String

        class dimensions(BaseCinnamonField):
            api_name = "dimensions"
            api_kind = "SCALAR"
            api_kind_name = "Int"
            python_iterable = list
            python_name = "dimensions"
            scalar = scalars.Int

        class placement(BaseCinnamonField):
            api_name = "placement"
            api_kind = "SCALAR"
            api_kind_name = "String"
            python_iterable = None
            python_name = "placement"
            scalar = scalars.String

    url: str
    dimensions: List[int]
    placement: str


class NotificationConnection(BaseCinnamonObject, BaseCinnamonEdgesObject):
    class _API_FIELDS:
        class edges(BaseCinnamonField):
            api_name = "edges"
            api_kind = "OBJECT"
            api_kind_name = "NotificationEdge"
            python_iterable = list
            python_name = "edges"

        class pageInfo(BaseCinnamonField):
            api_name = "pageInfo"
            api_kind = "OBJECT"
            api_kind_name = "PageInfo"
            python_iterable = None
            python_name = "page_info"

        class totalCount(BaseCinnamonField):
            api_name = "totalCount"
            api_kind = "SCALAR"
            api_kind_name = "Int"
            python_iterable = None
            python_name = "total_count"
            scalar = scalars.Int

    edges: List["NotificationEdge"]
    page_info: "PageInfo"
    total_count: int


class NotificationEdge(BaseCinnamonObject):
    class _API_FIELDS:
        class node(BaseCinnamonField):
            api_name = "node"
            api_kind = "OBJECT"
            api_kind_name = "Notification"
            python_iterable = None
            python_name = "node"

        class cursor(BaseCinnamonField):
            api_name = "cursor"
            api_kind = "SCALAR"
            api_kind_name = "String"
            python_iterable = None
            python_name = "cursor"
            scalar = scalars.String

    node: "Notification"
    cursor: str


class Notification(BaseCinnamonObject):
    class _API_FIELDS:
        class id(BaseCinnamonField):
            api_name = "id"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = None
            python_name = "id"
            scalar = scalars.ObjectId

        class creationDate(BaseCinnamonField):
            api_name = "creationDate"
            api_kind = "SCALAR"
            api_kind_name = "DateISO"
            python_iterable = None
            python_name = "creation_date"
            scalar = scalars.DateISO

        class lastChangeDate(BaseCinnamonField):
            api_name = "lastChangeDate"
            api_kind = "SCALAR"
            api_kind_name = "DateISO"
            python_iterable = None
            python_name = "last_change_date"
            scalar = scalars.DateISO

        class title(BaseCinnamonField):
            api_name = "title"
            api_kind = "SCALAR"
            api_kind_name = "String"
            python_iterable = None
            python_name = "title"
            scalar = scalars.String

        class message(BaseCinnamonField):
            api_name = "message"
            api_kind = "SCALAR"
            api_kind_name = "String"
            python_iterable = None
            python_name = "message"
            scalar = scalars.String

        class status(BaseCinnamonField):
            api_name = "status"
            api_kind = "ENUM"
            api_kind_name = "NOTIFICATION_STATUS"
            python_iterable = None
            python_name = "status"

        class severity(BaseCinnamonField):
            api_name = "severity"
            api_kind = "ENUM"
            api_kind_name = "NOTIFICATION_SEVERITY"
            python_iterable = None
            python_name = "severity"

        class code(BaseCinnamonField):
            api_name = "code"
            api_kind = "ENUM"
            api_kind_name = "NOTIFICATION_CODE"
            python_iterable = None
            python_name = "code"

        class source(BaseCinnamonField):
            api_name = "source"
            api_kind = "SCALAR"
            api_kind_name = "String"
            python_iterable = None
            python_name = "source"
            scalar = scalars.String

        class resource(BaseCinnamonField):
            api_name = "resource"
            api_kind = "INTERFACE"
            api_kind_name = "NotificationResource"
            python_iterable = None
            python_name = "resource"

    id: str
    creation_date: datetime
    last_change_date: datetime
    title: str
    message: str
    status: enums.NOTIFICATION_STATUS
    severity: enums.NOTIFICATION_SEVERITY
    code: enums.NOTIFICATION_CODE
    source: str
    resource: Any


class CampaignTemplateConnection(BaseCinnamonObject, BaseCinnamonEdgesObject):
    class _API_FIELDS:
        class edges(BaseCinnamonField):
            api_name = "edges"
            api_kind = "OBJECT"
            api_kind_name = "CampaignTemplateEdge"
            python_iterable = list
            python_name = "edges"

        class pageInfo(BaseCinnamonField):
            api_name = "pageInfo"
            api_kind = "OBJECT"
            api_kind_name = "PageInfo"
            python_iterable = None
            python_name = "page_info"

        class totalCount(BaseCinnamonField):
            api_name = "totalCount"
            api_kind = "SCALAR"
            api_kind_name = "Int"
            python_iterable = None
            python_name = "total_count"
            scalar = scalars.Int

    edges: List["CampaignTemplateEdge"]
    page_info: "PageInfo"
    total_count: int


class CampaignTemplateEdge(BaseCinnamonObject):
    class _API_FIELDS:
        class node(BaseCinnamonField):
            api_name = "node"
            api_kind = "OBJECT"
            api_kind_name = "CampaignTemplate"
            python_iterable = None
            python_name = "node"

        class cursor(BaseCinnamonField):
            api_name = "cursor"
            api_kind = "SCALAR"
            api_kind_name = "String"
            python_iterable = None
            python_name = "cursor"
            scalar = scalars.String

    node: "CampaignTemplate"
    cursor: str


class VendorConnection(BaseCinnamonObject, BaseCinnamonEdgesObject):
    class _API_FIELDS:
        class edges(BaseCinnamonField):
            api_name = "edges"
            api_kind = "OBJECT"
            api_kind_name = "VendorEdge"
            python_iterable = list
            python_name = "edges"

        class pageInfo(BaseCinnamonField):
            api_name = "pageInfo"
            api_kind = "OBJECT"
            api_kind_name = "PageInfo"
            python_iterable = None
            python_name = "page_info"

        class totalCount(BaseCinnamonField):
            api_name = "totalCount"
            api_kind = "SCALAR"
            api_kind_name = "Int"
            python_iterable = None
            python_name = "total_count"
            scalar = scalars.Int

    edges: List["VendorEdge"]
    page_info: "PageInfo"
    total_count: int


class VendorEdge(BaseCinnamonObject):
    class _API_FIELDS:
        class node(BaseCinnamonField):
            api_name = "node"
            api_kind = "OBJECT"
            api_kind_name = "Vendor"
            python_iterable = None
            python_name = "node"

        class cursor(BaseCinnamonField):
            api_name = "cursor"
            api_kind = "SCALAR"
            api_kind_name = "String"
            python_iterable = None
            python_name = "cursor"
            scalar = scalars.String

    node: "Vendor"
    cursor: str


class CreativeTemplateConnection(BaseCinnamonObject, BaseCinnamonEdgesObject):
    class _API_FIELDS:
        class edges(BaseCinnamonField):
            api_name = "edges"
            api_kind = "OBJECT"
            api_kind_name = "CreativeTemplateEdge"
            python_iterable = list
            python_name = "edges"

        class pageInfo(BaseCinnamonField):
            api_name = "pageInfo"
            api_kind = "OBJECT"
            api_kind_name = "PageInfo"
            python_iterable = None
            python_name = "page_info"

        class totalCount(BaseCinnamonField):
            api_name = "totalCount"
            api_kind = "SCALAR"
            api_kind_name = "Int"
            python_iterable = None
            python_name = "total_count"
            scalar = scalars.Int

    edges: List["CreativeTemplateEdge"]
    page_info: "PageInfo"
    total_count: int


class CreativeTemplateEdge(BaseCinnamonObject):
    class _API_FIELDS:
        class node(BaseCinnamonField):
            api_name = "node"
            api_kind = "OBJECT"
            api_kind_name = "CreativeTemplate"
            python_iterable = None
            python_name = "node"

        class cursor(BaseCinnamonField):
            api_name = "cursor"
            api_kind = "SCALAR"
            api_kind_name = "String"
            python_iterable = None
            python_name = "cursor"
            scalar = scalars.String

    node: "CreativeTemplate"
    cursor: str


class CreativeTemplate(BaseCinnamonObject):
    class _API_FIELDS:
        class id(BaseCinnamonField):
            api_name = "id"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = None
            python_name = "id"
            scalar = scalars.ObjectId

        class creationDate(BaseCinnamonField):
            api_name = "creationDate"
            api_kind = "SCALAR"
            api_kind_name = "DateISO"
            python_iterable = None
            python_name = "creation_date"
            scalar = scalars.DateISO

        class lastChangeDate(BaseCinnamonField):
            api_name = "lastChangeDate"
            api_kind = "SCALAR"
            api_kind_name = "DateISO"
            python_iterable = None
            python_name = "last_change_date"
            scalar = scalars.DateISO

        class name(BaseCinnamonField):
            api_name = "name"
            api_kind = "SCALAR"
            api_kind_name = "NonEmptyString"
            python_iterable = None
            python_name = "name"
            scalar = scalars.NonEmptyString

        class height(BaseCinnamonField):
            api_name = "height"
            api_kind = "SCALAR"
            api_kind_name = "Int"
            python_iterable = None
            python_name = "height"
            scalar = scalars.Int

        class width(BaseCinnamonField):
            api_name = "width"
            api_kind = "SCALAR"
            api_kind_name = "Int"
            python_iterable = None
            python_name = "width"
            scalar = scalars.Int

        class systemStatus(BaseCinnamonField):
            api_name = "systemStatus"
            api_kind = "ENUM"
            api_kind_name = "SystemStatus"
            python_iterable = None
            python_name = "system_status"

        class errors(BaseCinnamonField):
            api_name = "errors"
            api_kind = "SCALAR"
            api_kind_name = "JSONObject"
            python_iterable = list
            python_name = "errors"
            scalar = scalars.JSONObject

        class warnings(BaseCinnamonField):
            api_name = "warnings"
            api_kind = "SCALAR"
            api_kind_name = "JSONObject"
            python_iterable = list
            python_name = "warnings"
            scalar = scalars.JSONObject

        class marketplace(BaseCinnamonField):
            api_name = "marketplace"
            api_kind = "OBJECT"
            api_kind_name = "Marketplace"
            python_iterable = None
            python_name = "marketplace"

        class marketingCampaigns(BaseCinnamonField):
            api_name = "marketingCampaigns"
            api_kind = "OBJECT"
            api_kind_name = "MarketingCampaignConnection"
            python_iterable = None
            python_name = "marketing_campaigns"

        class creativeLayers(BaseCinnamonField):
            api_name = "creativeLayers"
            api_kind = "OBJECT"
            api_kind_name = "CreativeLayerConnection"
            python_iterable = None
            python_name = "creative_layers"

    id: str
    creation_date: datetime
    last_change_date: datetime
    name: str
    height: int
    width: int
    system_status: enums.SystemStatus
    errors: List[dict]
    warnings: List[dict]
    marketplace: "Marketplace"
    marketing_campaigns: "MarketingCampaignConnection"
    creative_layers: "CreativeLayerConnection"


class CreativeLayerConnection(BaseCinnamonObject, BaseCinnamonEdgesObject):
    class _API_FIELDS:
        class edges(BaseCinnamonField):
            api_name = "edges"
            api_kind = "OBJECT"
            api_kind_name = "CreativeLayerEdge"
            python_iterable = list
            python_name = "edges"

        class pageInfo(BaseCinnamonField):
            api_name = "pageInfo"
            api_kind = "OBJECT"
            api_kind_name = "PageInfo"
            python_iterable = None
            python_name = "page_info"

        class totalCount(BaseCinnamonField):
            api_name = "totalCount"
            api_kind = "SCALAR"
            api_kind_name = "Int"
            python_iterable = None
            python_name = "total_count"
            scalar = scalars.Int

    edges: List["CreativeLayerEdge"]
    page_info: "PageInfo"
    total_count: int


class CreativeLayerEdge(BaseCinnamonObject):
    class _API_FIELDS:
        class node(BaseCinnamonField):
            api_name = "node"
            api_kind = "OBJECT"
            api_kind_name = "CreativeLayer"
            python_iterable = None
            python_name = "node"

        class cursor(BaseCinnamonField):
            api_name = "cursor"
            api_kind = "SCALAR"
            api_kind_name = "String"
            python_iterable = None
            python_name = "cursor"
            scalar = scalars.String

    node: "CreativeLayer"
    cursor: str


class CreativeLayer(BaseCinnamonObject):
    class _API_FIELDS:
        class id(BaseCinnamonField):
            api_name = "id"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = None
            python_name = "id"
            scalar = scalars.ObjectId

        class creationDate(BaseCinnamonField):
            api_name = "creationDate"
            api_kind = "SCALAR"
            api_kind_name = "DateISO"
            python_iterable = None
            python_name = "creation_date"
            scalar = scalars.DateISO

        class lastChangeDate(BaseCinnamonField):
            api_name = "lastChangeDate"
            api_kind = "SCALAR"
            api_kind_name = "DateISO"
            python_iterable = None
            python_name = "last_change_date"
            scalar = scalars.DateISO

        class name(BaseCinnamonField):
            api_name = "name"
            api_kind = "SCALAR"
            api_kind_name = "NonEmptyString"
            python_iterable = None
            python_name = "name"
            scalar = scalars.NonEmptyString

        class height(BaseCinnamonField):
            api_name = "height"
            api_kind = "SCALAR"
            api_kind_name = "Int"
            python_iterable = None
            python_name = "height"
            scalar = scalars.Int

        class width(BaseCinnamonField):
            api_name = "width"
            api_kind = "SCALAR"
            api_kind_name = "Int"
            python_iterable = None
            python_name = "width"
            scalar = scalars.Int

        class x(BaseCinnamonField):
            api_name = "x"
            api_kind = "SCALAR"
            api_kind_name = "Int"
            python_iterable = None
            python_name = "x"
            scalar = scalars.Int

        class y(BaseCinnamonField):
            api_name = "y"
            api_kind = "SCALAR"
            api_kind_name = "Int"
            python_iterable = None
            python_name = "y"
            scalar = scalars.Int

        class order(BaseCinnamonField):
            api_name = "order"
            api_kind = "SCALAR"
            api_kind_name = "Int"
            python_iterable = None
            python_name = "order"
            scalar = scalars.Int

        class type(BaseCinnamonField):
            api_name = "type"
            api_kind = "ENUM"
            api_kind_name = "CreativeLayerTypes"
            python_iterable = None
            python_name = "type"

        class properties(BaseCinnamonField):
            api_name = "properties"
            api_kind = "SCALAR"
            api_kind_name = "JSONObject"
            python_iterable = None
            python_name = "properties"
            scalar = scalars.JSONObject

        class systemStatus(BaseCinnamonField):
            api_name = "systemStatus"
            api_kind = "ENUM"
            api_kind_name = "SystemStatus"
            python_iterable = None
            python_name = "system_status"

        class errors(BaseCinnamonField):
            api_name = "errors"
            api_kind = "SCALAR"
            api_kind_name = "JSONObject"
            python_iterable = list
            python_name = "errors"
            scalar = scalars.JSONObject

        class warnings(BaseCinnamonField):
            api_name = "warnings"
            api_kind = "SCALAR"
            api_kind_name = "JSONObject"
            python_iterable = list
            python_name = "warnings"
            scalar = scalars.JSONObject

        class creativeTemplate(BaseCinnamonField):
            api_name = "creativeTemplate"
            api_kind = "OBJECT"
            api_kind_name = "CreativeTemplate"
            python_iterable = None
            python_name = "creative_template"

    id: str
    creation_date: datetime
    last_change_date: datetime
    name: str
    height: int
    width: int
    x: int
    y: int
    order: int
    type: enums.CreativeLayerTypes
    properties: dict
    system_status: enums.SystemStatus
    errors: List[dict]
    warnings: List[dict]
    creative_template: "CreativeTemplate"


class GCPXConnection(BaseCinnamonObject, BaseCinnamonEdgesObject):
    class _API_FIELDS:
        class edges(BaseCinnamonField):
            api_name = "edges"
            api_kind = "OBJECT"
            api_kind_name = "GCPXEdge"
            python_iterable = list
            python_name = "edges"

        class pageInfo(BaseCinnamonField):
            api_name = "pageInfo"
            api_kind = "OBJECT"
            api_kind_name = "PageInfo"
            python_iterable = None
            python_name = "page_info"

        class totalCount(BaseCinnamonField):
            api_name = "totalCount"
            api_kind = "SCALAR"
            api_kind_name = "Int"
            python_iterable = None
            python_name = "total_count"
            scalar = scalars.Int

    edges: List["GCPXEdge"]
    page_info: "PageInfo"
    total_count: int


class GCPXEdge(BaseCinnamonObject):
    class _API_FIELDS:
        class node(BaseCinnamonField):
            api_name = "node"
            api_kind = "OBJECT"
            api_kind_name = "GCPX"
            python_iterable = None
            python_name = "node"

        class cursor(BaseCinnamonField):
            api_name = "cursor"
            api_kind = "SCALAR"
            api_kind_name = "String"
            python_iterable = None
            python_name = "cursor"
            scalar = scalars.String

    node: "GCPX"
    cursor: str


class CreativeFont(BaseCinnamonObject):
    class _API_FIELDS:
        class id(BaseCinnamonField):
            api_name = "id"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = None
            python_name = "id"
            scalar = scalars.ObjectId

        class creationDate(BaseCinnamonField):
            api_name = "creationDate"
            api_kind = "SCALAR"
            api_kind_name = "DateISO"
            python_iterable = None
            python_name = "creation_date"
            scalar = scalars.DateISO

        class lastChangeDate(BaseCinnamonField):
            api_name = "lastChangeDate"
            api_kind = "SCALAR"
            api_kind_name = "DateISO"
            python_iterable = None
            python_name = "last_change_date"
            scalar = scalars.DateISO

        class name(BaseCinnamonField):
            api_name = "name"
            api_kind = "SCALAR"
            api_kind_name = "NonEmptyString"
            python_iterable = None
            python_name = "name"
            scalar = scalars.NonEmptyString

        class url(BaseCinnamonField):
            api_name = "url"
            api_kind = "SCALAR"
            api_kind_name = "NonEmptyString"
            python_iterable = None
            python_name = "url"
            scalar = scalars.NonEmptyString

        class properties(BaseCinnamonField):
            api_name = "properties"
            api_kind = "SCALAR"
            api_kind_name = "JSONObject"
            python_iterable = None
            python_name = "properties"
            scalar = scalars.JSONObject

        class systemStatus(BaseCinnamonField):
            api_name = "systemStatus"
            api_kind = "ENUM"
            api_kind_name = "SystemStatus"
            python_iterable = None
            python_name = "system_status"

        class errors(BaseCinnamonField):
            api_name = "errors"
            api_kind = "SCALAR"
            api_kind_name = "JSONObject"
            python_iterable = list
            python_name = "errors"
            scalar = scalars.JSONObject

        class warnings(BaseCinnamonField):
            api_name = "warnings"
            api_kind = "SCALAR"
            api_kind_name = "JSONObject"
            python_iterable = list
            python_name = "warnings"
            scalar = scalars.JSONObject

        class marketplace(BaseCinnamonField):
            api_name = "marketplace"
            api_kind = "OBJECT"
            api_kind_name = "Marketplace"
            python_iterable = None
            python_name = "marketplace"

    id: str
    creation_date: datetime
    last_change_date: datetime
    name: str
    url: str
    properties: dict
    system_status: enums.SystemStatus
    errors: List[dict]
    warnings: List[dict]
    marketplace: "Marketplace"


class CreativeFontConnection(BaseCinnamonObject, BaseCinnamonEdgesObject):
    class _API_FIELDS:
        class edges(BaseCinnamonField):
            api_name = "edges"
            api_kind = "OBJECT"
            api_kind_name = "CreativeFontEdge"
            python_iterable = list
            python_name = "edges"

        class pageInfo(BaseCinnamonField):
            api_name = "pageInfo"
            api_kind = "OBJECT"
            api_kind_name = "PageInfo"
            python_iterable = None
            python_name = "page_info"

        class totalCount(BaseCinnamonField):
            api_name = "totalCount"
            api_kind = "SCALAR"
            api_kind_name = "Int"
            python_iterable = None
            python_name = "total_count"
            scalar = scalars.Int

    edges: List["CreativeFontEdge"]
    page_info: "PageInfo"
    total_count: int


class CreativeFontEdge(BaseCinnamonObject):
    class _API_FIELDS:
        class node(BaseCinnamonField):
            api_name = "node"
            api_kind = "OBJECT"
            api_kind_name = "CreativeFont"
            python_iterable = None
            python_name = "node"

        class cursor(BaseCinnamonField):
            api_name = "cursor"
            api_kind = "SCALAR"
            api_kind_name = "String"
            python_iterable = None
            python_name = "cursor"
            scalar = scalars.String

    node: "CreativeFont"
    cursor: str


class CreativeImage(BaseCinnamonObject):
    class _API_FIELDS:
        class id(BaseCinnamonField):
            api_name = "id"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = None
            python_name = "id"
            scalar = scalars.ObjectId

        class creationDate(BaseCinnamonField):
            api_name = "creationDate"
            api_kind = "SCALAR"
            api_kind_name = "DateISO"
            python_iterable = None
            python_name = "creation_date"
            scalar = scalars.DateISO

        class lastChangeDate(BaseCinnamonField):
            api_name = "lastChangeDate"
            api_kind = "SCALAR"
            api_kind_name = "DateISO"
            python_iterable = None
            python_name = "last_change_date"
            scalar = scalars.DateISO

        class name(BaseCinnamonField):
            api_name = "name"
            api_kind = "SCALAR"
            api_kind_name = "NonEmptyString"
            python_iterable = None
            python_name = "name"
            scalar = scalars.NonEmptyString

        class url(BaseCinnamonField):
            api_name = "url"
            api_kind = "SCALAR"
            api_kind_name = "NonEmptyString"
            python_iterable = None
            python_name = "url"
            scalar = scalars.NonEmptyString

        class properties(BaseCinnamonField):
            api_name = "properties"
            api_kind = "SCALAR"
            api_kind_name = "JSONObject"
            python_iterable = None
            python_name = "properties"
            scalar = scalars.JSONObject

        class systemStatus(BaseCinnamonField):
            api_name = "systemStatus"
            api_kind = "ENUM"
            api_kind_name = "SystemStatus"
            python_iterable = None
            python_name = "system_status"

        class errors(BaseCinnamonField):
            api_name = "errors"
            api_kind = "SCALAR"
            api_kind_name = "JSONObject"
            python_iterable = list
            python_name = "errors"
            scalar = scalars.JSONObject

        class warnings(BaseCinnamonField):
            api_name = "warnings"
            api_kind = "SCALAR"
            api_kind_name = "JSONObject"
            python_iterable = list
            python_name = "warnings"
            scalar = scalars.JSONObject

        class marketplace(BaseCinnamonField):
            api_name = "marketplace"
            api_kind = "OBJECT"
            api_kind_name = "Marketplace"
            python_iterable = None
            python_name = "marketplace"

    id: str
    creation_date: datetime
    last_change_date: datetime
    name: str
    url: str
    properties: dict
    system_status: enums.SystemStatus
    errors: List[dict]
    warnings: List[dict]
    marketplace: "Marketplace"


class CreativeImageConnection(BaseCinnamonObject, BaseCinnamonEdgesObject):
    class _API_FIELDS:
        class edges(BaseCinnamonField):
            api_name = "edges"
            api_kind = "OBJECT"
            api_kind_name = "CreativeImageEdge"
            python_iterable = list
            python_name = "edges"

        class pageInfo(BaseCinnamonField):
            api_name = "pageInfo"
            api_kind = "OBJECT"
            api_kind_name = "PageInfo"
            python_iterable = None
            python_name = "page_info"

        class totalCount(BaseCinnamonField):
            api_name = "totalCount"
            api_kind = "SCALAR"
            api_kind_name = "Int"
            python_iterable = None
            python_name = "total_count"
            scalar = scalars.Int

    edges: List["CreativeImageEdge"]
    page_info: "PageInfo"
    total_count: int


class CreativeImageEdge(BaseCinnamonObject):
    class _API_FIELDS:
        class node(BaseCinnamonField):
            api_name = "node"
            api_kind = "OBJECT"
            api_kind_name = "CreativeImage"
            python_iterable = None
            python_name = "node"

        class cursor(BaseCinnamonField):
            api_name = "cursor"
            api_kind = "SCALAR"
            api_kind_name = "String"
            python_iterable = None
            python_name = "cursor"
            scalar = scalars.String

    node: "CreativeImage"
    cursor: str


class Token(BaseCinnamonObject):
    class _API_FIELDS:
        class token(BaseCinnamonField):
            api_name = "token"
            api_kind = "SCALAR"
            api_kind_name = "String"
            python_iterable = None
            python_name = "token"
            scalar = scalars.String

        class refreshToken(BaseCinnamonField):
            api_name = "refreshToken"
            api_kind = "SCALAR"
            api_kind_name = "String"
            python_iterable = None
            python_name = "refresh_token"
            scalar = scalars.String

        class expiryDate(BaseCinnamonField):
            api_name = "expiryDate"
            api_kind = "SCALAR"
            api_kind_name = "DateISO"
            python_iterable = None
            python_name = "expiry_date"
            scalar = scalars.DateISO

        class user(BaseCinnamonField):
            api_name = "user"
            api_kind = "OBJECT"
            api_kind_name = "User"
            python_iterable = None
            python_name = "user"

    token: str
    refresh_token: str
    expiry_date: datetime
    user: "User"


class Deletion(BaseCinnamonObject):
    class _API_FIELDS:
        class id(BaseCinnamonField):
            api_name = "id"
            api_kind = "SCALAR"
            api_kind_name = "String"
            python_iterable = None
            python_name = "id"
            scalar = scalars.String

    id: str


class RequestResult(BaseCinnamonObject):
    class _API_FIELDS:
        class result(BaseCinnamonField):
            api_name = "result"
            api_kind = "SCALAR"
            api_kind_name = "String"
            python_iterable = None
            python_name = "result"
            scalar = scalars.String

    result: str


class MarketingCampaignSnapshot(BaseCinnamonObject):
    class _API_FIELDS:
        class id(BaseCinnamonField):
            api_name = "id"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = None
            python_name = "id"
            scalar = scalars.ObjectId

        class creationDate(BaseCinnamonField):
            api_name = "creationDate"
            api_kind = "SCALAR"
            api_kind_name = "DateISO"
            python_iterable = None
            python_name = "creation_date"
            scalar = scalars.DateISO

        class lastChangeDate(BaseCinnamonField):
            api_name = "lastChangeDate"
            api_kind = "SCALAR"
            api_kind_name = "DateISO"
            python_iterable = None
            python_name = "last_change_date"
            scalar = scalars.DateISO

        class marketingCampaign(BaseCinnamonField):
            api_name = "marketingCampaign"
            api_kind = "OBJECT"
            api_kind_name = "MarketingCampaign"
            python_iterable = None
            python_name = "marketing_campaign"

        class successful(BaseCinnamonField):
            api_name = "successful"
            api_kind = "SCALAR"
            api_kind_name = "Boolean"
            python_iterable = None
            python_name = "successful"
            scalar = scalars.Boolean

        class name(BaseCinnamonField):
            api_name = "name"
            api_kind = "SCALAR"
            api_kind_name = "String"
            python_iterable = None
            python_name = "name"
            scalar = scalars.String

        class status(BaseCinnamonField):
            api_name = "status"
            api_kind = "ENUM"
            api_kind_name = "MarketingCampaignStatus"
            python_iterable = None
            python_name = "status"

        class creativeSpec(BaseCinnamonField):
            api_name = "creativeSpec"
            api_kind = "SCALAR"
            api_kind_name = "JSONObject"
            python_iterable = None
            python_name = "creative_spec"
            scalar = scalars.JSONObject

        class runTimeSpec(BaseCinnamonField):
            api_name = "runTimeSpec"
            api_kind = "SCALAR"
            api_kind_name = "JSONObject"
            python_iterable = None
            python_name = "run_time_spec"
            scalar = scalars.JSONObject

        class locationSpec(BaseCinnamonField):
            api_name = "locationSpec"
            api_kind = "SCALAR"
            api_kind_name = "JSONObject"
            python_iterable = None
            python_name = "location_spec"
            scalar = scalars.JSONObject

        class kpi(BaseCinnamonField):
            api_name = "kpi"
            api_kind = "SCALAR"
            api_kind_name = "String"
            python_iterable = None
            python_name = "kpi"
            scalar = scalars.String

        class productIds(BaseCinnamonField):
            api_name = "productIds"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = list
            python_name = "product_ids"
            scalar = scalars.ObjectId

    id: str
    creation_date: datetime
    last_change_date: datetime
    marketing_campaign: "MarketingCampaign"
    successful: bool
    name: str
    status: enums.MarketingCampaignStatus
    creative_spec: dict
    run_time_spec: Union[dict, None, CinnamonUndefined]
    location_spec: dict
    kpi: Union[str, None, CinnamonUndefined]
    product_ids: List[str]


class MarketingCampaignSnapshotEdge(BaseCinnamonObject):
    class _API_FIELDS:
        class node(BaseCinnamonField):
            api_name = "node"
            api_kind = "OBJECT"
            api_kind_name = "MarketingCampaignSnapshot"
            python_iterable = None
            python_name = "node"

        class cursor(BaseCinnamonField):
            api_name = "cursor"
            api_kind = "SCALAR"
            api_kind_name = "String"
            python_iterable = None
            python_name = "cursor"
            scalar = scalars.String

    node: "MarketingCampaignSnapshot"
    cursor: str


class MarketingCampaignSnapshotConnection(BaseCinnamonObject, BaseCinnamonEdgesObject):
    class _API_FIELDS:
        class edges(BaseCinnamonField):
            api_name = "edges"
            api_kind = "OBJECT"
            api_kind_name = "MarketingCampaignSnapshotEdge"
            python_iterable = list
            python_name = "edges"

        class pageInfo(BaseCinnamonField):
            api_name = "pageInfo"
            api_kind = "OBJECT"
            api_kind_name = "PageInfo"
            python_iterable = None
            python_name = "page_info"

        class totalCount(BaseCinnamonField):
            api_name = "totalCount"
            api_kind = "SCALAR"
            api_kind_name = "Int"
            python_iterable = None
            python_name = "total_count"
            scalar = scalars.Int

    edges: List["MarketingCampaignSnapshotEdge"]
    page_info: "PageInfo"
    total_count: int


class SingleUseToken(BaseCinnamonObject):
    class _API_FIELDS:
        class id(BaseCinnamonField):
            api_name = "id"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = None
            python_name = "id"
            scalar = scalars.ObjectId

        class creationDate(BaseCinnamonField):
            api_name = "creationDate"
            api_kind = "SCALAR"
            api_kind_name = "DateISO"
            python_iterable = None
            python_name = "creation_date"
            scalar = scalars.DateISO

        class lastChangeDate(BaseCinnamonField):
            api_name = "lastChangeDate"
            api_kind = "SCALAR"
            api_kind_name = "DateISO"
            python_iterable = None
            python_name = "last_change_date"
            scalar = scalars.DateISO

        class token(BaseCinnamonField):
            api_name = "token"
            api_kind = "SCALAR"
            api_kind_name = "NonEmptyString"
            python_iterable = None
            python_name = "token"
            scalar = scalars.NonEmptyString

        class user(BaseCinnamonField):
            api_name = "user"
            api_kind = "OBJECT"
            api_kind_name = "User"
            python_iterable = None
            python_name = "user"

    id: str
    creation_date: datetime
    last_change_date: datetime
    token: str
    user: "User"


class SingleUseTokenEdge(BaseCinnamonObject):
    class _API_FIELDS:
        class node(BaseCinnamonField):
            api_name = "node"
            api_kind = "OBJECT"
            api_kind_name = "SingleUseToken"
            python_iterable = None
            python_name = "node"

        class cursor(BaseCinnamonField):
            api_name = "cursor"
            api_kind = "SCALAR"
            api_kind_name = "String"
            python_iterable = None
            python_name = "cursor"
            scalar = scalars.String

    node: "SingleUseToken"
    cursor: str


class SingleUseTokenConnection(BaseCinnamonObject, BaseCinnamonEdgesObject):
    class _API_FIELDS:
        class edges(BaseCinnamonField):
            api_name = "edges"
            api_kind = "OBJECT"
            api_kind_name = "SingleUseTokenEdge"
            python_iterable = list
            python_name = "edges"

        class pageInfo(BaseCinnamonField):
            api_name = "pageInfo"
            api_kind = "OBJECT"
            api_kind_name = "PageInfo"
            python_iterable = None
            python_name = "page_info"

        class totalCount(BaseCinnamonField):
            api_name = "totalCount"
            api_kind = "SCALAR"
            api_kind_name = "Int"
            python_iterable = None
            python_name = "total_count"
            scalar = scalars.Int

    edges: List["SingleUseTokenEdge"]
    page_info: "PageInfo"
    total_count: int


CampaignTemplate._API_FIELDS.marketplace.obj = Marketplace
CampaignTemplate._API_FIELDS.marketingCampaigns.obj = MarketingCampaignConnection
CampaignTemplate._API_FIELDS.GCPXHistory.obj = GCPXConnection
CampaignTemplate._API_FIELDS.currentGCPX.obj = GCPX
Marketplace._API_FIELDS.organization.obj = Organization
Marketplace._API_FIELDS.mediaChannels.obj = MediaChannelConnection
Marketplace._API_FIELDS.campaignTemplates.obj = CampaignTemplateConnection
Marketplace._API_FIELDS.vendors.obj = VendorConnection
Marketplace._API_FIELDS.vendorTokens.obj = VendorTokenConnection
Marketplace._API_FIELDS.creativeTemplates.obj = CreativeTemplateConnection
Marketplace._API_FIELDS.products.obj = ProductConnection
Organization._API_FIELDS.users.obj = UserConnection
Organization._API_FIELDS.marketplaces.obj = MarketplaceConnection
UserConnection._API_FIELDS.edges.obj = UserEdge
UserConnection._API_FIELDS.pageInfo.obj = PageInfo
UserEdge._API_FIELDS.node.obj = User
User._API_FIELDS.organizations.obj = OrganizationConnection
User._API_FIELDS.entitlements.obj = EntitlementConnection
OrganizationConnection._API_FIELDS.edges.obj = OrganizationEdge
OrganizationConnection._API_FIELDS.pageInfo.obj = PageInfo
OrganizationEdge._API_FIELDS.node.obj = Organization
EntitlementConnection._API_FIELDS.edges.obj = EntitlementEdge
EntitlementConnection._API_FIELDS.pageInfo.obj = PageInfo
EntitlementEdge._API_FIELDS.node.obj = Entitlement
Entitlement._API_FIELDS.user.obj = User
MarketplaceConnection._API_FIELDS.edges.obj = MarketplaceEdge
MarketplaceConnection._API_FIELDS.pageInfo.obj = PageInfo
MarketplaceEdge._API_FIELDS.node.obj = Marketplace
MediaChannelConnection._API_FIELDS.edges.obj = MediaChannelEdge
MediaChannelConnection._API_FIELDS.pageInfo.obj = PageInfo
MediaChannelEdge._API_FIELDS.node.obj = MediaChannel
MediaChannel._API_FIELDS.catalogs.obj = CatalogConnection
MediaChannel._API_FIELDS.marketplace.obj = Marketplace
CatalogConnection._API_FIELDS.edges.obj = CatalogEdge
CatalogConnection._API_FIELDS.pageInfo.obj = PageInfo
CatalogEdge._API_FIELDS.node.obj = Catalog
Catalog._API_FIELDS.mediaChannel.obj = MediaChannel
Catalog._API_FIELDS.products.obj = ProductConnection
ProductConnection._API_FIELDS.edges.obj = ProductEdge
ProductConnection._API_FIELDS.pageInfo.obj = PageInfo
ProductEdge._API_FIELDS.node.obj = Product
Product._API_FIELDS.vendor.obj = Vendor
Product._API_FIELDS.results.obj = ResultConnection
Product._API_FIELDS.marketingCampaigns.obj = MarketingCampaignConnection
Product._API_FIELDS.catalog.obj = Catalog
ResultResource._API_FIELDS.vendor.obj = Vendor
Vendor._API_FIELDS.marketplace.obj = Marketplace
Vendor._API_FIELDS.vendorTokens.obj = VendorTokenConnection
Vendor._API_FIELDS.products.obj = ProductConnection
VendorTokenConnection._API_FIELDS.edges.obj = VendorTokenEdge
VendorTokenConnection._API_FIELDS.pageInfo.obj = PageInfo
VendorTokenEdge._API_FIELDS.node.obj = VendorToken
VendorToken._API_FIELDS.vendor.obj = Vendor
VendorToken._API_FIELDS.marketplace.obj = Marketplace
ResultConnection._API_FIELDS.edges.obj = ResultEdge
ResultConnection._API_FIELDS.pageInfo.obj = PageInfo
ResultEdge._API_FIELDS.node.obj = Result
Result._API_FIELDS.analytics.obj = ResultAnalytics
Result._API_FIELDS.vendor.obj = Vendor
MarketingCampaignConnection._API_FIELDS.edges.obj = MarketingCampaignEdge
MarketingCampaignConnection._API_FIELDS.pageInfo.obj = PageInfo
MarketingCampaignEdge._API_FIELDS.node.obj = MarketingCampaign
MarketingCampaign._API_FIELDS.vendor.obj = Vendor
MarketingCampaign._API_FIELDS.GCPX.obj = GCPX
MarketingCampaign._API_FIELDS.marketingAds.obj = MarketingAdConnection
MarketingCampaign._API_FIELDS.products.obj = ProductConnection
MarketingCampaign._API_FIELDS.catalog.obj = Catalog
MarketingCampaign._API_FIELDS.campaignTemplate.obj = CampaignTemplate
MarketingCampaign._API_FIELDS.mediaChannel.obj = MediaChannel
MarketingCampaign._API_FIELDS.results.obj = ResultConnection
MarketingCampaign._API_FIELDS.notifications.obj = NotificationConnection
GCPX._API_FIELDS.campaignTemplate.obj = CampaignTemplate
GCPX._API_FIELDS.marketplace.obj = Marketplace
GCPX._API_FIELDS.marketingCampaigns.obj = MarketingCampaignConnection
MarketingAdConnection._API_FIELDS.edges.obj = MarketingAdEdge
MarketingAdConnection._API_FIELDS.pageInfo.obj = PageInfo
MarketingAdEdge._API_FIELDS.node.obj = MarketingAd
MarketingAd._API_FIELDS.vendor.obj = Vendor
MarketingAd._API_FIELDS.adPreviews.obj = AdPreview
MarketingAd._API_FIELDS.results.obj = ResultConnection
MarketingAd._API_FIELDS.marketingCampaign.obj = MarketingCampaign
NotificationConnection._API_FIELDS.edges.obj = NotificationEdge
NotificationConnection._API_FIELDS.pageInfo.obj = PageInfo
NotificationEdge._API_FIELDS.node.obj = Notification
CampaignTemplateConnection._API_FIELDS.edges.obj = CampaignTemplateEdge
CampaignTemplateConnection._API_FIELDS.pageInfo.obj = PageInfo
CampaignTemplateEdge._API_FIELDS.node.obj = CampaignTemplate
VendorConnection._API_FIELDS.edges.obj = VendorEdge
VendorConnection._API_FIELDS.pageInfo.obj = PageInfo
VendorEdge._API_FIELDS.node.obj = Vendor
CreativeTemplateConnection._API_FIELDS.edges.obj = CreativeTemplateEdge
CreativeTemplateConnection._API_FIELDS.pageInfo.obj = PageInfo
CreativeTemplateEdge._API_FIELDS.node.obj = CreativeTemplate
CreativeTemplate._API_FIELDS.marketplace.obj = Marketplace
CreativeTemplate._API_FIELDS.marketingCampaigns.obj = MarketingCampaignConnection
CreativeTemplate._API_FIELDS.creativeLayers.obj = CreativeLayerConnection
CreativeLayerConnection._API_FIELDS.edges.obj = CreativeLayerEdge
CreativeLayerConnection._API_FIELDS.pageInfo.obj = PageInfo
CreativeLayerEdge._API_FIELDS.node.obj = CreativeLayer
CreativeLayer._API_FIELDS.creativeTemplate.obj = CreativeTemplate
GCPXConnection._API_FIELDS.edges.obj = GCPXEdge
GCPXConnection._API_FIELDS.pageInfo.obj = PageInfo
GCPXEdge._API_FIELDS.node.obj = GCPX
CreativeFont._API_FIELDS.marketplace.obj = Marketplace
CreativeFontConnection._API_FIELDS.edges.obj = CreativeFontEdge
CreativeFontConnection._API_FIELDS.pageInfo.obj = PageInfo
CreativeFontEdge._API_FIELDS.node.obj = CreativeFont
CreativeImage._API_FIELDS.marketplace.obj = Marketplace
CreativeImageConnection._API_FIELDS.edges.obj = CreativeImageEdge
CreativeImageConnection._API_FIELDS.pageInfo.obj = PageInfo
CreativeImageEdge._API_FIELDS.node.obj = CreativeImage
Token._API_FIELDS.user.obj = User
MarketingCampaignSnapshot._API_FIELDS.marketingCampaign.obj = MarketingCampaign
MarketingCampaignSnapshotEdge._API_FIELDS.node.obj = MarketingCampaignSnapshot
MarketingCampaignSnapshotConnection._API_FIELDS.edges.obj = (
    MarketingCampaignSnapshotEdge
)
MarketingCampaignSnapshotConnection._API_FIELDS.pageInfo.obj = PageInfo
SingleUseToken._API_FIELDS.user.obj = User
SingleUseTokenEdge._API_FIELDS.node.obj = SingleUseToken
SingleUseTokenConnection._API_FIELDS.edges.obj = SingleUseTokenEdge
SingleUseTokenConnection._API_FIELDS.pageInfo.obj = PageInfo
__all__ = [
    "CampaignTemplate",
    "Marketplace",
    "EntitlementResource",
    "Organization",
    "UserConnection",
    "UserEdge",
    "User",
    "Me",
    "OrganizationConnection",
    "OrganizationEdge",
    "PageInfo",
    "EntitlementConnection",
    "EntitlementEdge",
    "Entitlement",
    "MarketplaceConnection",
    "MarketplaceEdge",
    "MediaChannelConnection",
    "MediaChannelEdge",
    "MediaChannel",
    "CatalogConnection",
    "CatalogEdge",
    "Catalog",
    "ProductConnection",
    "ProductEdge",
    "Product",
    "ResultResource",
    "Vendor",
    "VendorTokenConnection",
    "VendorTokenEdge",
    "VendorToken",
    "ResultConnection",
    "ResultEdge",
    "Result",
    "ResultAnalytics",
    "MarketingCampaignConnection",
    "MarketingCampaignEdge",
    "MarketingCampaign",
    "NotificationResource",
    "GCPX",
    "MarketingAdConnection",
    "MarketingAdEdge",
    "MarketingAd",
    "AdPreview",
    "NotificationConnection",
    "NotificationEdge",
    "Notification",
    "CampaignTemplateConnection",
    "CampaignTemplateEdge",
    "VendorConnection",
    "VendorEdge",
    "CreativeTemplateConnection",
    "CreativeTemplateEdge",
    "CreativeTemplate",
    "CreativeLayerConnection",
    "CreativeLayerEdge",
    "CreativeLayer",
    "GCPXConnection",
    "GCPXEdge",
    "CreativeFont",
    "CreativeFontConnection",
    "CreativeFontEdge",
    "CreativeImage",
    "CreativeImageConnection",
    "CreativeImageEdge",
    "Token",
    "Deletion",
    "RequestResult",
    "MarketingCampaignSnapshot",
    "MarketingCampaignSnapshotEdge",
    "MarketingCampaignSnapshotConnection",
    "SingleUseToken",
    "SingleUseTokenEdge",
    "SingleUseTokenConnection",
]
