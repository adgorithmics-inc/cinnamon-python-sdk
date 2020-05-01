from typing import Union, List

from .internals.base_classes import BaseCinnamonInput, BaseCinnamonField
from .internals.constants import CinnamonUndefined
from .internals import scalars
from . import enums

class SortInput(BaseCinnamonInput):
    class _FIELDS:
        class field(BaseCinnamonField):
            api_name = "field"
            api_kind = "SCALAR"
            api_kind_name = "NonEmptyString"
            python_iterable = None
            python_name = "field"
            scalar = scalars.NonEmptyString

        class order(BaseCinnamonField):
            api_name = "order"
            api_kind = "ENUM"
            api_kind_name = "SORT_ORDER"
            python_iterable = None
            python_name = "order"

    field: Union[str, None, CinnamonUndefined]
    order: Union[enums.SORT_ORDER, None, CinnamonUndefined]

    def __init__(
        self,
        field: Union[str, None, CinnamonUndefined] = CinnamonUndefined,
        order: Union[enums.SORT_ORDER, None, CinnamonUndefined] = CinnamonUndefined,
    ) -> None:
        super().__init__(field=field, order=order)


class UserLoginInput(BaseCinnamonInput):
    class _FIELDS:
        class email(BaseCinnamonField):
            api_name = "email"
            api_kind = "SCALAR"
            api_kind_name = "NonEmptyString"
            python_iterable = None
            python_name = "email"
            scalar = scalars.NonEmptyString

        class password(BaseCinnamonField):
            api_name = "password"
            api_kind = "SCALAR"
            api_kind_name = "NonEmptyString"
            python_iterable = None
            python_name = "password"
            scalar = scalars.NonEmptyString

    email: str
    password: str

    def __init__(self, email: str, password: str) -> None:
        super().__init__(email=email, password=password)


class RefreshTokenInput(BaseCinnamonInput):
    class _FIELDS:
        class refresh_token(BaseCinnamonField):
            api_name = "refreshToken"
            api_kind = "SCALAR"
            api_kind_name = "String"
            python_iterable = None
            python_name = "refresh_token"
            scalar = scalars.String

    refresh_token: str

    def __init__(self, refresh_token: str) -> None:
        super().__init__(refresh_token=refresh_token)


class CatalogCreateInput(BaseCinnamonInput):
    class _FIELDS:
        class name(BaseCinnamonField):
            api_name = "name"
            api_kind = "SCALAR"
            api_kind_name = "NonEmptyString"
            python_iterable = None
            python_name = "name"
            scalar = scalars.NonEmptyString

        class external_event_source_ids(BaseCinnamonField):
            api_name = "externalEventSourceIds"
            api_kind = "SCALAR"
            api_kind_name = "String"
            python_iterable = list
            python_name = "external_event_source_ids"
            scalar = scalars.String

        class media_channel_id(BaseCinnamonField):
            api_name = "mediaChannelId"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = None
            python_name = "media_channel_id"
            scalar = scalars.ObjectId

        class catalog_type(BaseCinnamonField):
            api_name = "catalogType"
            api_kind = "ENUM"
            api_kind_name = "CatalogType"
            python_iterable = None
            python_name = "catalog_type"

    name: str
    external_event_source_ids: List[str]
    media_channel_id: str
    catalog_type: enums.CatalogType

    def __init__(
        self,
        name: str,
        external_event_source_ids: List[str],
        media_channel_id: str,
        catalog_type: enums.CatalogType,
    ) -> None:
        super().__init__(
            name=name,
            external_event_source_ids=external_event_source_ids,
            media_channel_id=media_channel_id,
            catalog_type=catalog_type,
        )


class CatalogImportInput(BaseCinnamonInput):
    class _FIELDS:
        class media_channel_id(BaseCinnamonField):
            api_name = "mediaChannelId"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = None
            python_name = "media_channel_id"
            scalar = scalars.ObjectId

        class remote_id(BaseCinnamonField):
            api_name = "remoteId"
            api_kind = "SCALAR"
            api_kind_name = "String"
            python_iterable = None
            python_name = "remote_id"
            scalar = scalars.String

        class product_source(BaseCinnamonField):
            api_name = "productSource"
            api_kind = "ENUM"
            api_kind_name = "PRODUCT_SOURCE"
            python_iterable = None
            python_name = "product_source"

        class vendor_id(BaseCinnamonField):
            api_name = "vendorId"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = None
            python_name = "vendor_id"
            scalar = scalars.ObjectId

    media_channel_id: str
    remote_id: str
    product_source: Union[enums.PRODUCT_SOURCE, None, CinnamonUndefined]
    vendor_id: Union[str, None, CinnamonUndefined]

    def __init__(
        self,
        media_channel_id: str,
        remote_id: str,
        product_source: Union[
            enums.PRODUCT_SOURCE, None, CinnamonUndefined
        ] = CinnamonUndefined,
        vendor_id: Union[str, None, CinnamonUndefined] = CinnamonUndefined,
    ) -> None:
        super().__init__(
            media_channel_id=media_channel_id,
            remote_id=remote_id,
            product_source=product_source,
            vendor_id=vendor_id,
        )


class CatalogUpdateInput(BaseCinnamonInput):
    class _FIELDS:
        class external_event_source_ids(BaseCinnamonField):
            api_name = "externalEventSourceIds"
            api_kind = "SCALAR"
            api_kind_name = "String"
            python_iterable = list
            python_name = "external_event_source_ids"
            scalar = scalars.String

        class name(BaseCinnamonField):
            api_name = "name"
            api_kind = "SCALAR"
            api_kind_name = "NonEmptyString"
            python_iterable = None
            python_name = "name"
            scalar = scalars.NonEmptyString

    external_event_source_ids: List[str]
    name: Union[str, None, CinnamonUndefined]

    def __init__(
        self,
        external_event_source_ids: List[str],
        name: Union[str, None, CinnamonUndefined] = CinnamonUndefined,
    ) -> None:
        super().__init__(external_event_source_ids=external_event_source_ids, name=name)


class CatalogSyncInput(BaseCinnamonInput):
    class _FIELDS:
        class reconcile_state(BaseCinnamonField):
            api_name = "reconcileState"
            api_kind = "ENUM"
            api_kind_name = "ReconcileStateEnum"
            python_iterable = None
            python_name = "reconcile_state"

    reconcile_state: Union[enums.ReconcileStateEnum, None, CinnamonUndefined]

    def __init__(
        self,
        reconcile_state: Union[
            enums.ReconcileStateEnum, None, CinnamonUndefined
        ] = CinnamonUndefined,
    ) -> None:
        super().__init__(reconcile_state=reconcile_state)


class CreativeFontCreateInput(BaseCinnamonInput):
    class _FIELDS:
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

        class marketplace_id(BaseCinnamonField):
            api_name = "marketplaceId"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = None
            python_name = "marketplace_id"
            scalar = scalars.ObjectId

    name: str
    url: str
    properties: dict
    marketplace_id: str

    def __init__(
        self, name: str, url: str, properties: dict, marketplace_id: str
    ) -> None:
        super().__init__(
            name=name, url=url, properties=properties, marketplace_id=marketplace_id
        )


class CreativeFontUpdateInput(BaseCinnamonInput):
    class _FIELDS:
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

    name: Union[str, None, CinnamonUndefined]
    url: Union[str, None, CinnamonUndefined]
    properties: Union[dict, None, CinnamonUndefined]

    def __init__(
        self,
        name: Union[str, None, CinnamonUndefined] = CinnamonUndefined,
        url: Union[str, None, CinnamonUndefined] = CinnamonUndefined,
        properties: Union[dict, None, CinnamonUndefined] = CinnamonUndefined,
    ) -> None:
        super().__init__(name=name, url=url, properties=properties)


class CreativeImageCreateInput(BaseCinnamonInput):
    class _FIELDS:
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

        class marketplace_id(BaseCinnamonField):
            api_name = "marketplaceId"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = None
            python_name = "marketplace_id"
            scalar = scalars.ObjectId

    name: str
    url: str
    properties: dict
    marketplace_id: str

    def __init__(
        self, name: str, url: str, properties: dict, marketplace_id: str
    ) -> None:
        super().__init__(
            name=name, url=url, properties=properties, marketplace_id=marketplace_id
        )


class CreativeImageUpdateInput(BaseCinnamonInput):
    class _FIELDS:
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

    name: Union[str, None, CinnamonUndefined]
    url: Union[str, None, CinnamonUndefined]
    properties: Union[dict, None, CinnamonUndefined]

    def __init__(
        self,
        name: Union[str, None, CinnamonUndefined] = CinnamonUndefined,
        url: Union[str, None, CinnamonUndefined] = CinnamonUndefined,
        properties: Union[dict, None, CinnamonUndefined] = CinnamonUndefined,
    ) -> None:
        super().__init__(name=name, url=url, properties=properties)


class CreativeLayerCreateInput(BaseCinnamonInput):
    class _FIELDS:
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

        class creative_template_id(BaseCinnamonField):
            api_name = "creativeTemplateId"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = None
            python_name = "creative_template_id"
            scalar = scalars.ObjectId

    name: str
    height: int
    width: int
    x: int
    y: int
    order: int
    type: enums.CreativeLayerTypes
    properties: dict
    creative_template_id: str

    def __init__(
        self,
        name: str,
        height: int,
        width: int,
        x: int,
        y: int,
        order: int,
        type: enums.CreativeLayerTypes,
        properties: dict,
        creative_template_id: str,
    ) -> None:
        super().__init__(
            name=name,
            height=height,
            width=width,
            x=x,
            y=y,
            order=order,
            type=type,
            properties=properties,
            creative_template_id=creative_template_id,
        )


class CreativeLayerUpdateInput(BaseCinnamonInput):
    class _FIELDS:
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

    name: Union[str, None, CinnamonUndefined]
    height: Union[int, None, CinnamonUndefined]
    width: Union[int, None, CinnamonUndefined]
    x: Union[int, None, CinnamonUndefined]
    y: Union[int, None, CinnamonUndefined]
    order: Union[int, None, CinnamonUndefined]
    type: Union[enums.CreativeLayerTypes, None, CinnamonUndefined]
    properties: Union[dict, None, CinnamonUndefined]

    def __init__(
        self,
        name: Union[str, None, CinnamonUndefined] = CinnamonUndefined,
        height: Union[int, None, CinnamonUndefined] = CinnamonUndefined,
        width: Union[int, None, CinnamonUndefined] = CinnamonUndefined,
        x: Union[int, None, CinnamonUndefined] = CinnamonUndefined,
        y: Union[int, None, CinnamonUndefined] = CinnamonUndefined,
        order: Union[int, None, CinnamonUndefined] = CinnamonUndefined,
        type: Union[
            enums.CreativeLayerTypes, None, CinnamonUndefined
        ] = CinnamonUndefined,
        properties: Union[dict, None, CinnamonUndefined] = CinnamonUndefined,
    ) -> None:
        super().__init__(
            name=name,
            height=height,
            width=width,
            x=x,
            y=y,
            order=order,
            type=type,
            properties=properties,
        )


class CreativeTemplateCreateInput(BaseCinnamonInput):
    class _FIELDS:
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

        class marketplace_id(BaseCinnamonField):
            api_name = "marketplaceId"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = None
            python_name = "marketplace_id"
            scalar = scalars.ObjectId

    name: str
    height: int
    width: int
    marketplace_id: str

    def __init__(self, name: str, height: int, width: int, marketplace_id: str) -> None:
        super().__init__(
            name=name, height=height, width=width, marketplace_id=marketplace_id
        )


class CreativeTemplateUpdateInput(BaseCinnamonInput):
    class _FIELDS:
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

    name: Union[str, None, CinnamonUndefined]
    height: Union[int, None, CinnamonUndefined]
    width: Union[int, None, CinnamonUndefined]

    def __init__(
        self,
        name: Union[str, None, CinnamonUndefined] = CinnamonUndefined,
        height: Union[int, None, CinnamonUndefined] = CinnamonUndefined,
        width: Union[int, None, CinnamonUndefined] = CinnamonUndefined,
    ) -> None:
        super().__init__(name=name, height=height, width=width)


class EntitlementInput(BaseCinnamonInput):
    class _FIELDS:
        class resource_id(BaseCinnamonField):
            api_name = "resourceId"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = None
            python_name = "resource_id"
            scalar = scalars.ObjectId

        class user_id(BaseCinnamonField):
            api_name = "userId"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = None
            python_name = "user_id"
            scalar = scalars.ObjectId

        class permissions(BaseCinnamonField):
            api_name = "permissions"
            api_kind = "ENUM"
            api_kind_name = "AuthPermission"
            python_iterable = list
            python_name = "permissions"

    resource_id: str
    user_id: str
    permissions: List[enums.AuthPermission]

    def __init__(
        self, resource_id: str, user_id: str, permissions: List[enums.AuthPermission]
    ) -> None:
        super().__init__(
            resource_id=resource_id, user_id=user_id, permissions=permissions
        )


class EntitlementUpdateInput(BaseCinnamonInput):
    class _FIELDS:
        class permissions(BaseCinnamonField):
            api_name = "permissions"
            api_kind = "ENUM"
            api_kind_name = "AuthPermission"
            python_iterable = list
            python_name = "permissions"

    permissions: List[enums.AuthPermission]

    def __init__(self, permissions: List[enums.AuthPermission]) -> None:
        super().__init__(permissions=permissions)


class MarketingCampaignInput(BaseCinnamonInput):
    class _FIELDS:
        class campaign_template_id(BaseCinnamonField):
            api_name = "campaignTemplateId"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = None
            python_name = "campaign_template_id"
            scalar = scalars.ObjectId

        class creative_spec(BaseCinnamonField):
            api_name = "creativeSpec"
            api_kind = "SCALAR"
            api_kind_name = "JSONObject"
            python_iterable = None
            python_name = "creative_spec"
            scalar = scalars.JSONObject

        class product_ids(BaseCinnamonField):
            api_name = "productIds"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = list
            python_name = "product_ids"
            scalar = scalars.ObjectId

        class run_time_spec(BaseCinnamonField):
            api_name = "runTimeSpec"
            api_kind = "SCALAR"
            api_kind_name = "JSONObject"
            python_iterable = None
            python_name = "run_time_spec"
            scalar = scalars.JSONObject

        class location_spec(BaseCinnamonField):
            api_name = "locationSpec"
            api_kind = "SCALAR"
            api_kind_name = "JSONObject"
            python_iterable = None
            python_name = "location_spec"
            scalar = scalars.JSONObject

        class conversion_spec(BaseCinnamonField):
            api_name = "conversionSpec"
            api_kind = "SCALAR"
            api_kind_name = "JSONObject"
            python_iterable = None
            python_name = "conversion_spec"
            scalar = scalars.JSONObject

        class status(BaseCinnamonField):
            api_name = "status"
            api_kind = "ENUM"
            api_kind_name = "MarketingCampaignStatus"
            python_iterable = None
            python_name = "status"

        class name(BaseCinnamonField):
            api_name = "name"
            api_kind = "SCALAR"
            api_kind_name = "NonEmptyString"
            python_iterable = None
            python_name = "name"
            scalar = scalars.NonEmptyString

    campaign_template_id: str
    creative_spec: dict
    product_ids: List[str]
    run_time_spec: Union[dict, None, CinnamonUndefined]
    location_spec: Union[dict, None, CinnamonUndefined]
    conversion_spec: Union[dict, None, CinnamonUndefined]
    status: Union[enums.MarketingCampaignStatus, None, CinnamonUndefined]
    name: Union[str, None, CinnamonUndefined]

    def __init__(
        self,
        campaign_template_id: str,
        creative_spec: dict,
        product_ids: List[str],
        run_time_spec: Union[dict, None, CinnamonUndefined] = CinnamonUndefined,
        location_spec: Union[dict, None, CinnamonUndefined] = CinnamonUndefined,
        conversion_spec: Union[dict, None, CinnamonUndefined] = CinnamonUndefined,
        status: Union[
            enums.MarketingCampaignStatus, None, CinnamonUndefined
        ] = CinnamonUndefined,
        name: Union[str, None, CinnamonUndefined] = CinnamonUndefined,
    ) -> None:
        super().__init__(
            campaign_template_id=campaign_template_id,
            creative_spec=creative_spec,
            product_ids=product_ids,
            run_time_spec=run_time_spec,
            location_spec=location_spec,
            conversion_spec=conversion_spec,
            status=status,
            name=name,
        )


class MarketingCampaignUpdateInput(BaseCinnamonInput):
    class _FIELDS:
        class product_ids(BaseCinnamonField):
            api_name = "productIds"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = list
            python_name = "product_ids"
            scalar = scalars.ObjectId

        class creative_spec(BaseCinnamonField):
            api_name = "creativeSpec"
            api_kind = "SCALAR"
            api_kind_name = "JSONObject"
            python_iterable = None
            python_name = "creative_spec"
            scalar = scalars.JSONObject

        class run_time_spec(BaseCinnamonField):
            api_name = "runTimeSpec"
            api_kind = "SCALAR"
            api_kind_name = "JSONObject"
            python_iterable = None
            python_name = "run_time_spec"
            scalar = scalars.JSONObject

        class location_spec(BaseCinnamonField):
            api_name = "locationSpec"
            api_kind = "SCALAR"
            api_kind_name = "JSONObject"
            python_iterable = None
            python_name = "location_spec"
            scalar = scalars.JSONObject

        class status(BaseCinnamonField):
            api_name = "status"
            api_kind = "ENUM"
            api_kind_name = "MarketingCampaignStatus"
            python_iterable = None
            python_name = "status"

        class name(BaseCinnamonField):
            api_name = "name"
            api_kind = "SCALAR"
            api_kind_name = "NonEmptyString"
            python_iterable = None
            python_name = "name"
            scalar = scalars.NonEmptyString

    product_ids: List[str]
    creative_spec: Union[dict, None, CinnamonUndefined]
    run_time_spec: Union[dict, None, CinnamonUndefined]
    location_spec: Union[dict, None, CinnamonUndefined]
    status: Union[enums.MarketingCampaignStatus, None, CinnamonUndefined]
    name: Union[str, None, CinnamonUndefined]

    def __init__(
        self,
        product_ids: List[str],
        creative_spec: Union[dict, None, CinnamonUndefined] = CinnamonUndefined,
        run_time_spec: Union[dict, None, CinnamonUndefined] = CinnamonUndefined,
        location_spec: Union[dict, None, CinnamonUndefined] = CinnamonUndefined,
        status: Union[
            enums.MarketingCampaignStatus, None, CinnamonUndefined
        ] = CinnamonUndefined,
        name: Union[str, None, CinnamonUndefined] = CinnamonUndefined,
    ) -> None:
        super().__init__(
            product_ids=product_ids,
            creative_spec=creative_spec,
            run_time_spec=run_time_spec,
            location_spec=location_spec,
            status=status,
            name=name,
        )


class MarketingCampaignSyncInput(BaseCinnamonInput):
    class _FIELDS:
        class reconcile_state(BaseCinnamonField):
            api_name = "reconcileState"
            api_kind = "ENUM"
            api_kind_name = "ReconcileStateEnum"
            python_iterable = None
            python_name = "reconcile_state"

    reconcile_state: Union[enums.ReconcileStateEnum, None, CinnamonUndefined]

    def __init__(
        self,
        reconcile_state: Union[
            enums.ReconcileStateEnum, None, CinnamonUndefined
        ] = CinnamonUndefined,
    ) -> None:
        super().__init__(reconcile_state=reconcile_state)


class MarketplaceInput(BaseCinnamonInput):
    class _FIELDS:
        class name(BaseCinnamonField):
            api_name = "name"
            api_kind = "SCALAR"
            api_kind_name = "NonEmptyString"
            python_iterable = None
            python_name = "name"
            scalar = scalars.NonEmptyString

        class organization_id(BaseCinnamonField):
            api_name = "organizationId"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = None
            python_name = "organization_id"
            scalar = scalars.ObjectId

    name: str
    organization_id: str

    def __init__(self, name: str, organization_id: str) -> None:
        super().__init__(name=name, organization_id=organization_id)


class MarketplaceUpdateInput(BaseCinnamonInput):
    class _FIELDS:
        class name(BaseCinnamonField):
            api_name = "name"
            api_kind = "SCALAR"
            api_kind_name = "NonEmptyString"
            python_iterable = None
            python_name = "name"
            scalar = scalars.NonEmptyString

    name: Union[str, None, CinnamonUndefined]

    def __init__(
        self, name: Union[str, None, CinnamonUndefined] = CinnamonUndefined
    ) -> None:
        super().__init__(name=name)


class MediaChannelCreateInput(BaseCinnamonInput):
    class _FIELDS:
        class name(BaseCinnamonField):
            api_name = "name"
            api_kind = "SCALAR"
            api_kind_name = "NonEmptyString"
            python_iterable = None
            python_name = "name"
            scalar = scalars.NonEmptyString

        class marketplace_id(BaseCinnamonField):
            api_name = "marketplaceId"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = None
            python_name = "marketplace_id"
            scalar = scalars.ObjectId

        class platform(BaseCinnamonField):
            api_name = "platform"
            api_kind = "ENUM"
            api_kind_name = "Platform"
            python_iterable = None
            python_name = "platform"

        class token(BaseCinnamonField):
            api_name = "token"
            api_kind = "SCALAR"
            api_kind_name = "NonEmptyString"
            python_iterable = None
            python_name = "token"
            scalar = scalars.NonEmptyString

    name: str
    marketplace_id: str
    platform: enums.Platform
    token: str

    def __init__(
        self, name: str, marketplace_id: str, platform: enums.Platform, token: str
    ) -> None:
        super().__init__(
            name=name, marketplace_id=marketplace_id, platform=platform, token=token
        )


class MediaChannelImportInput(BaseCinnamonInput):
    class _FIELDS:
        class marketplace_id(BaseCinnamonField):
            api_name = "marketplaceId"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = None
            python_name = "marketplace_id"
            scalar = scalars.ObjectId

        class platform(BaseCinnamonField):
            api_name = "platform"
            api_kind = "ENUM"
            api_kind_name = "Platform"
            python_iterable = None
            python_name = "platform"

        class remote_id(BaseCinnamonField):
            api_name = "remoteId"
            api_kind = "SCALAR"
            api_kind_name = "String"
            python_iterable = None
            python_name = "remote_id"
            scalar = scalars.String

        class token(BaseCinnamonField):
            api_name = "token"
            api_kind = "SCALAR"
            api_kind_name = "NonEmptyString"
            python_iterable = None
            python_name = "token"
            scalar = scalars.NonEmptyString

    marketplace_id: str
    platform: enums.Platform
    remote_id: str
    token: str

    def __init__(
        self, marketplace_id: str, platform: enums.Platform, remote_id: str, token: str
    ) -> None:
        super().__init__(
            marketplace_id=marketplace_id,
            platform=platform,
            remote_id=remote_id,
            token=token,
        )


class MediaChannelUpdateInput(BaseCinnamonInput):
    class _FIELDS:
        class name(BaseCinnamonField):
            api_name = "name"
            api_kind = "SCALAR"
            api_kind_name = "NonEmptyString"
            python_iterable = None
            python_name = "name"
            scalar = scalars.NonEmptyString

        class token(BaseCinnamonField):
            api_name = "token"
            api_kind = "SCALAR"
            api_kind_name = "NonEmptyString"
            python_iterable = None
            python_name = "token"
            scalar = scalars.NonEmptyString

    name: Union[str, None, CinnamonUndefined]
    token: Union[str, None, CinnamonUndefined]

    def __init__(
        self,
        name: Union[str, None, CinnamonUndefined] = CinnamonUndefined,
        token: Union[str, None, CinnamonUndefined] = CinnamonUndefined,
    ) -> None:
        super().__init__(name=name, token=token)


class NotificationUpdateInput(BaseCinnamonInput):
    class _FIELDS:
        class status(BaseCinnamonField):
            api_name = "status"
            api_kind = "ENUM"
            api_kind_name = "NOTIFICATION_STATUS"
            python_iterable = None
            python_name = "status"

    status: Union[enums.NOTIFICATION_STATUS, None, CinnamonUndefined]

    def __init__(
        self,
        status: Union[
            enums.NOTIFICATION_STATUS, None, CinnamonUndefined
        ] = CinnamonUndefined,
    ) -> None:
        super().__init__(status=status)


class OrganizationInput(BaseCinnamonInput):
    class _FIELDS:
        class name(BaseCinnamonField):
            api_name = "name"
            api_kind = "SCALAR"
            api_kind_name = "NonEmptyString"
            python_iterable = None
            python_name = "name"
            scalar = scalars.NonEmptyString

    name: str

    def __init__(self, name: str) -> None:
        super().__init__(name=name)


class OrganizationUpdateInput(BaseCinnamonInput):
    class _FIELDS:
        class name(BaseCinnamonField):
            api_name = "name"
            api_kind = "SCALAR"
            api_kind_name = "NonEmptyString"
            python_iterable = None
            python_name = "name"
            scalar = scalars.NonEmptyString

    name: Union[str, None, CinnamonUndefined]

    def __init__(
        self, name: Union[str, None, CinnamonUndefined] = CinnamonUndefined
    ) -> None:
        super().__init__(name=name)


class ProductInput(BaseCinnamonInput):
    class _FIELDS:
        class vendor_id(BaseCinnamonField):
            api_name = "vendorId"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = None
            python_name = "vendor_id"
            scalar = scalars.ObjectId

        class catalog_id(BaseCinnamonField):
            api_name = "catalogId"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = None
            python_name = "catalog_id"
            scalar = scalars.ObjectId

        class metadata(BaseCinnamonField):
            api_name = "metadata"
            api_kind = "SCALAR"
            api_kind_name = "JSONObject"
            python_iterable = None
            python_name = "metadata"
            scalar = scalars.JSONObject

    vendor_id: str
    catalog_id: str
    metadata: dict

    def __init__(self, vendor_id: str, catalog_id: str, metadata: dict) -> None:
        super().__init__(vendor_id=vendor_id, catalog_id=catalog_id, metadata=metadata)


class ProductUpdateInput(BaseCinnamonInput):
    class _FIELDS:
        class metadata(BaseCinnamonField):
            api_name = "metadata"
            api_kind = "SCALAR"
            api_kind_name = "JSONObject"
            python_iterable = None
            python_name = "metadata"
            scalar = scalars.JSONObject

    metadata: dict

    def __init__(self, metadata: dict) -> None:
        super().__init__(metadata=metadata)


class RequestResetPasswordInput(BaseCinnamonInput):
    class _FIELDS:
        class email(BaseCinnamonField):
            api_name = "email"
            api_kind = "SCALAR"
            api_kind_name = "NonEmptyString"
            python_iterable = None
            python_name = "email"
            scalar = scalars.NonEmptyString

    email: str

    def __init__(self, email: str) -> None:
        super().__init__(email=email)


class ResetPasswordInput(BaseCinnamonInput):
    class _FIELDS:
        class token(BaseCinnamonField):
            api_name = "token"
            api_kind = "SCALAR"
            api_kind_name = "NonEmptyString"
            python_iterable = None
            python_name = "token"
            scalar = scalars.NonEmptyString

        class password(BaseCinnamonField):
            api_name = "password"
            api_kind = "SCALAR"
            api_kind_name = "NonEmptyString"
            python_iterable = None
            python_name = "password"
            scalar = scalars.NonEmptyString

    token: str
    password: str

    def __init__(self, token: str, password: str) -> None:
        super().__init__(token=token, password=password)


class UserUpdateInput(BaseCinnamonInput):
    class _FIELDS:
        class email(BaseCinnamonField):
            api_name = "email"
            api_kind = "SCALAR"
            api_kind_name = "NonEmptyString"
            python_iterable = None
            python_name = "email"
            scalar = scalars.NonEmptyString

        class first_name(BaseCinnamonField):
            api_name = "firstName"
            api_kind = "SCALAR"
            api_kind_name = "NonEmptyString"
            python_iterable = None
            python_name = "first_name"
            scalar = scalars.NonEmptyString

        class last_name(BaseCinnamonField):
            api_name = "lastName"
            api_kind = "SCALAR"
            api_kind_name = "NonEmptyString"
            python_iterable = None
            python_name = "last_name"
            scalar = scalars.NonEmptyString

        class password(BaseCinnamonField):
            api_name = "password"
            api_kind = "SCALAR"
            api_kind_name = "NonEmptyString"
            python_iterable = None
            python_name = "password"
            scalar = scalars.NonEmptyString

        class notice_opt_in(BaseCinnamonField):
            api_name = "noticeOptIn"
            api_kind = "SCALAR"
            api_kind_name = "Boolean"
            python_iterable = None
            python_name = "notice_opt_in"
            scalar = scalars.Boolean

        class newsletter_opt_in(BaseCinnamonField):
            api_name = "newsletterOptIn"
            api_kind = "SCALAR"
            api_kind_name = "Boolean"
            python_iterable = None
            python_name = "newsletter_opt_in"
            scalar = scalars.Boolean

    email: Union[str, None, CinnamonUndefined]
    first_name: Union[str, None, CinnamonUndefined]
    last_name: Union[str, None, CinnamonUndefined]
    password: Union[str, None, CinnamonUndefined]
    notice_opt_in: Union[bool, None, CinnamonUndefined]
    newsletter_opt_in: Union[bool, None, CinnamonUndefined]

    def __init__(
        self,
        email: Union[str, None, CinnamonUndefined] = CinnamonUndefined,
        first_name: Union[str, None, CinnamonUndefined] = CinnamonUndefined,
        last_name: Union[str, None, CinnamonUndefined] = CinnamonUndefined,
        password: Union[str, None, CinnamonUndefined] = CinnamonUndefined,
        notice_opt_in: Union[bool, None, CinnamonUndefined] = CinnamonUndefined,
        newsletter_opt_in: Union[bool, None, CinnamonUndefined] = CinnamonUndefined,
    ) -> None:
        super().__init__(
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password,
            notice_opt_in=notice_opt_in,
            newsletter_opt_in=newsletter_opt_in,
        )


class VendorInput(BaseCinnamonInput):
    class _FIELDS:
        class name(BaseCinnamonField):
            api_name = "name"
            api_kind = "SCALAR"
            api_kind_name = "NonEmptyString"
            python_iterable = None
            python_name = "name"
            scalar = scalars.NonEmptyString

        class marketplace_id(BaseCinnamonField):
            api_name = "marketplaceId"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = None
            python_name = "marketplace_id"
            scalar = scalars.ObjectId

    name: str
    marketplace_id: str

    def __init__(self, name: str, marketplace_id: str) -> None:
        super().__init__(name=name, marketplace_id=marketplace_id)


class VendorUpdateInput(BaseCinnamonInput):
    class _FIELDS:
        class name(BaseCinnamonField):
            api_name = "name"
            api_kind = "SCALAR"
            api_kind_name = "NonEmptyString"
            python_iterable = None
            python_name = "name"
            scalar = scalars.NonEmptyString

    name: Union[str, None, CinnamonUndefined]

    def __init__(
        self, name: Union[str, None, CinnamonUndefined] = CinnamonUndefined
    ) -> None:
        super().__init__(name=name)


class VendorTokenInput(BaseCinnamonInput):
    class _FIELDS:
        class vendor_id(BaseCinnamonField):
            api_name = "vendorId"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = None
            python_name = "vendor_id"
            scalar = scalars.ObjectId

        class email(BaseCinnamonField):
            api_name = "email"
            api_kind = "SCALAR"
            api_kind_name = "NonEmptyString"
            python_iterable = None
            python_name = "email"
            scalar = scalars.NonEmptyString

        class password(BaseCinnamonField):
            api_name = "password"
            api_kind = "SCALAR"
            api_kind_name = "NonEmptyString"
            python_iterable = None
            python_name = "password"
            scalar = scalars.NonEmptyString

    vendor_id: str
    email: Union[str, None, CinnamonUndefined]
    password: Union[str, None, CinnamonUndefined]

    def __init__(
        self,
        vendor_id: str,
        email: Union[str, None, CinnamonUndefined] = CinnamonUndefined,
        password: Union[str, None, CinnamonUndefined] = CinnamonUndefined,
    ) -> None:
        super().__init__(vendor_id=vendor_id, email=email, password=password)


class LoginVendorInput(BaseCinnamonInput):
    class _FIELDS:
        class marketplace_id(BaseCinnamonField):
            api_name = "marketplaceId"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = None
            python_name = "marketplace_id"
            scalar = scalars.ObjectId

        class email(BaseCinnamonField):
            api_name = "email"
            api_kind = "SCALAR"
            api_kind_name = "NonEmptyString"
            python_iterable = None
            python_name = "email"
            scalar = scalars.NonEmptyString

        class password(BaseCinnamonField):
            api_name = "password"
            api_kind = "SCALAR"
            api_kind_name = "NonEmptyString"
            python_iterable = None
            python_name = "password"
            scalar = scalars.NonEmptyString

    marketplace_id: str
    email: str
    password: str

    def __init__(self, marketplace_id: str, email: str, password: str) -> None:
        super().__init__(marketplace_id=marketplace_id, email=email, password=password)


class SetVendorPasswordInput(BaseCinnamonInput):
    class _FIELDS:
        class marketplace_id(BaseCinnamonField):
            api_name = "marketplaceId"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = None
            python_name = "marketplace_id"
            scalar = scalars.ObjectId

        class email(BaseCinnamonField):
            api_name = "email"
            api_kind = "SCALAR"
            api_kind_name = "NonEmptyString"
            python_iterable = None
            python_name = "email"
            scalar = scalars.NonEmptyString

        class password(BaseCinnamonField):
            api_name = "password"
            api_kind = "SCALAR"
            api_kind_name = "NonEmptyString"
            python_iterable = None
            python_name = "password"
            scalar = scalars.NonEmptyString

    marketplace_id: str
    email: str
    password: str

    def __init__(self, marketplace_id: str, email: str, password: str) -> None:
        super().__init__(marketplace_id=marketplace_id, email=email, password=password)


__all__ = [
    "SortInput",
    "UserLoginInput",
    "RefreshTokenInput",
    "CatalogCreateInput",
    "CatalogImportInput",
    "CatalogUpdateInput",
    "CatalogSyncInput",
    "CreativeFontCreateInput",
    "CreativeFontUpdateInput",
    "CreativeImageCreateInput",
    "CreativeImageUpdateInput",
    "CreativeLayerCreateInput",
    "CreativeLayerUpdateInput",
    "CreativeTemplateCreateInput",
    "CreativeTemplateUpdateInput",
    "EntitlementInput",
    "EntitlementUpdateInput",
    "MarketingCampaignInput",
    "MarketingCampaignUpdateInput",
    "MarketingCampaignSyncInput",
    "MarketplaceInput",
    "MarketplaceUpdateInput",
    "MediaChannelCreateInput",
    "MediaChannelImportInput",
    "MediaChannelUpdateInput",
    "NotificationUpdateInput",
    "OrganizationInput",
    "OrganizationUpdateInput",
    "ProductInput",
    "ProductUpdateInput",
    "RequestResetPasswordInput",
    "ResetPasswordInput",
    "UserUpdateInput",
    "VendorInput",
    "VendorUpdateInput",
    "VendorTokenInput",
    "LoginVendorInput",
    "SetVendorPasswordInput",
]
