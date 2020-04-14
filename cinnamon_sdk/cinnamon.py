from typing import Union, List
from datetime import datetime
from .internals.base_classes import BaseSyncCinnamon, BaseCinnamonField
from .internals.constants import CinnamonUndefined
from .internals import scalars
from . import fields as fields_module
from . import objects
from . import inputs

class _ARGUMENT_LEGENDS:
    class campaign_template:
        class id(BaseCinnamonField):
            api_name = "id"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = None
            python_name = "id"
            scalar = scalars.ObjectId

    class campaign_templates:
        class sort(BaseCinnamonField):
            api_name = "sort"
            api_kind = "INPUT_OBJECT"
            api_kind_name = "SortInput"
            python_iterable = None
            python_name = "sort"

        class filter(BaseCinnamonField):
            api_name = "filter"
            api_kind = "SCALAR"
            api_kind_name = "FilterInput"
            python_iterable = None
            python_name = "filter"
            scalar = scalars.FilterInput

        class show_deleted(BaseCinnamonField):
            api_name = "showDeleted"
            api_kind = "SCALAR"
            api_kind_name = "Boolean"
            python_iterable = None
            python_name = "show_deleted"
            scalar = scalars.Boolean

    class campaign_templates_with_current_gcpx:
        class sort(BaseCinnamonField):
            api_name = "sort"
            api_kind = "INPUT_OBJECT"
            api_kind_name = "SortInput"
            python_iterable = None
            python_name = "sort"

        class filter(BaseCinnamonField):
            api_name = "filter"
            api_kind = "SCALAR"
            api_kind_name = "FilterInput"
            python_iterable = None
            python_name = "filter"
            scalar = scalars.FilterInput

        class show_deleted(BaseCinnamonField):
            api_name = "showDeleted"
            api_kind = "SCALAR"
            api_kind_name = "Boolean"
            python_iterable = None
            python_name = "show_deleted"
            scalar = scalars.Boolean

    class catalog:
        class id(BaseCinnamonField):
            api_name = "id"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = None
            python_name = "id"
            scalar = scalars.ObjectId

    class catalogs:
        class sort(BaseCinnamonField):
            api_name = "sort"
            api_kind = "INPUT_OBJECT"
            api_kind_name = "SortInput"
            python_iterable = None
            python_name = "sort"

        class filter(BaseCinnamonField):
            api_name = "filter"
            api_kind = "SCALAR"
            api_kind_name = "FilterInput"
            python_iterable = None
            python_name = "filter"
            scalar = scalars.FilterInput

        class show_deleted(BaseCinnamonField):
            api_name = "showDeleted"
            api_kind = "SCALAR"
            api_kind_name = "Boolean"
            python_iterable = None
            python_name = "show_deleted"
            scalar = scalars.Boolean

    class creative_font:
        class id(BaseCinnamonField):
            api_name = "id"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = None
            python_name = "id"
            scalar = scalars.ObjectId

    class creative_fonts:
        class sort(BaseCinnamonField):
            api_name = "sort"
            api_kind = "INPUT_OBJECT"
            api_kind_name = "SortInput"
            python_iterable = None
            python_name = "sort"

        class filter(BaseCinnamonField):
            api_name = "filter"
            api_kind = "SCALAR"
            api_kind_name = "FilterInput"
            python_iterable = None
            python_name = "filter"
            scalar = scalars.FilterInput

        class show_deleted(BaseCinnamonField):
            api_name = "showDeleted"
            api_kind = "SCALAR"
            api_kind_name = "Boolean"
            python_iterable = None
            python_name = "show_deleted"
            scalar = scalars.Boolean

    class creative_image:
        class id(BaseCinnamonField):
            api_name = "id"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = None
            python_name = "id"
            scalar = scalars.ObjectId

    class creative_images:
        class sort(BaseCinnamonField):
            api_name = "sort"
            api_kind = "INPUT_OBJECT"
            api_kind_name = "SortInput"
            python_iterable = None
            python_name = "sort"

        class filter(BaseCinnamonField):
            api_name = "filter"
            api_kind = "SCALAR"
            api_kind_name = "FilterInput"
            python_iterable = None
            python_name = "filter"
            scalar = scalars.FilterInput

        class show_deleted(BaseCinnamonField):
            api_name = "showDeleted"
            api_kind = "SCALAR"
            api_kind_name = "Boolean"
            python_iterable = None
            python_name = "show_deleted"
            scalar = scalars.Boolean

    class creative_layer:
        class id(BaseCinnamonField):
            api_name = "id"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = None
            python_name = "id"
            scalar = scalars.ObjectId

    class creative_layers:
        class sort(BaseCinnamonField):
            api_name = "sort"
            api_kind = "INPUT_OBJECT"
            api_kind_name = "SortInput"
            python_iterable = None
            python_name = "sort"

        class filter(BaseCinnamonField):
            api_name = "filter"
            api_kind = "SCALAR"
            api_kind_name = "FilterInput"
            python_iterable = None
            python_name = "filter"
            scalar = scalars.FilterInput

        class show_deleted(BaseCinnamonField):
            api_name = "showDeleted"
            api_kind = "SCALAR"
            api_kind_name = "Boolean"
            python_iterable = None
            python_name = "show_deleted"
            scalar = scalars.Boolean

    class creative_template:
        class id(BaseCinnamonField):
            api_name = "id"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = None
            python_name = "id"
            scalar = scalars.ObjectId

    class creative_templates:
        class sort(BaseCinnamonField):
            api_name = "sort"
            api_kind = "INPUT_OBJECT"
            api_kind_name = "SortInput"
            python_iterable = None
            python_name = "sort"

        class filter(BaseCinnamonField):
            api_name = "filter"
            api_kind = "SCALAR"
            api_kind_name = "FilterInput"
            python_iterable = None
            python_name = "filter"
            scalar = scalars.FilterInput

        class show_deleted(BaseCinnamonField):
            api_name = "showDeleted"
            api_kind = "SCALAR"
            api_kind_name = "Boolean"
            python_iterable = None
            python_name = "show_deleted"
            scalar = scalars.Boolean

    class entitlement:
        class id(BaseCinnamonField):
            api_name = "id"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = None
            python_name = "id"
            scalar = scalars.ObjectId

    class entitlements:
        class sort(BaseCinnamonField):
            api_name = "sort"
            api_kind = "INPUT_OBJECT"
            api_kind_name = "SortInput"
            python_iterable = None
            python_name = "sort"

        class filter(BaseCinnamonField):
            api_name = "filter"
            api_kind = "SCALAR"
            api_kind_name = "FilterInput"
            python_iterable = None
            python_name = "filter"
            scalar = scalars.FilterInput

    class marketing_ad:
        class id(BaseCinnamonField):
            api_name = "id"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = None
            python_name = "id"
            scalar = scalars.ObjectId

    class marketing_ads:
        class sort(BaseCinnamonField):
            api_name = "sort"
            api_kind = "INPUT_OBJECT"
            api_kind_name = "SortInput"
            python_iterable = None
            python_name = "sort"

        class filter(BaseCinnamonField):
            api_name = "filter"
            api_kind = "SCALAR"
            api_kind_name = "FilterInput"
            python_iterable = None
            python_name = "filter"
            scalar = scalars.FilterInput

        class show_deleted(BaseCinnamonField):
            api_name = "showDeleted"
            api_kind = "SCALAR"
            api_kind_name = "Boolean"
            python_iterable = None
            python_name = "show_deleted"
            scalar = scalars.Boolean

    class marketing_campaign:
        class id(BaseCinnamonField):
            api_name = "id"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = None
            python_name = "id"
            scalar = scalars.ObjectId

    class marketing_campaigns:
        class sort(BaseCinnamonField):
            api_name = "sort"
            api_kind = "INPUT_OBJECT"
            api_kind_name = "SortInput"
            python_iterable = None
            python_name = "sort"

        class filter(BaseCinnamonField):
            api_name = "filter"
            api_kind = "SCALAR"
            api_kind_name = "FilterInput"
            python_iterable = None
            python_name = "filter"
            scalar = scalars.FilterInput

        class show_deleted(BaseCinnamonField):
            api_name = "showDeleted"
            api_kind = "SCALAR"
            api_kind_name = "Boolean"
            python_iterable = None
            python_name = "show_deleted"
            scalar = scalars.Boolean

    class marketplace:
        class id(BaseCinnamonField):
            api_name = "id"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = None
            python_name = "id"
            scalar = scalars.ObjectId

    class marketplaces:
        class sort(BaseCinnamonField):
            api_name = "sort"
            api_kind = "INPUT_OBJECT"
            api_kind_name = "SortInput"
            python_iterable = None
            python_name = "sort"

        class filter(BaseCinnamonField):
            api_name = "filter"
            api_kind = "SCALAR"
            api_kind_name = "FilterInput"
            python_iterable = None
            python_name = "filter"
            scalar = scalars.FilterInput

        class show_deleted(BaseCinnamonField):
            api_name = "showDeleted"
            api_kind = "SCALAR"
            api_kind_name = "Boolean"
            python_iterable = None
            python_name = "show_deleted"
            scalar = scalars.Boolean

    class media_channel:
        class id(BaseCinnamonField):
            api_name = "id"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = None
            python_name = "id"
            scalar = scalars.ObjectId

    class media_channels:
        class sort(BaseCinnamonField):
            api_name = "sort"
            api_kind = "INPUT_OBJECT"
            api_kind_name = "SortInput"
            python_iterable = None
            python_name = "sort"

        class filter(BaseCinnamonField):
            api_name = "filter"
            api_kind = "SCALAR"
            api_kind_name = "FilterInput"
            python_iterable = None
            python_name = "filter"
            scalar = scalars.FilterInput

        class show_deleted(BaseCinnamonField):
            api_name = "showDeleted"
            api_kind = "SCALAR"
            api_kind_name = "Boolean"
            python_iterable = None
            python_name = "show_deleted"
            scalar = scalars.Boolean

    class notification:
        class id(BaseCinnamonField):
            api_name = "id"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = None
            python_name = "id"
            scalar = scalars.ObjectId

    class notifications:
        class sort(BaseCinnamonField):
            api_name = "sort"
            api_kind = "INPUT_OBJECT"
            api_kind_name = "SortInput"
            python_iterable = None
            python_name = "sort"

        class filter(BaseCinnamonField):
            api_name = "filter"
            api_kind = "SCALAR"
            api_kind_name = "FilterInput"
            python_iterable = None
            python_name = "filter"
            scalar = scalars.FilterInput

    class organization:
        class id(BaseCinnamonField):
            api_name = "id"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = None
            python_name = "id"
            scalar = scalars.ObjectId

    class organizations:
        class sort(BaseCinnamonField):
            api_name = "sort"
            api_kind = "INPUT_OBJECT"
            api_kind_name = "SortInput"
            python_iterable = None
            python_name = "sort"

        class filter(BaseCinnamonField):
            api_name = "filter"
            api_kind = "SCALAR"
            api_kind_name = "FilterInput"
            python_iterable = None
            python_name = "filter"
            scalar = scalars.FilterInput

        class show_deleted(BaseCinnamonField):
            api_name = "showDeleted"
            api_kind = "SCALAR"
            api_kind_name = "Boolean"
            python_iterable = None
            python_name = "show_deleted"
            scalar = scalars.Boolean

    class product:
        class id(BaseCinnamonField):
            api_name = "id"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = None
            python_name = "id"
            scalar = scalars.ObjectId

    class products:
        class sort(BaseCinnamonField):
            api_name = "sort"
            api_kind = "INPUT_OBJECT"
            api_kind_name = "SortInput"
            python_iterable = None
            python_name = "sort"

        class filter(BaseCinnamonField):
            api_name = "filter"
            api_kind = "SCALAR"
            api_kind_name = "FilterInput"
            python_iterable = None
            python_name = "filter"
            scalar = scalars.FilterInput

        class show_deleted(BaseCinnamonField):
            api_name = "showDeleted"
            api_kind = "SCALAR"
            api_kind_name = "Boolean"
            python_iterable = None
            python_name = "show_deleted"
            scalar = scalars.Boolean

    class result:
        class id(BaseCinnamonField):
            api_name = "id"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = None
            python_name = "id"
            scalar = scalars.ObjectId

    class results:
        class sort(BaseCinnamonField):
            api_name = "sort"
            api_kind = "INPUT_OBJECT"
            api_kind_name = "SortInput"
            python_iterable = None
            python_name = "sort"

        class filter(BaseCinnamonField):
            api_name = "filter"
            api_kind = "SCALAR"
            api_kind_name = "FilterInput"
            python_iterable = None
            python_name = "filter"
            scalar = scalars.FilterInput

    class vendor:
        class id(BaseCinnamonField):
            api_name = "id"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = None
            python_name = "id"
            scalar = scalars.ObjectId

    class vendors:
        class sort(BaseCinnamonField):
            api_name = "sort"
            api_kind = "INPUT_OBJECT"
            api_kind_name = "SortInput"
            python_iterable = None
            python_name = "sort"

        class filter(BaseCinnamonField):
            api_name = "filter"
            api_kind = "SCALAR"
            api_kind_name = "FilterInput"
            python_iterable = None
            python_name = "filter"
            scalar = scalars.FilterInput

        class show_deleted(BaseCinnamonField):
            api_name = "showDeleted"
            api_kind = "SCALAR"
            api_kind_name = "Boolean"
            python_iterable = None
            python_name = "show_deleted"
            scalar = scalars.Boolean

    class vendor_token:
        class id(BaseCinnamonField):
            api_name = "id"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = None
            python_name = "id"
            scalar = scalars.ObjectId

    class vendor_tokens:
        class sort(BaseCinnamonField):
            api_name = "sort"
            api_kind = "INPUT_OBJECT"
            api_kind_name = "SortInput"
            python_iterable = None
            python_name = "sort"

        class filter(BaseCinnamonField):
            api_name = "filter"
            api_kind = "SCALAR"
            api_kind_name = "FilterInput"
            python_iterable = None
            python_name = "filter"
            scalar = scalars.FilterInput

    class refresh_login:
        class input(BaseCinnamonField):
            api_name = "input"
            api_kind = "INPUT_OBJECT"
            api_kind_name = "RefreshTokenInput"
            python_iterable = None
            python_name = "input"

    class create_catalog:
        class input(BaseCinnamonField):
            api_name = "input"
            api_kind = "INPUT_OBJECT"
            api_kind_name = "CatalogCreateInput"
            python_iterable = None
            python_name = "input"

    class import_catalog:
        class input(BaseCinnamonField):
            api_name = "input"
            api_kind = "INPUT_OBJECT"
            api_kind_name = "CatalogImportInput"
            python_iterable = None
            python_name = "input"

    class update_catalog:
        class input(BaseCinnamonField):
            api_name = "input"
            api_kind = "INPUT_OBJECT"
            api_kind_name = "CatalogUpdateInput"
            python_iterable = None
            python_name = "input"

        class id(BaseCinnamonField):
            api_name = "id"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = None
            python_name = "id"
            scalar = scalars.ObjectId

    class update_catalogs:
        class input(BaseCinnamonField):
            api_name = "input"
            api_kind = "INPUT_OBJECT"
            api_kind_name = "CatalogUpdateInput"
            python_iterable = None
            python_name = "input"

        class sort(BaseCinnamonField):
            api_name = "sort"
            api_kind = "INPUT_OBJECT"
            api_kind_name = "SortInput"
            python_iterable = None
            python_name = "sort"

        class filter(BaseCinnamonField):
            api_name = "filter"
            api_kind = "SCALAR"
            api_kind_name = "FilterInput"
            python_iterable = None
            python_name = "filter"
            scalar = scalars.FilterInput

        class show_deleted(BaseCinnamonField):
            api_name = "showDeleted"
            api_kind = "SCALAR"
            api_kind_name = "Boolean"
            python_iterable = None
            python_name = "show_deleted"
            scalar = scalars.Boolean

    class delete_catalog:
        class id(BaseCinnamonField):
            api_name = "id"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = None
            python_name = "id"
            scalar = scalars.ObjectId

    class create_creative_font:
        class input(BaseCinnamonField):
            api_name = "input"
            api_kind = "INPUT_OBJECT"
            api_kind_name = "CreativeFontCreateInput"
            python_iterable = None
            python_name = "input"

    class update_creative_font:
        class input(BaseCinnamonField):
            api_name = "input"
            api_kind = "INPUT_OBJECT"
            api_kind_name = "CreativeFontUpdateInput"
            python_iterable = None
            python_name = "input"

        class id(BaseCinnamonField):
            api_name = "id"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = None
            python_name = "id"
            scalar = scalars.ObjectId

    class update_creative_fonts:
        class input(BaseCinnamonField):
            api_name = "input"
            api_kind = "INPUT_OBJECT"
            api_kind_name = "CreativeFontUpdateInput"
            python_iterable = None
            python_name = "input"

        class sort(BaseCinnamonField):
            api_name = "sort"
            api_kind = "INPUT_OBJECT"
            api_kind_name = "SortInput"
            python_iterable = None
            python_name = "sort"

        class filter(BaseCinnamonField):
            api_name = "filter"
            api_kind = "SCALAR"
            api_kind_name = "FilterInput"
            python_iterable = None
            python_name = "filter"
            scalar = scalars.FilterInput

        class show_deleted(BaseCinnamonField):
            api_name = "showDeleted"
            api_kind = "SCALAR"
            api_kind_name = "Boolean"
            python_iterable = None
            python_name = "show_deleted"
            scalar = scalars.Boolean

    class delete_creative_font:
        class id(BaseCinnamonField):
            api_name = "id"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = None
            python_name = "id"
            scalar = scalars.ObjectId

    class create_creative_image:
        class input(BaseCinnamonField):
            api_name = "input"
            api_kind = "INPUT_OBJECT"
            api_kind_name = "CreativeImageCreateInput"
            python_iterable = None
            python_name = "input"

    class update_creative_image:
        class input(BaseCinnamonField):
            api_name = "input"
            api_kind = "INPUT_OBJECT"
            api_kind_name = "CreativeImageUpdateInput"
            python_iterable = None
            python_name = "input"

        class id(BaseCinnamonField):
            api_name = "id"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = None
            python_name = "id"
            scalar = scalars.ObjectId

    class update_creative_images:
        class input(BaseCinnamonField):
            api_name = "input"
            api_kind = "INPUT_OBJECT"
            api_kind_name = "CreativeImageUpdateInput"
            python_iterable = None
            python_name = "input"

        class sort(BaseCinnamonField):
            api_name = "sort"
            api_kind = "INPUT_OBJECT"
            api_kind_name = "SortInput"
            python_iterable = None
            python_name = "sort"

        class filter(BaseCinnamonField):
            api_name = "filter"
            api_kind = "SCALAR"
            api_kind_name = "FilterInput"
            python_iterable = None
            python_name = "filter"
            scalar = scalars.FilterInput

        class show_deleted(BaseCinnamonField):
            api_name = "showDeleted"
            api_kind = "SCALAR"
            api_kind_name = "Boolean"
            python_iterable = None
            python_name = "show_deleted"
            scalar = scalars.Boolean

    class delete_creative_image:
        class id(BaseCinnamonField):
            api_name = "id"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = None
            python_name = "id"
            scalar = scalars.ObjectId

    class create_creative_layer:
        class input(BaseCinnamonField):
            api_name = "input"
            api_kind = "INPUT_OBJECT"
            api_kind_name = "CreativeLayerCreateInput"
            python_iterable = None
            python_name = "input"

    class update_creative_layer:
        class input(BaseCinnamonField):
            api_name = "input"
            api_kind = "INPUT_OBJECT"
            api_kind_name = "CreativeLayerUpdateInput"
            python_iterable = None
            python_name = "input"

        class id(BaseCinnamonField):
            api_name = "id"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = None
            python_name = "id"
            scalar = scalars.ObjectId

    class update_creative_layers:
        class input(BaseCinnamonField):
            api_name = "input"
            api_kind = "INPUT_OBJECT"
            api_kind_name = "CreativeLayerUpdateInput"
            python_iterable = None
            python_name = "input"

        class sort(BaseCinnamonField):
            api_name = "sort"
            api_kind = "INPUT_OBJECT"
            api_kind_name = "SortInput"
            python_iterable = None
            python_name = "sort"

        class filter(BaseCinnamonField):
            api_name = "filter"
            api_kind = "SCALAR"
            api_kind_name = "FilterInput"
            python_iterable = None
            python_name = "filter"
            scalar = scalars.FilterInput

        class show_deleted(BaseCinnamonField):
            api_name = "showDeleted"
            api_kind = "SCALAR"
            api_kind_name = "Boolean"
            python_iterable = None
            python_name = "show_deleted"
            scalar = scalars.Boolean

    class delete_creative_layer:
        class id(BaseCinnamonField):
            api_name = "id"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = None
            python_name = "id"
            scalar = scalars.ObjectId

    class create_creative_template:
        class input(BaseCinnamonField):
            api_name = "input"
            api_kind = "INPUT_OBJECT"
            api_kind_name = "CreativeTemplateCreateInput"
            python_iterable = None
            python_name = "input"

    class update_creative_template:
        class input(BaseCinnamonField):
            api_name = "input"
            api_kind = "INPUT_OBJECT"
            api_kind_name = "CreativeTemplateUpdateInput"
            python_iterable = None
            python_name = "input"

        class id(BaseCinnamonField):
            api_name = "id"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = None
            python_name = "id"
            scalar = scalars.ObjectId

    class update_creative_templates:
        class input(BaseCinnamonField):
            api_name = "input"
            api_kind = "INPUT_OBJECT"
            api_kind_name = "CreativeTemplateUpdateInput"
            python_iterable = None
            python_name = "input"

        class sort(BaseCinnamonField):
            api_name = "sort"
            api_kind = "INPUT_OBJECT"
            api_kind_name = "SortInput"
            python_iterable = None
            python_name = "sort"

        class filter(BaseCinnamonField):
            api_name = "filter"
            api_kind = "SCALAR"
            api_kind_name = "FilterInput"
            python_iterable = None
            python_name = "filter"
            scalar = scalars.FilterInput

        class show_deleted(BaseCinnamonField):
            api_name = "showDeleted"
            api_kind = "SCALAR"
            api_kind_name = "Boolean"
            python_iterable = None
            python_name = "show_deleted"
            scalar = scalars.Boolean

    class delete_creative_template:
        class id(BaseCinnamonField):
            api_name = "id"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = None
            python_name = "id"
            scalar = scalars.ObjectId

    class create_entitlement:
        class input(BaseCinnamonField):
            api_name = "input"
            api_kind = "INPUT_OBJECT"
            api_kind_name = "EntitlementInput"
            python_iterable = None
            python_name = "input"

    class update_entitlement:
        class input(BaseCinnamonField):
            api_name = "input"
            api_kind = "INPUT_OBJECT"
            api_kind_name = "EntitlementUpdateInput"
            python_iterable = None
            python_name = "input"

        class id(BaseCinnamonField):
            api_name = "id"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = None
            python_name = "id"
            scalar = scalars.ObjectId

    class update_entitlements:
        class input(BaseCinnamonField):
            api_name = "input"
            api_kind = "INPUT_OBJECT"
            api_kind_name = "EntitlementUpdateInput"
            python_iterable = None
            python_name = "input"

        class sort(BaseCinnamonField):
            api_name = "sort"
            api_kind = "INPUT_OBJECT"
            api_kind_name = "SortInput"
            python_iterable = None
            python_name = "sort"

        class filter(BaseCinnamonField):
            api_name = "filter"
            api_kind = "SCALAR"
            api_kind_name = "FilterInput"
            python_iterable = None
            python_name = "filter"
            scalar = scalars.FilterInput

    class delete_entitlement:
        class id(BaseCinnamonField):
            api_name = "id"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = None
            python_name = "id"
            scalar = scalars.ObjectId

    class create_marketing_campaign:
        class input(BaseCinnamonField):
            api_name = "input"
            api_kind = "INPUT_OBJECT"
            api_kind_name = "MarketingCampaignInput"
            python_iterable = None
            python_name = "input"

    class update_marketing_campaign:
        class input(BaseCinnamonField):
            api_name = "input"
            api_kind = "INPUT_OBJECT"
            api_kind_name = "MarketingCampaignUpdateInput"
            python_iterable = None
            python_name = "input"

        class id(BaseCinnamonField):
            api_name = "id"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = None
            python_name = "id"
            scalar = scalars.ObjectId

    class update_marketing_campaigns:
        class input(BaseCinnamonField):
            api_name = "input"
            api_kind = "INPUT_OBJECT"
            api_kind_name = "MarketingCampaignUpdateInput"
            python_iterable = None
            python_name = "input"

        class sort(BaseCinnamonField):
            api_name = "sort"
            api_kind = "INPUT_OBJECT"
            api_kind_name = "SortInput"
            python_iterable = None
            python_name = "sort"

        class filter(BaseCinnamonField):
            api_name = "filter"
            api_kind = "SCALAR"
            api_kind_name = "FilterInput"
            python_iterable = None
            python_name = "filter"
            scalar = scalars.FilterInput

        class show_deleted(BaseCinnamonField):
            api_name = "showDeleted"
            api_kind = "SCALAR"
            api_kind_name = "Boolean"
            python_iterable = None
            python_name = "show_deleted"
            scalar = scalars.Boolean

    class sync_marketing_campaign:
        class id(BaseCinnamonField):
            api_name = "id"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = None
            python_name = "id"
            scalar = scalars.ObjectId

        class input(BaseCinnamonField):
            api_name = "input"
            api_kind = "INPUT_OBJECT"
            api_kind_name = "MarketingCampaignSyncInput"
            python_iterable = None
            python_name = "input"

    class approve_marketing_campaign:
        class last_change_date(BaseCinnamonField):
            api_name = "lastChangeDate"
            api_kind = "SCALAR"
            api_kind_name = "DateISO"
            python_iterable = None
            python_name = "last_change_date"
            scalar = scalars.DateISO

        class id(BaseCinnamonField):
            api_name = "id"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = None
            python_name = "id"
            scalar = scalars.ObjectId

    class delete_marketing_campaign:
        class id(BaseCinnamonField):
            api_name = "id"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = None
            python_name = "id"
            scalar = scalars.ObjectId

    class create_marketplace:
        class input(BaseCinnamonField):
            api_name = "input"
            api_kind = "INPUT_OBJECT"
            api_kind_name = "MarketplaceInput"
            python_iterable = None
            python_name = "input"

    class update_marketplace:
        class input(BaseCinnamonField):
            api_name = "input"
            api_kind = "INPUT_OBJECT"
            api_kind_name = "MarketplaceUpdateInput"
            python_iterable = None
            python_name = "input"

        class id(BaseCinnamonField):
            api_name = "id"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = None
            python_name = "id"
            scalar = scalars.ObjectId

    class update_marketplaces:
        class input(BaseCinnamonField):
            api_name = "input"
            api_kind = "INPUT_OBJECT"
            api_kind_name = "MarketplaceUpdateInput"
            python_iterable = None
            python_name = "input"

        class sort(BaseCinnamonField):
            api_name = "sort"
            api_kind = "INPUT_OBJECT"
            api_kind_name = "SortInput"
            python_iterable = None
            python_name = "sort"

        class filter(BaseCinnamonField):
            api_name = "filter"
            api_kind = "SCALAR"
            api_kind_name = "FilterInput"
            python_iterable = None
            python_name = "filter"
            scalar = scalars.FilterInput

        class show_deleted(BaseCinnamonField):
            api_name = "showDeleted"
            api_kind = "SCALAR"
            api_kind_name = "Boolean"
            python_iterable = None
            python_name = "show_deleted"
            scalar = scalars.Boolean

    class delete_marketplace:
        class id(BaseCinnamonField):
            api_name = "id"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = None
            python_name = "id"
            scalar = scalars.ObjectId

    class create_media_channel:
        class input(BaseCinnamonField):
            api_name = "input"
            api_kind = "INPUT_OBJECT"
            api_kind_name = "MediaChannelCreateInput"
            python_iterable = None
            python_name = "input"

    class import_media_channel:
        class input(BaseCinnamonField):
            api_name = "input"
            api_kind = "INPUT_OBJECT"
            api_kind_name = "MediaChannelImportInput"
            python_iterable = None
            python_name = "input"

    class update_media_channel:
        class input(BaseCinnamonField):
            api_name = "input"
            api_kind = "INPUT_OBJECT"
            api_kind_name = "MediaChannelUpdateInput"
            python_iterable = None
            python_name = "input"

        class id(BaseCinnamonField):
            api_name = "id"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = None
            python_name = "id"
            scalar = scalars.ObjectId

    class update_media_channels:
        class input(BaseCinnamonField):
            api_name = "input"
            api_kind = "INPUT_OBJECT"
            api_kind_name = "MediaChannelUpdateInput"
            python_iterable = None
            python_name = "input"

        class sort(BaseCinnamonField):
            api_name = "sort"
            api_kind = "INPUT_OBJECT"
            api_kind_name = "SortInput"
            python_iterable = None
            python_name = "sort"

        class filter(BaseCinnamonField):
            api_name = "filter"
            api_kind = "SCALAR"
            api_kind_name = "FilterInput"
            python_iterable = None
            python_name = "filter"
            scalar = scalars.FilterInput

        class show_deleted(BaseCinnamonField):
            api_name = "showDeleted"
            api_kind = "SCALAR"
            api_kind_name = "Boolean"
            python_iterable = None
            python_name = "show_deleted"
            scalar = scalars.Boolean

    class delete_media_channel:
        class id(BaseCinnamonField):
            api_name = "id"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = None
            python_name = "id"
            scalar = scalars.ObjectId

    class update_notification:
        class input(BaseCinnamonField):
            api_name = "input"
            api_kind = "INPUT_OBJECT"
            api_kind_name = "NotificationUpdateInput"
            python_iterable = None
            python_name = "input"

        class id(BaseCinnamonField):
            api_name = "id"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = None
            python_name = "id"
            scalar = scalars.ObjectId

    class update_notifications:
        class input(BaseCinnamonField):
            api_name = "input"
            api_kind = "INPUT_OBJECT"
            api_kind_name = "NotificationUpdateInput"
            python_iterable = None
            python_name = "input"

        class sort(BaseCinnamonField):
            api_name = "sort"
            api_kind = "INPUT_OBJECT"
            api_kind_name = "SortInput"
            python_iterable = None
            python_name = "sort"

        class filter(BaseCinnamonField):
            api_name = "filter"
            api_kind = "SCALAR"
            api_kind_name = "FilterInput"
            python_iterable = None
            python_name = "filter"
            scalar = scalars.FilterInput

    class create_organization:
        class input(BaseCinnamonField):
            api_name = "input"
            api_kind = "INPUT_OBJECT"
            api_kind_name = "OrganizationInput"
            python_iterable = None
            python_name = "input"

    class update_organization:
        class input(BaseCinnamonField):
            api_name = "input"
            api_kind = "INPUT_OBJECT"
            api_kind_name = "OrganizationUpdateInput"
            python_iterable = None
            python_name = "input"

        class id(BaseCinnamonField):
            api_name = "id"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = None
            python_name = "id"
            scalar = scalars.ObjectId

    class update_organizations:
        class input(BaseCinnamonField):
            api_name = "input"
            api_kind = "INPUT_OBJECT"
            api_kind_name = "OrganizationUpdateInput"
            python_iterable = None
            python_name = "input"

        class sort(BaseCinnamonField):
            api_name = "sort"
            api_kind = "INPUT_OBJECT"
            api_kind_name = "SortInput"
            python_iterable = None
            python_name = "sort"

        class filter(BaseCinnamonField):
            api_name = "filter"
            api_kind = "SCALAR"
            api_kind_name = "FilterInput"
            python_iterable = None
            python_name = "filter"
            scalar = scalars.FilterInput

        class show_deleted(BaseCinnamonField):
            api_name = "showDeleted"
            api_kind = "SCALAR"
            api_kind_name = "Boolean"
            python_iterable = None
            python_name = "show_deleted"
            scalar = scalars.Boolean

    class delete_organization:
        class id(BaseCinnamonField):
            api_name = "id"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = None
            python_name = "id"
            scalar = scalars.ObjectId

    class create_product:
        class input(BaseCinnamonField):
            api_name = "input"
            api_kind = "INPUT_OBJECT"
            api_kind_name = "ProductInput"
            python_iterable = None
            python_name = "input"

    class update_product:
        class input(BaseCinnamonField):
            api_name = "input"
            api_kind = "INPUT_OBJECT"
            api_kind_name = "ProductUpdateInput"
            python_iterable = None
            python_name = "input"

        class id(BaseCinnamonField):
            api_name = "id"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = None
            python_name = "id"
            scalar = scalars.ObjectId

    class update_products:
        class input(BaseCinnamonField):
            api_name = "input"
            api_kind = "INPUT_OBJECT"
            api_kind_name = "ProductUpdateInput"
            python_iterable = None
            python_name = "input"

        class sort(BaseCinnamonField):
            api_name = "sort"
            api_kind = "INPUT_OBJECT"
            api_kind_name = "SortInput"
            python_iterable = None
            python_name = "sort"

        class filter(BaseCinnamonField):
            api_name = "filter"
            api_kind = "SCALAR"
            api_kind_name = "FilterInput"
            python_iterable = None
            python_name = "filter"
            scalar = scalars.FilterInput

        class show_deleted(BaseCinnamonField):
            api_name = "showDeleted"
            api_kind = "SCALAR"
            api_kind_name = "Boolean"
            python_iterable = None
            python_name = "show_deleted"
            scalar = scalars.Boolean

    class delete_product:
        class id(BaseCinnamonField):
            api_name = "id"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = None
            python_name = "id"
            scalar = scalars.ObjectId

    class request_reset_password:
        class input(BaseCinnamonField):
            api_name = "input"
            api_kind = "INPUT_OBJECT"
            api_kind_name = "RequestResetPasswordInput"
            python_iterable = None
            python_name = "input"

    class reset_password:
        class input(BaseCinnamonField):
            api_name = "input"
            api_kind = "INPUT_OBJECT"
            api_kind_name = "ResetPasswordInput"
            python_iterable = None
            python_name = "input"

    class update_user:
        class input(BaseCinnamonField):
            api_name = "input"
            api_kind = "INPUT_OBJECT"
            api_kind_name = "UserUpdateInput"
            python_iterable = None
            python_name = "input"

    class create_vendor:
        class input(BaseCinnamonField):
            api_name = "input"
            api_kind = "INPUT_OBJECT"
            api_kind_name = "VendorInput"
            python_iterable = None
            python_name = "input"

    class update_vendor:
        class input(BaseCinnamonField):
            api_name = "input"
            api_kind = "INPUT_OBJECT"
            api_kind_name = "VendorUpdateInput"
            python_iterable = None
            python_name = "input"

        class id(BaseCinnamonField):
            api_name = "id"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = None
            python_name = "id"
            scalar = scalars.ObjectId

    class update_vendors:
        class input(BaseCinnamonField):
            api_name = "input"
            api_kind = "INPUT_OBJECT"
            api_kind_name = "VendorUpdateInput"
            python_iterable = None
            python_name = "input"

        class sort(BaseCinnamonField):
            api_name = "sort"
            api_kind = "INPUT_OBJECT"
            api_kind_name = "SortInput"
            python_iterable = None
            python_name = "sort"

        class filter(BaseCinnamonField):
            api_name = "filter"
            api_kind = "SCALAR"
            api_kind_name = "FilterInput"
            python_iterable = None
            python_name = "filter"
            scalar = scalars.FilterInput

        class show_deleted(BaseCinnamonField):
            api_name = "showDeleted"
            api_kind = "SCALAR"
            api_kind_name = "Boolean"
            python_iterable = None
            python_name = "show_deleted"
            scalar = scalars.Boolean

    class delete_vendor:
        class id(BaseCinnamonField):
            api_name = "id"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = None
            python_name = "id"
            scalar = scalars.ObjectId

    class create_vendor_token:
        class input(BaseCinnamonField):
            api_name = "input"
            api_kind = "INPUT_OBJECT"
            api_kind_name = "VendorTokenInput"
            python_iterable = None
            python_name = "input"

    class login_vendor:
        class input(BaseCinnamonField):
            api_name = "input"
            api_kind = "INPUT_OBJECT"
            api_kind_name = "LoginVendorInput"
            python_iterable = None
            python_name = "input"

    class set_vendor_password:
        class input(BaseCinnamonField):
            api_name = "input"
            api_kind = "INPUT_OBJECT"
            api_kind_name = "SetVendorPasswordInput"
            python_iterable = None
            python_name = "input"

    class delete_vendor_token:
        class id(BaseCinnamonField):
            api_name = "id"
            api_kind = "SCALAR"
            api_kind_name = "ObjectId"
            python_iterable = None
            python_name = "id"
            scalar = scalars.ObjectId


class Cinnamon(BaseSyncCinnamon):
    def campaign_template(
        self,
        id: str,
        fields: List[
            fields_module.CampaignTemplateFields
        ] = fields_module.CampaignTemplateFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.CampaignTemplate:
        query_args = self._query_builder(
            "query",
            "campaignTemplate",
            fields,
            {"id": id,},
            _ARGUMENT_LEGENDS.campaign_template,
            False,
        )
        return objects.CampaignTemplate(
            self.api(headers=headers, token=token, **query_args)["data"][
                "campaignTemplate"
            ],
        )

    def campaign_templates(
        self,
        sort: Union[inputs.SortInput, None, CinnamonUndefined] = CinnamonUndefined,
        filter: Union[dict, None, CinnamonUndefined] = CinnamonUndefined,
        show_deleted: Union[bool, None, CinnamonUndefined] = CinnamonUndefined,
        fields: List[
            fields_module.CampaignTemplateConnectionFields
        ] = fields_module.CampaignTemplateConnectionFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.CampaignTemplateConnection:
        query_args = self._query_builder(
            "query",
            "campaignTemplates",
            fields,
            {"sort": sort, "filter": filter, "show_deleted": show_deleted,},
            _ARGUMENT_LEGENDS.campaign_templates,
            True,
        )
        return self.iterate_edges(
            objects.CampaignTemplateConnection,
            query_args,
            headers,
            token,
            "campaignTemplates",
        )

    def campaign_templates_with_current_gcpx(
        self,
        sort: Union[inputs.SortInput, None, CinnamonUndefined] = CinnamonUndefined,
        filter: Union[dict, None, CinnamonUndefined] = CinnamonUndefined,
        show_deleted: Union[bool, None, CinnamonUndefined] = CinnamonUndefined,
        fields: List[
            fields_module.CampaignTemplateConnectionFields
        ] = fields_module.CampaignTemplateConnectionFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.CampaignTemplateConnection:
        query_args = self._query_builder(
            "query",
            "campaignTemplatesWithCurrentGCPX",
            fields,
            {"sort": sort, "filter": filter, "show_deleted": show_deleted,},
            _ARGUMENT_LEGENDS.campaign_templates_with_current_gcpx,
            True,
        )
        return self.iterate_edges(
            objects.CampaignTemplateConnection,
            query_args,
            headers,
            token,
            "campaignTemplatesWithCurrentGCPX",
        )

    def catalog(
        self,
        id: str,
        fields: List[
            fields_module.CatalogFields
        ] = fields_module.CatalogFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.Catalog:
        query_args = self._query_builder(
            "query", "catalog", fields, {"id": id,}, _ARGUMENT_LEGENDS.catalog, False,
        )
        return objects.Catalog(
            self.api(headers=headers, token=token, **query_args)["data"]["catalog"],
        )

    def catalogs(
        self,
        sort: Union[inputs.SortInput, None, CinnamonUndefined] = CinnamonUndefined,
        filter: Union[dict, None, CinnamonUndefined] = CinnamonUndefined,
        show_deleted: Union[bool, None, CinnamonUndefined] = CinnamonUndefined,
        fields: List[
            fields_module.CatalogConnectionFields
        ] = fields_module.CatalogConnectionFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.CatalogConnection:
        query_args = self._query_builder(
            "query",
            "catalogs",
            fields,
            {"sort": sort, "filter": filter, "show_deleted": show_deleted,},
            _ARGUMENT_LEGENDS.catalogs,
            True,
        )
        return self.iterate_edges(
            objects.CatalogConnection, query_args, headers, token, "catalogs",
        )

    def creative_font(
        self,
        id: str,
        fields: List[
            fields_module.CreativeFontFields
        ] = fields_module.CreativeFontFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.CreativeFont:
        query_args = self._query_builder(
            "query",
            "creativeFont",
            fields,
            {"id": id,},
            _ARGUMENT_LEGENDS.creative_font,
            False,
        )
        return objects.CreativeFont(
            self.api(headers=headers, token=token, **query_args)["data"][
                "creativeFont"
            ],
        )

    def creative_fonts(
        self,
        sort: Union[inputs.SortInput, None, CinnamonUndefined] = CinnamonUndefined,
        filter: Union[dict, None, CinnamonUndefined] = CinnamonUndefined,
        show_deleted: Union[bool, None, CinnamonUndefined] = CinnamonUndefined,
        fields: List[
            fields_module.CreativeFontConnectionFields
        ] = fields_module.CreativeFontConnectionFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.CreativeFontConnection:
        query_args = self._query_builder(
            "query",
            "creativeFonts",
            fields,
            {"sort": sort, "filter": filter, "show_deleted": show_deleted,},
            _ARGUMENT_LEGENDS.creative_fonts,
            True,
        )
        return self.iterate_edges(
            objects.CreativeFontConnection, query_args, headers, token, "creativeFonts",
        )

    def creative_image(
        self,
        id: str,
        fields: List[
            fields_module.CreativeImageFields
        ] = fields_module.CreativeImageFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.CreativeImage:
        query_args = self._query_builder(
            "query",
            "creativeImage",
            fields,
            {"id": id,},
            _ARGUMENT_LEGENDS.creative_image,
            False,
        )
        return objects.CreativeImage(
            self.api(headers=headers, token=token, **query_args)["data"][
                "creativeImage"
            ],
        )

    def creative_images(
        self,
        sort: Union[inputs.SortInput, None, CinnamonUndefined] = CinnamonUndefined,
        filter: Union[dict, None, CinnamonUndefined] = CinnamonUndefined,
        show_deleted: Union[bool, None, CinnamonUndefined] = CinnamonUndefined,
        fields: List[
            fields_module.CreativeImageConnectionFields
        ] = fields_module.CreativeImageConnectionFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.CreativeImageConnection:
        query_args = self._query_builder(
            "query",
            "creativeImages",
            fields,
            {"sort": sort, "filter": filter, "show_deleted": show_deleted,},
            _ARGUMENT_LEGENDS.creative_images,
            True,
        )
        return self.iterate_edges(
            objects.CreativeImageConnection,
            query_args,
            headers,
            token,
            "creativeImages",
        )

    def creative_layer(
        self,
        id: str,
        fields: List[
            fields_module.CreativeLayerFields
        ] = fields_module.CreativeLayerFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.CreativeLayer:
        query_args = self._query_builder(
            "query",
            "creativeLayer",
            fields,
            {"id": id,},
            _ARGUMENT_LEGENDS.creative_layer,
            False,
        )
        return objects.CreativeLayer(
            self.api(headers=headers, token=token, **query_args)["data"][
                "creativeLayer"
            ],
        )

    def creative_layers(
        self,
        sort: Union[inputs.SortInput, None, CinnamonUndefined] = CinnamonUndefined,
        filter: Union[dict, None, CinnamonUndefined] = CinnamonUndefined,
        show_deleted: Union[bool, None, CinnamonUndefined] = CinnamonUndefined,
        fields: List[
            fields_module.CreativeLayerConnectionFields
        ] = fields_module.CreativeLayerConnectionFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.CreativeLayerConnection:
        query_args = self._query_builder(
            "query",
            "creativeLayers",
            fields,
            {"sort": sort, "filter": filter, "show_deleted": show_deleted,},
            _ARGUMENT_LEGENDS.creative_layers,
            True,
        )
        return self.iterate_edges(
            objects.CreativeLayerConnection,
            query_args,
            headers,
            token,
            "creativeLayers",
        )

    def creative_template(
        self,
        id: str,
        fields: List[
            fields_module.CreativeTemplateFields
        ] = fields_module.CreativeTemplateFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.CreativeTemplate:
        query_args = self._query_builder(
            "query",
            "creativeTemplate",
            fields,
            {"id": id,},
            _ARGUMENT_LEGENDS.creative_template,
            False,
        )
        return objects.CreativeTemplate(
            self.api(headers=headers, token=token, **query_args)["data"][
                "creativeTemplate"
            ],
        )

    def creative_templates(
        self,
        sort: Union[inputs.SortInput, None, CinnamonUndefined] = CinnamonUndefined,
        filter: Union[dict, None, CinnamonUndefined] = CinnamonUndefined,
        show_deleted: Union[bool, None, CinnamonUndefined] = CinnamonUndefined,
        fields: List[
            fields_module.CreativeTemplateConnectionFields
        ] = fields_module.CreativeTemplateConnectionFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.CreativeTemplateConnection:
        query_args = self._query_builder(
            "query",
            "creativeTemplates",
            fields,
            {"sort": sort, "filter": filter, "show_deleted": show_deleted,},
            _ARGUMENT_LEGENDS.creative_templates,
            True,
        )
        return self.iterate_edges(
            objects.CreativeTemplateConnection,
            query_args,
            headers,
            token,
            "creativeTemplates",
        )

    def entitlement(
        self,
        id: str,
        fields: List[
            fields_module.EntitlementFields
        ] = fields_module.EntitlementFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.Entitlement:
        query_args = self._query_builder(
            "query",
            "entitlement",
            fields,
            {"id": id,},
            _ARGUMENT_LEGENDS.entitlement,
            False,
        )
        return objects.Entitlement(
            self.api(headers=headers, token=token, **query_args)["data"]["entitlement"],
        )

    def entitlements(
        self,
        sort: Union[inputs.SortInput, None, CinnamonUndefined] = CinnamonUndefined,
        filter: Union[dict, None, CinnamonUndefined] = CinnamonUndefined,
        fields: List[
            fields_module.EntitlementConnectionFields
        ] = fields_module.EntitlementConnectionFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.EntitlementConnection:
        query_args = self._query_builder(
            "query",
            "entitlements",
            fields,
            {"sort": sort, "filter": filter,},
            _ARGUMENT_LEGENDS.entitlements,
            True,
        )
        return self.iterate_edges(
            objects.EntitlementConnection, query_args, headers, token, "entitlements",
        )

    def marketing_ad(
        self,
        id: str,
        fields: List[
            fields_module.MarketingAdFields
        ] = fields_module.MarketingAdFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.MarketingAd:
        query_args = self._query_builder(
            "query",
            "marketingAd",
            fields,
            {"id": id,},
            _ARGUMENT_LEGENDS.marketing_ad,
            False,
        )
        return objects.MarketingAd(
            self.api(headers=headers, token=token, **query_args)["data"]["marketingAd"],
        )

    def marketing_ads(
        self,
        sort: Union[inputs.SortInput, None, CinnamonUndefined] = CinnamonUndefined,
        filter: Union[dict, None, CinnamonUndefined] = CinnamonUndefined,
        show_deleted: Union[bool, None, CinnamonUndefined] = CinnamonUndefined,
        fields: List[
            fields_module.MarketingAdConnectionFields
        ] = fields_module.MarketingAdConnectionFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.MarketingAdConnection:
        query_args = self._query_builder(
            "query",
            "marketingAds",
            fields,
            {"sort": sort, "filter": filter, "show_deleted": show_deleted,},
            _ARGUMENT_LEGENDS.marketing_ads,
            True,
        )
        return self.iterate_edges(
            objects.MarketingAdConnection, query_args, headers, token, "marketingAds",
        )

    def marketing_campaign(
        self,
        id: str,
        fields: List[
            fields_module.MarketingCampaignFields
        ] = fields_module.MarketingCampaignFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.MarketingCampaign:
        query_args = self._query_builder(
            "query",
            "marketingCampaign",
            fields,
            {"id": id,},
            _ARGUMENT_LEGENDS.marketing_campaign,
            False,
        )
        return objects.MarketingCampaign(
            self.api(headers=headers, token=token, **query_args)["data"][
                "marketingCampaign"
            ],
        )

    def marketing_campaigns(
        self,
        sort: Union[inputs.SortInput, None, CinnamonUndefined] = CinnamonUndefined,
        filter: Union[dict, None, CinnamonUndefined] = CinnamonUndefined,
        show_deleted: Union[bool, None, CinnamonUndefined] = CinnamonUndefined,
        fields: List[
            fields_module.MarketingCampaignConnectionFields
        ] = fields_module.MarketingCampaignConnectionFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.MarketingCampaignConnection:
        query_args = self._query_builder(
            "query",
            "marketingCampaigns",
            fields,
            {"sort": sort, "filter": filter, "show_deleted": show_deleted,},
            _ARGUMENT_LEGENDS.marketing_campaigns,
            True,
        )
        return self.iterate_edges(
            objects.MarketingCampaignConnection,
            query_args,
            headers,
            token,
            "marketingCampaigns",
        )

    def marketplace(
        self,
        id: str,
        fields: List[
            fields_module.MarketplaceFields
        ] = fields_module.MarketplaceFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.Marketplace:
        query_args = self._query_builder(
            "query",
            "marketplace",
            fields,
            {"id": id,},
            _ARGUMENT_LEGENDS.marketplace,
            False,
        )
        return objects.Marketplace(
            self.api(headers=headers, token=token, **query_args)["data"]["marketplace"],
        )

    def marketplaces(
        self,
        sort: Union[inputs.SortInput, None, CinnamonUndefined] = CinnamonUndefined,
        filter: Union[dict, None, CinnamonUndefined] = CinnamonUndefined,
        show_deleted: Union[bool, None, CinnamonUndefined] = CinnamonUndefined,
        fields: List[
            fields_module.MarketplaceConnectionFields
        ] = fields_module.MarketplaceConnectionFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.MarketplaceConnection:
        query_args = self._query_builder(
            "query",
            "marketplaces",
            fields,
            {"sort": sort, "filter": filter, "show_deleted": show_deleted,},
            _ARGUMENT_LEGENDS.marketplaces,
            True,
        )
        return self.iterate_edges(
            objects.MarketplaceConnection, query_args, headers, token, "marketplaces",
        )

    def me(
        self,
        fields: List[fields_module.MeFields] = fields_module.MeFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.Me:
        query_args = self._query_builder(
            "query", "me", fields, {}, _ARGUMENT_LEGENDS.me, False,
        )
        return objects.Me(
            self.api(headers=headers, token=token, **query_args)["data"]["me"],
        )

    def media_channel(
        self,
        id: str,
        fields: List[
            fields_module.MediaChannelFields
        ] = fields_module.MediaChannelFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.MediaChannel:
        query_args = self._query_builder(
            "query",
            "mediaChannel",
            fields,
            {"id": id,},
            _ARGUMENT_LEGENDS.media_channel,
            False,
        )
        return objects.MediaChannel(
            self.api(headers=headers, token=token, **query_args)["data"][
                "mediaChannel"
            ],
        )

    def media_channels(
        self,
        sort: Union[inputs.SortInput, None, CinnamonUndefined] = CinnamonUndefined,
        filter: Union[dict, None, CinnamonUndefined] = CinnamonUndefined,
        show_deleted: Union[bool, None, CinnamonUndefined] = CinnamonUndefined,
        fields: List[
            fields_module.MediaChannelConnectionFields
        ] = fields_module.MediaChannelConnectionFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.MediaChannelConnection:
        query_args = self._query_builder(
            "query",
            "mediaChannels",
            fields,
            {"sort": sort, "filter": filter, "show_deleted": show_deleted,},
            _ARGUMENT_LEGENDS.media_channels,
            True,
        )
        return self.iterate_edges(
            objects.MediaChannelConnection, query_args, headers, token, "mediaChannels",
        )

    def notification(
        self,
        id: str,
        fields: List[
            fields_module.NotificationFields
        ] = fields_module.NotificationFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.Notification:
        query_args = self._query_builder(
            "query",
            "notification",
            fields,
            {"id": id,},
            _ARGUMENT_LEGENDS.notification,
            False,
        )
        return objects.Notification(
            self.api(headers=headers, token=token, **query_args)["data"][
                "notification"
            ],
        )

    def notifications(
        self,
        sort: Union[inputs.SortInput, None, CinnamonUndefined] = CinnamonUndefined,
        filter: Union[dict, None, CinnamonUndefined] = CinnamonUndefined,
        fields: List[
            fields_module.NotificationConnectionFields
        ] = fields_module.NotificationConnectionFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.NotificationConnection:
        query_args = self._query_builder(
            "query",
            "notifications",
            fields,
            {"sort": sort, "filter": filter,},
            _ARGUMENT_LEGENDS.notifications,
            True,
        )
        return self.iterate_edges(
            objects.NotificationConnection, query_args, headers, token, "notifications",
        )

    def organization(
        self,
        id: str,
        fields: List[
            fields_module.OrganizationFields
        ] = fields_module.OrganizationFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.Organization:
        query_args = self._query_builder(
            "query",
            "organization",
            fields,
            {"id": id,},
            _ARGUMENT_LEGENDS.organization,
            False,
        )
        return objects.Organization(
            self.api(headers=headers, token=token, **query_args)["data"][
                "organization"
            ],
        )

    def organizations(
        self,
        sort: Union[inputs.SortInput, None, CinnamonUndefined] = CinnamonUndefined,
        filter: Union[dict, None, CinnamonUndefined] = CinnamonUndefined,
        show_deleted: Union[bool, None, CinnamonUndefined] = CinnamonUndefined,
        fields: List[
            fields_module.OrganizationConnectionFields
        ] = fields_module.OrganizationConnectionFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.OrganizationConnection:
        query_args = self._query_builder(
            "query",
            "organizations",
            fields,
            {"sort": sort, "filter": filter, "show_deleted": show_deleted,},
            _ARGUMENT_LEGENDS.organizations,
            True,
        )
        return self.iterate_edges(
            objects.OrganizationConnection, query_args, headers, token, "organizations",
        )

    def product(
        self,
        id: str,
        fields: List[
            fields_module.ProductFields
        ] = fields_module.ProductFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.Product:
        query_args = self._query_builder(
            "query", "product", fields, {"id": id,}, _ARGUMENT_LEGENDS.product, False,
        )
        return objects.Product(
            self.api(headers=headers, token=token, **query_args)["data"]["product"],
        )

    def products(
        self,
        sort: Union[inputs.SortInput, None, CinnamonUndefined] = CinnamonUndefined,
        filter: Union[dict, None, CinnamonUndefined] = CinnamonUndefined,
        show_deleted: Union[bool, None, CinnamonUndefined] = CinnamonUndefined,
        fields: List[
            fields_module.ProductConnectionFields
        ] = fields_module.ProductConnectionFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.ProductConnection:
        query_args = self._query_builder(
            "query",
            "products",
            fields,
            {"sort": sort, "filter": filter, "show_deleted": show_deleted,},
            _ARGUMENT_LEGENDS.products,
            True,
        )
        return self.iterate_edges(
            objects.ProductConnection, query_args, headers, token, "products",
        )

    def result(
        self,
        id: str,
        fields: List[
            fields_module.ResultFields
        ] = fields_module.ResultFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.Result:
        query_args = self._query_builder(
            "query", "result", fields, {"id": id,}, _ARGUMENT_LEGENDS.result, False,
        )
        return objects.Result(
            self.api(headers=headers, token=token, **query_args)["data"]["result"],
        )

    def results(
        self,
        sort: Union[inputs.SortInput, None, CinnamonUndefined] = CinnamonUndefined,
        filter: Union[dict, None, CinnamonUndefined] = CinnamonUndefined,
        fields: List[
            fields_module.ResultConnectionFields
        ] = fields_module.ResultConnectionFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.ResultConnection:
        query_args = self._query_builder(
            "query",
            "results",
            fields,
            {"sort": sort, "filter": filter,},
            _ARGUMENT_LEGENDS.results,
            True,
        )
        return self.iterate_edges(
            objects.ResultConnection, query_args, headers, token, "results",
        )

    def vendor(
        self,
        id: str,
        fields: List[
            fields_module.VendorFields
        ] = fields_module.VendorFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.Vendor:
        query_args = self._query_builder(
            "query", "vendor", fields, {"id": id,}, _ARGUMENT_LEGENDS.vendor, False,
        )
        return objects.Vendor(
            self.api(headers=headers, token=token, **query_args)["data"]["vendor"],
        )

    def vendors(
        self,
        sort: Union[inputs.SortInput, None, CinnamonUndefined] = CinnamonUndefined,
        filter: Union[dict, None, CinnamonUndefined] = CinnamonUndefined,
        show_deleted: Union[bool, None, CinnamonUndefined] = CinnamonUndefined,
        fields: List[
            fields_module.VendorConnectionFields
        ] = fields_module.VendorConnectionFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.VendorConnection:
        query_args = self._query_builder(
            "query",
            "vendors",
            fields,
            {"sort": sort, "filter": filter, "show_deleted": show_deleted,},
            _ARGUMENT_LEGENDS.vendors,
            True,
        )
        return self.iterate_edges(
            objects.VendorConnection, query_args, headers, token, "vendors",
        )

    def vendor_token(
        self,
        id: str,
        fields: List[
            fields_module.VendorTokenFields
        ] = fields_module.VendorTokenFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.VendorToken:
        query_args = self._query_builder(
            "query",
            "vendorToken",
            fields,
            {"id": id,},
            _ARGUMENT_LEGENDS.vendor_token,
            False,
        )
        return objects.VendorToken(
            self.api(headers=headers, token=token, **query_args)["data"]["vendorToken"],
        )

    def vendor_tokens(
        self,
        sort: Union[inputs.SortInput, None, CinnamonUndefined] = CinnamonUndefined,
        filter: Union[dict, None, CinnamonUndefined] = CinnamonUndefined,
        fields: List[
            fields_module.VendorTokenConnectionFields
        ] = fields_module.VendorTokenConnectionFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.VendorTokenConnection:
        query_args = self._query_builder(
            "query",
            "vendorTokens",
            fields,
            {"sort": sort, "filter": filter,},
            _ARGUMENT_LEGENDS.vendor_tokens,
            True,
        )
        return self.iterate_edges(
            objects.VendorTokenConnection, query_args, headers, token, "vendorTokens",
        )

    def refresh_login(
        self,
        input: inputs.RefreshTokenInput,
        fields: List[
            fields_module.TokenFields
        ] = fields_module.TokenFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.Token:
        query_args = self._query_builder(
            "mutation",
            "refreshLogin",
            fields,
            {"input": input,},
            _ARGUMENT_LEGENDS.refresh_login,
            False,
        )
        return objects.Token(
            self.api(headers=headers, token=token, **query_args)["data"][
                "refreshLogin"
            ],
        )

    def create_catalog(
        self,
        input: inputs.CatalogCreateInput,
        fields: List[
            fields_module.CatalogFields
        ] = fields_module.CatalogFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.Catalog:
        query_args = self._query_builder(
            "mutation",
            "createCatalog",
            fields,
            {"input": input,},
            _ARGUMENT_LEGENDS.create_catalog,
            False,
        )
        return objects.Catalog(
            self.api(headers=headers, token=token, **query_args)["data"][
                "createCatalog"
            ],
        )

    def import_catalog(
        self,
        input: inputs.CatalogImportInput,
        fields: List[
            fields_module.CatalogFields
        ] = fields_module.CatalogFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.Catalog:
        query_args = self._query_builder(
            "mutation",
            "importCatalog",
            fields,
            {"input": input,},
            _ARGUMENT_LEGENDS.import_catalog,
            False,
        )
        return objects.Catalog(
            self.api(headers=headers, token=token, **query_args)["data"][
                "importCatalog"
            ],
        )

    def update_catalog(
        self,
        input: inputs.CatalogUpdateInput,
        id: str,
        fields: List[
            fields_module.CatalogFields
        ] = fields_module.CatalogFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.Catalog:
        query_args = self._query_builder(
            "mutation",
            "updateCatalog",
            fields,
            {"input": input, "id": id,},
            _ARGUMENT_LEGENDS.update_catalog,
            False,
        )
        return objects.Catalog(
            self.api(headers=headers, token=token, **query_args)["data"][
                "updateCatalog"
            ],
        )

    def update_catalogs(
        self,
        input: inputs.CatalogUpdateInput,
        sort: Union[inputs.SortInput, None, CinnamonUndefined] = CinnamonUndefined,
        filter: Union[dict, None, CinnamonUndefined] = CinnamonUndefined,
        show_deleted: Union[bool, None, CinnamonUndefined] = CinnamonUndefined,
        fields: List[
            fields_module.CatalogConnectionFields
        ] = fields_module.CatalogConnectionFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.CatalogConnection:
        query_args = self._query_builder(
            "mutation",
            "updateCatalogs",
            fields,
            {
                "input": input,
                "sort": sort,
                "filter": filter,
                "show_deleted": show_deleted,
            },
            _ARGUMENT_LEGENDS.update_catalogs,
            True,
        )
        return self.iterate_edges(
            objects.CatalogConnection, query_args, headers, token, "updateCatalogs",
        )

    def delete_catalog(
        self,
        id: str,
        fields: List[
            fields_module.DeletionFields
        ] = fields_module.DeletionFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.Deletion:
        query_args = self._query_builder(
            "mutation",
            "deleteCatalog",
            fields,
            {"id": id,},
            _ARGUMENT_LEGENDS.delete_catalog,
            False,
        )
        return objects.Deletion(
            self.api(headers=headers, token=token, **query_args)["data"][
                "deleteCatalog"
            ],
        )

    def create_creative_font(
        self,
        input: inputs.CreativeFontCreateInput,
        fields: List[
            fields_module.CreativeFontFields
        ] = fields_module.CreativeFontFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.CreativeFont:
        query_args = self._query_builder(
            "mutation",
            "createCreativeFont",
            fields,
            {"input": input,},
            _ARGUMENT_LEGENDS.create_creative_font,
            False,
        )
        return objects.CreativeFont(
            self.api(headers=headers, token=token, **query_args)["data"][
                "createCreativeFont"
            ],
        )

    def update_creative_font(
        self,
        input: inputs.CreativeFontUpdateInput,
        id: str,
        fields: List[
            fields_module.CreativeFontFields
        ] = fields_module.CreativeFontFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.CreativeFont:
        query_args = self._query_builder(
            "mutation",
            "updateCreativeFont",
            fields,
            {"input": input, "id": id,},
            _ARGUMENT_LEGENDS.update_creative_font,
            False,
        )
        return objects.CreativeFont(
            self.api(headers=headers, token=token, **query_args)["data"][
                "updateCreativeFont"
            ],
        )

    def update_creative_fonts(
        self,
        input: inputs.CreativeFontUpdateInput,
        sort: Union[inputs.SortInput, None, CinnamonUndefined] = CinnamonUndefined,
        filter: Union[dict, None, CinnamonUndefined] = CinnamonUndefined,
        show_deleted: Union[bool, None, CinnamonUndefined] = CinnamonUndefined,
        fields: List[
            fields_module.CreativeFontConnectionFields
        ] = fields_module.CreativeFontConnectionFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.CreativeFontConnection:
        query_args = self._query_builder(
            "mutation",
            "updateCreativeFonts",
            fields,
            {
                "input": input,
                "sort": sort,
                "filter": filter,
                "show_deleted": show_deleted,
            },
            _ARGUMENT_LEGENDS.update_creative_fonts,
            True,
        )
        return self.iterate_edges(
            objects.CreativeFontConnection,
            query_args,
            headers,
            token,
            "updateCreativeFonts",
        )

    def delete_creative_font(
        self,
        id: str,
        fields: List[
            fields_module.DeletionFields
        ] = fields_module.DeletionFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.Deletion:
        query_args = self._query_builder(
            "mutation",
            "deleteCreativeFont",
            fields,
            {"id": id,},
            _ARGUMENT_LEGENDS.delete_creative_font,
            False,
        )
        return objects.Deletion(
            self.api(headers=headers, token=token, **query_args)["data"][
                "deleteCreativeFont"
            ],
        )

    def create_creative_image(
        self,
        input: inputs.CreativeImageCreateInput,
        fields: List[
            fields_module.CreativeImageFields
        ] = fields_module.CreativeImageFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.CreativeImage:
        query_args = self._query_builder(
            "mutation",
            "createCreativeImage",
            fields,
            {"input": input,},
            _ARGUMENT_LEGENDS.create_creative_image,
            False,
        )
        return objects.CreativeImage(
            self.api(headers=headers, token=token, **query_args)["data"][
                "createCreativeImage"
            ],
        )

    def update_creative_image(
        self,
        input: inputs.CreativeImageUpdateInput,
        id: str,
        fields: List[
            fields_module.CreativeImageFields
        ] = fields_module.CreativeImageFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.CreativeImage:
        query_args = self._query_builder(
            "mutation",
            "updateCreativeImage",
            fields,
            {"input": input, "id": id,},
            _ARGUMENT_LEGENDS.update_creative_image,
            False,
        )
        return objects.CreativeImage(
            self.api(headers=headers, token=token, **query_args)["data"][
                "updateCreativeImage"
            ],
        )

    def update_creative_images(
        self,
        input: inputs.CreativeImageUpdateInput,
        sort: Union[inputs.SortInput, None, CinnamonUndefined] = CinnamonUndefined,
        filter: Union[dict, None, CinnamonUndefined] = CinnamonUndefined,
        show_deleted: Union[bool, None, CinnamonUndefined] = CinnamonUndefined,
        fields: List[
            fields_module.CreativeImageConnectionFields
        ] = fields_module.CreativeImageConnectionFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.CreativeImageConnection:
        query_args = self._query_builder(
            "mutation",
            "updateCreativeImages",
            fields,
            {
                "input": input,
                "sort": sort,
                "filter": filter,
                "show_deleted": show_deleted,
            },
            _ARGUMENT_LEGENDS.update_creative_images,
            True,
        )
        return self.iterate_edges(
            objects.CreativeImageConnection,
            query_args,
            headers,
            token,
            "updateCreativeImages",
        )

    def delete_creative_image(
        self,
        id: str,
        fields: List[
            fields_module.DeletionFields
        ] = fields_module.DeletionFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.Deletion:
        query_args = self._query_builder(
            "mutation",
            "deleteCreativeImage",
            fields,
            {"id": id,},
            _ARGUMENT_LEGENDS.delete_creative_image,
            False,
        )
        return objects.Deletion(
            self.api(headers=headers, token=token, **query_args)["data"][
                "deleteCreativeImage"
            ],
        )

    def create_creative_layer(
        self,
        input: inputs.CreativeLayerCreateInput,
        fields: List[
            fields_module.CreativeLayerFields
        ] = fields_module.CreativeLayerFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.CreativeLayer:
        query_args = self._query_builder(
            "mutation",
            "createCreativeLayer",
            fields,
            {"input": input,},
            _ARGUMENT_LEGENDS.create_creative_layer,
            False,
        )
        return objects.CreativeLayer(
            self.api(headers=headers, token=token, **query_args)["data"][
                "createCreativeLayer"
            ],
        )

    def update_creative_layer(
        self,
        input: inputs.CreativeLayerUpdateInput,
        id: str,
        fields: List[
            fields_module.CreativeLayerFields
        ] = fields_module.CreativeLayerFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.CreativeLayer:
        query_args = self._query_builder(
            "mutation",
            "updateCreativeLayer",
            fields,
            {"input": input, "id": id,},
            _ARGUMENT_LEGENDS.update_creative_layer,
            False,
        )
        return objects.CreativeLayer(
            self.api(headers=headers, token=token, **query_args)["data"][
                "updateCreativeLayer"
            ],
        )

    def update_creative_layers(
        self,
        input: inputs.CreativeLayerUpdateInput,
        sort: Union[inputs.SortInput, None, CinnamonUndefined] = CinnamonUndefined,
        filter: Union[dict, None, CinnamonUndefined] = CinnamonUndefined,
        show_deleted: Union[bool, None, CinnamonUndefined] = CinnamonUndefined,
        fields: List[
            fields_module.CreativeLayerConnectionFields
        ] = fields_module.CreativeLayerConnectionFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.CreativeLayerConnection:
        query_args = self._query_builder(
            "mutation",
            "updateCreativeLayers",
            fields,
            {
                "input": input,
                "sort": sort,
                "filter": filter,
                "show_deleted": show_deleted,
            },
            _ARGUMENT_LEGENDS.update_creative_layers,
            True,
        )
        return self.iterate_edges(
            objects.CreativeLayerConnection,
            query_args,
            headers,
            token,
            "updateCreativeLayers",
        )

    def delete_creative_layer(
        self,
        id: str,
        fields: List[
            fields_module.DeletionFields
        ] = fields_module.DeletionFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.Deletion:
        query_args = self._query_builder(
            "mutation",
            "deleteCreativeLayer",
            fields,
            {"id": id,},
            _ARGUMENT_LEGENDS.delete_creative_layer,
            False,
        )
        return objects.Deletion(
            self.api(headers=headers, token=token, **query_args)["data"][
                "deleteCreativeLayer"
            ],
        )

    def create_creative_template(
        self,
        input: inputs.CreativeTemplateCreateInput,
        fields: List[
            fields_module.CreativeTemplateFields
        ] = fields_module.CreativeTemplateFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.CreativeTemplate:
        query_args = self._query_builder(
            "mutation",
            "createCreativeTemplate",
            fields,
            {"input": input,},
            _ARGUMENT_LEGENDS.create_creative_template,
            False,
        )
        return objects.CreativeTemplate(
            self.api(headers=headers, token=token, **query_args)["data"][
                "createCreativeTemplate"
            ],
        )

    def update_creative_template(
        self,
        input: inputs.CreativeTemplateUpdateInput,
        id: str,
        fields: List[
            fields_module.CreativeTemplateFields
        ] = fields_module.CreativeTemplateFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.CreativeTemplate:
        query_args = self._query_builder(
            "mutation",
            "updateCreativeTemplate",
            fields,
            {"input": input, "id": id,},
            _ARGUMENT_LEGENDS.update_creative_template,
            False,
        )
        return objects.CreativeTemplate(
            self.api(headers=headers, token=token, **query_args)["data"][
                "updateCreativeTemplate"
            ],
        )

    def update_creative_templates(
        self,
        input: inputs.CreativeTemplateUpdateInput,
        sort: Union[inputs.SortInput, None, CinnamonUndefined] = CinnamonUndefined,
        filter: Union[dict, None, CinnamonUndefined] = CinnamonUndefined,
        show_deleted: Union[bool, None, CinnamonUndefined] = CinnamonUndefined,
        fields: List[
            fields_module.CreativeTemplateConnectionFields
        ] = fields_module.CreativeTemplateConnectionFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.CreativeTemplateConnection:
        query_args = self._query_builder(
            "mutation",
            "updateCreativeTemplates",
            fields,
            {
                "input": input,
                "sort": sort,
                "filter": filter,
                "show_deleted": show_deleted,
            },
            _ARGUMENT_LEGENDS.update_creative_templates,
            True,
        )
        return self.iterate_edges(
            objects.CreativeTemplateConnection,
            query_args,
            headers,
            token,
            "updateCreativeTemplates",
        )

    def delete_creative_template(
        self,
        id: str,
        fields: List[
            fields_module.DeletionFields
        ] = fields_module.DeletionFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.Deletion:
        query_args = self._query_builder(
            "mutation",
            "deleteCreativeTemplate",
            fields,
            {"id": id,},
            _ARGUMENT_LEGENDS.delete_creative_template,
            False,
        )
        return objects.Deletion(
            self.api(headers=headers, token=token, **query_args)["data"][
                "deleteCreativeTemplate"
            ],
        )

    def create_entitlement(
        self,
        input: inputs.EntitlementInput,
        fields: List[
            fields_module.EntitlementFields
        ] = fields_module.EntitlementFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.Entitlement:
        query_args = self._query_builder(
            "mutation",
            "createEntitlement",
            fields,
            {"input": input,},
            _ARGUMENT_LEGENDS.create_entitlement,
            False,
        )
        return objects.Entitlement(
            self.api(headers=headers, token=token, **query_args)["data"][
                "createEntitlement"
            ],
        )

    def update_entitlement(
        self,
        input: inputs.EntitlementUpdateInput,
        id: str,
        fields: List[
            fields_module.EntitlementFields
        ] = fields_module.EntitlementFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.Entitlement:
        query_args = self._query_builder(
            "mutation",
            "updateEntitlement",
            fields,
            {"input": input, "id": id,},
            _ARGUMENT_LEGENDS.update_entitlement,
            False,
        )
        return objects.Entitlement(
            self.api(headers=headers, token=token, **query_args)["data"][
                "updateEntitlement"
            ],
        )

    def update_entitlements(
        self,
        input: inputs.EntitlementUpdateInput,
        sort: Union[inputs.SortInput, None, CinnamonUndefined] = CinnamonUndefined,
        filter: Union[dict, None, CinnamonUndefined] = CinnamonUndefined,
        fields: List[
            fields_module.EntitlementConnectionFields
        ] = fields_module.EntitlementConnectionFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.EntitlementConnection:
        query_args = self._query_builder(
            "mutation",
            "updateEntitlements",
            fields,
            {"input": input, "sort": sort, "filter": filter,},
            _ARGUMENT_LEGENDS.update_entitlements,
            True,
        )
        return self.iterate_edges(
            objects.EntitlementConnection,
            query_args,
            headers,
            token,
            "updateEntitlements",
        )

    def delete_entitlement(
        self,
        id: str,
        fields: List[
            fields_module.DeletionFields
        ] = fields_module.DeletionFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.Deletion:
        query_args = self._query_builder(
            "mutation",
            "deleteEntitlement",
            fields,
            {"id": id,},
            _ARGUMENT_LEGENDS.delete_entitlement,
            False,
        )
        return objects.Deletion(
            self.api(headers=headers, token=token, **query_args)["data"][
                "deleteEntitlement"
            ],
        )

    def create_marketing_campaign(
        self,
        input: inputs.MarketingCampaignInput,
        fields: List[
            fields_module.MarketingCampaignFields
        ] = fields_module.MarketingCampaignFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.MarketingCampaign:
        query_args = self._query_builder(
            "mutation",
            "createMarketingCampaign",
            fields,
            {"input": input,},
            _ARGUMENT_LEGENDS.create_marketing_campaign,
            False,
        )
        return objects.MarketingCampaign(
            self.api(headers=headers, token=token, **query_args)["data"][
                "createMarketingCampaign"
            ],
        )

    def update_marketing_campaign(
        self,
        input: inputs.MarketingCampaignUpdateInput,
        id: str,
        fields: List[
            fields_module.MarketingCampaignFields
        ] = fields_module.MarketingCampaignFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.MarketingCampaign:
        query_args = self._query_builder(
            "mutation",
            "updateMarketingCampaign",
            fields,
            {"input": input, "id": id,},
            _ARGUMENT_LEGENDS.update_marketing_campaign,
            False,
        )
        return objects.MarketingCampaign(
            self.api(headers=headers, token=token, **query_args)["data"][
                "updateMarketingCampaign"
            ],
        )

    def update_marketing_campaigns(
        self,
        input: inputs.MarketingCampaignUpdateInput,
        sort: Union[inputs.SortInput, None, CinnamonUndefined] = CinnamonUndefined,
        filter: Union[dict, None, CinnamonUndefined] = CinnamonUndefined,
        show_deleted: Union[bool, None, CinnamonUndefined] = CinnamonUndefined,
        fields: List[
            fields_module.MarketingCampaignConnectionFields
        ] = fields_module.MarketingCampaignConnectionFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.MarketingCampaignConnection:
        query_args = self._query_builder(
            "mutation",
            "updateMarketingCampaigns",
            fields,
            {
                "input": input,
                "sort": sort,
                "filter": filter,
                "show_deleted": show_deleted,
            },
            _ARGUMENT_LEGENDS.update_marketing_campaigns,
            True,
        )
        return self.iterate_edges(
            objects.MarketingCampaignConnection,
            query_args,
            headers,
            token,
            "updateMarketingCampaigns",
        )

    def sync_marketing_campaign(
        self,
        id: str,
        input: Union[
            inputs.MarketingCampaignSyncInput, None, CinnamonUndefined
        ] = CinnamonUndefined,
        fields: List[
            fields_module.MarketingCampaignFields
        ] = fields_module.MarketingCampaignFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.MarketingCampaign:
        query_args = self._query_builder(
            "mutation",
            "syncMarketingCampaign",
            fields,
            {"id": id, "input": input,},
            _ARGUMENT_LEGENDS.sync_marketing_campaign,
            False,
        )
        return objects.MarketingCampaign(
            self.api(headers=headers, token=token, **query_args)["data"][
                "syncMarketingCampaign"
            ],
        )

    def approve_marketing_campaign(
        self,
        last_change_date: datetime,
        id: str,
        fields: List[
            fields_module.MarketingCampaignFields
        ] = fields_module.MarketingCampaignFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.MarketingCampaign:
        query_args = self._query_builder(
            "mutation",
            "approveMarketingCampaign",
            fields,
            {"last_change_date": last_change_date, "id": id,},
            _ARGUMENT_LEGENDS.approve_marketing_campaign,
            False,
        )
        return objects.MarketingCampaign(
            self.api(headers=headers, token=token, **query_args)["data"][
                "approveMarketingCampaign"
            ],
        )

    def delete_marketing_campaign(
        self,
        id: str,
        fields: List[
            fields_module.DeletionFields
        ] = fields_module.DeletionFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.Deletion:
        query_args = self._query_builder(
            "mutation",
            "deleteMarketingCampaign",
            fields,
            {"id": id,},
            _ARGUMENT_LEGENDS.delete_marketing_campaign,
            False,
        )
        return objects.Deletion(
            self.api(headers=headers, token=token, **query_args)["data"][
                "deleteMarketingCampaign"
            ],
        )

    def create_marketplace(
        self,
        input: inputs.MarketplaceInput,
        fields: List[
            fields_module.MarketplaceFields
        ] = fields_module.MarketplaceFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.Marketplace:
        query_args = self._query_builder(
            "mutation",
            "createMarketplace",
            fields,
            {"input": input,},
            _ARGUMENT_LEGENDS.create_marketplace,
            False,
        )
        return objects.Marketplace(
            self.api(headers=headers, token=token, **query_args)["data"][
                "createMarketplace"
            ],
        )

    def update_marketplace(
        self,
        input: inputs.MarketplaceUpdateInput,
        id: str,
        fields: List[
            fields_module.MarketplaceFields
        ] = fields_module.MarketplaceFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.Marketplace:
        query_args = self._query_builder(
            "mutation",
            "updateMarketplace",
            fields,
            {"input": input, "id": id,},
            _ARGUMENT_LEGENDS.update_marketplace,
            False,
        )
        return objects.Marketplace(
            self.api(headers=headers, token=token, **query_args)["data"][
                "updateMarketplace"
            ],
        )

    def update_marketplaces(
        self,
        input: inputs.MarketplaceUpdateInput,
        sort: Union[inputs.SortInput, None, CinnamonUndefined] = CinnamonUndefined,
        filter: Union[dict, None, CinnamonUndefined] = CinnamonUndefined,
        show_deleted: Union[bool, None, CinnamonUndefined] = CinnamonUndefined,
        fields: List[
            fields_module.MarketplaceConnectionFields
        ] = fields_module.MarketplaceConnectionFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.MarketplaceConnection:
        query_args = self._query_builder(
            "mutation",
            "updateMarketplaces",
            fields,
            {
                "input": input,
                "sort": sort,
                "filter": filter,
                "show_deleted": show_deleted,
            },
            _ARGUMENT_LEGENDS.update_marketplaces,
            True,
        )
        return self.iterate_edges(
            objects.MarketplaceConnection,
            query_args,
            headers,
            token,
            "updateMarketplaces",
        )

    def delete_marketplace(
        self,
        id: str,
        fields: List[
            fields_module.DeletionFields
        ] = fields_module.DeletionFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.Deletion:
        query_args = self._query_builder(
            "mutation",
            "deleteMarketplace",
            fields,
            {"id": id,},
            _ARGUMENT_LEGENDS.delete_marketplace,
            False,
        )
        return objects.Deletion(
            self.api(headers=headers, token=token, **query_args)["data"][
                "deleteMarketplace"
            ],
        )

    def create_media_channel(
        self,
        input: inputs.MediaChannelCreateInput,
        fields: List[
            fields_module.MediaChannelFields
        ] = fields_module.MediaChannelFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.MediaChannel:
        query_args = self._query_builder(
            "mutation",
            "createMediaChannel",
            fields,
            {"input": input,},
            _ARGUMENT_LEGENDS.create_media_channel,
            False,
        )
        return objects.MediaChannel(
            self.api(headers=headers, token=token, **query_args)["data"][
                "createMediaChannel"
            ],
        )

    def import_media_channel(
        self,
        input: inputs.MediaChannelImportInput,
        fields: List[
            fields_module.MediaChannelFields
        ] = fields_module.MediaChannelFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.MediaChannel:
        query_args = self._query_builder(
            "mutation",
            "importMediaChannel",
            fields,
            {"input": input,},
            _ARGUMENT_LEGENDS.import_media_channel,
            False,
        )
        return objects.MediaChannel(
            self.api(headers=headers, token=token, **query_args)["data"][
                "importMediaChannel"
            ],
        )

    def update_media_channel(
        self,
        input: inputs.MediaChannelUpdateInput,
        id: str,
        fields: List[
            fields_module.MediaChannelFields
        ] = fields_module.MediaChannelFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.MediaChannel:
        query_args = self._query_builder(
            "mutation",
            "updateMediaChannel",
            fields,
            {"input": input, "id": id,},
            _ARGUMENT_LEGENDS.update_media_channel,
            False,
        )
        return objects.MediaChannel(
            self.api(headers=headers, token=token, **query_args)["data"][
                "updateMediaChannel"
            ],
        )

    def update_media_channels(
        self,
        input: inputs.MediaChannelUpdateInput,
        sort: Union[inputs.SortInput, None, CinnamonUndefined] = CinnamonUndefined,
        filter: Union[dict, None, CinnamonUndefined] = CinnamonUndefined,
        show_deleted: Union[bool, None, CinnamonUndefined] = CinnamonUndefined,
        fields: List[
            fields_module.MediaChannelConnectionFields
        ] = fields_module.MediaChannelConnectionFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.MediaChannelConnection:
        query_args = self._query_builder(
            "mutation",
            "updateMediaChannels",
            fields,
            {
                "input": input,
                "sort": sort,
                "filter": filter,
                "show_deleted": show_deleted,
            },
            _ARGUMENT_LEGENDS.update_media_channels,
            True,
        )
        return self.iterate_edges(
            objects.MediaChannelConnection,
            query_args,
            headers,
            token,
            "updateMediaChannels",
        )

    def delete_media_channel(
        self,
        id: str,
        fields: List[
            fields_module.DeletionFields
        ] = fields_module.DeletionFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.Deletion:
        query_args = self._query_builder(
            "mutation",
            "deleteMediaChannel",
            fields,
            {"id": id,},
            _ARGUMENT_LEGENDS.delete_media_channel,
            False,
        )
        return objects.Deletion(
            self.api(headers=headers, token=token, **query_args)["data"][
                "deleteMediaChannel"
            ],
        )

    def update_notification(
        self,
        input: inputs.NotificationUpdateInput,
        id: str,
        fields: List[
            fields_module.NotificationFields
        ] = fields_module.NotificationFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.Notification:
        query_args = self._query_builder(
            "mutation",
            "updateNotification",
            fields,
            {"input": input, "id": id,},
            _ARGUMENT_LEGENDS.update_notification,
            False,
        )
        return objects.Notification(
            self.api(headers=headers, token=token, **query_args)["data"][
                "updateNotification"
            ],
        )

    def update_notifications(
        self,
        input: inputs.NotificationUpdateInput,
        sort: Union[inputs.SortInput, None, CinnamonUndefined] = CinnamonUndefined,
        filter: Union[dict, None, CinnamonUndefined] = CinnamonUndefined,
        fields: List[
            fields_module.NotificationConnectionFields
        ] = fields_module.NotificationConnectionFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.NotificationConnection:
        query_args = self._query_builder(
            "mutation",
            "updateNotifications",
            fields,
            {"input": input, "sort": sort, "filter": filter,},
            _ARGUMENT_LEGENDS.update_notifications,
            True,
        )
        return self.iterate_edges(
            objects.NotificationConnection,
            query_args,
            headers,
            token,
            "updateNotifications",
        )

    def create_organization(
        self,
        input: inputs.OrganizationInput,
        fields: List[
            fields_module.OrganizationFields
        ] = fields_module.OrganizationFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.Organization:
        query_args = self._query_builder(
            "mutation",
            "createOrganization",
            fields,
            {"input": input,},
            _ARGUMENT_LEGENDS.create_organization,
            False,
        )
        return objects.Organization(
            self.api(headers=headers, token=token, **query_args)["data"][
                "createOrganization"
            ],
        )

    def update_organization(
        self,
        input: inputs.OrganizationUpdateInput,
        id: str,
        fields: List[
            fields_module.OrganizationFields
        ] = fields_module.OrganizationFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.Organization:
        query_args = self._query_builder(
            "mutation",
            "updateOrganization",
            fields,
            {"input": input, "id": id,},
            _ARGUMENT_LEGENDS.update_organization,
            False,
        )
        return objects.Organization(
            self.api(headers=headers, token=token, **query_args)["data"][
                "updateOrganization"
            ],
        )

    def update_organizations(
        self,
        input: inputs.OrganizationUpdateInput,
        sort: Union[inputs.SortInput, None, CinnamonUndefined] = CinnamonUndefined,
        filter: Union[dict, None, CinnamonUndefined] = CinnamonUndefined,
        show_deleted: Union[bool, None, CinnamonUndefined] = CinnamonUndefined,
        fields: List[
            fields_module.OrganizationConnectionFields
        ] = fields_module.OrganizationConnectionFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.OrganizationConnection:
        query_args = self._query_builder(
            "mutation",
            "updateOrganizations",
            fields,
            {
                "input": input,
                "sort": sort,
                "filter": filter,
                "show_deleted": show_deleted,
            },
            _ARGUMENT_LEGENDS.update_organizations,
            True,
        )
        return self.iterate_edges(
            objects.OrganizationConnection,
            query_args,
            headers,
            token,
            "updateOrganizations",
        )

    def delete_organization(
        self,
        id: str,
        fields: List[
            fields_module.DeletionFields
        ] = fields_module.DeletionFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.Deletion:
        query_args = self._query_builder(
            "mutation",
            "deleteOrganization",
            fields,
            {"id": id,},
            _ARGUMENT_LEGENDS.delete_organization,
            False,
        )
        return objects.Deletion(
            self.api(headers=headers, token=token, **query_args)["data"][
                "deleteOrganization"
            ],
        )

    def create_product(
        self,
        input: inputs.ProductInput,
        fields: List[
            fields_module.ProductFields
        ] = fields_module.ProductFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.Product:
        query_args = self._query_builder(
            "mutation",
            "createProduct",
            fields,
            {"input": input,},
            _ARGUMENT_LEGENDS.create_product,
            False,
        )
        return objects.Product(
            self.api(headers=headers, token=token, **query_args)["data"][
                "createProduct"
            ],
        )

    def update_product(
        self,
        input: inputs.ProductUpdateInput,
        id: str,
        fields: List[
            fields_module.ProductFields
        ] = fields_module.ProductFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.Product:
        query_args = self._query_builder(
            "mutation",
            "updateProduct",
            fields,
            {"input": input, "id": id,},
            _ARGUMENT_LEGENDS.update_product,
            False,
        )
        return objects.Product(
            self.api(headers=headers, token=token, **query_args)["data"][
                "updateProduct"
            ],
        )

    def update_products(
        self,
        input: inputs.ProductUpdateInput,
        sort: Union[inputs.SortInput, None, CinnamonUndefined] = CinnamonUndefined,
        filter: Union[dict, None, CinnamonUndefined] = CinnamonUndefined,
        show_deleted: Union[bool, None, CinnamonUndefined] = CinnamonUndefined,
        fields: List[
            fields_module.ProductConnectionFields
        ] = fields_module.ProductConnectionFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.ProductConnection:
        query_args = self._query_builder(
            "mutation",
            "updateProducts",
            fields,
            {
                "input": input,
                "sort": sort,
                "filter": filter,
                "show_deleted": show_deleted,
            },
            _ARGUMENT_LEGENDS.update_products,
            True,
        )
        return self.iterate_edges(
            objects.ProductConnection, query_args, headers, token, "updateProducts",
        )

    def delete_product(
        self,
        id: str,
        fields: List[
            fields_module.DeletionFields
        ] = fields_module.DeletionFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.Deletion:
        query_args = self._query_builder(
            "mutation",
            "deleteProduct",
            fields,
            {"id": id,},
            _ARGUMENT_LEGENDS.delete_product,
            False,
        )
        return objects.Deletion(
            self.api(headers=headers, token=token, **query_args)["data"][
                "deleteProduct"
            ],
        )

    def request_reset_password(
        self,
        input: inputs.RequestResetPasswordInput,
        fields: List[
            fields_module.RequestResultFields
        ] = fields_module.RequestResultFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.RequestResult:
        query_args = self._query_builder(
            "mutation",
            "requestResetPassword",
            fields,
            {"input": input,},
            _ARGUMENT_LEGENDS.request_reset_password,
            False,
        )
        return objects.RequestResult(
            self.api(headers=headers, token=token, **query_args)["data"][
                "requestResetPassword"
            ],
        )

    def reset_password(
        self,
        input: inputs.ResetPasswordInput,
        fields: List[
            fields_module.UserFields
        ] = fields_module.UserFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.User:
        query_args = self._query_builder(
            "mutation",
            "resetPassword",
            fields,
            {"input": input,},
            _ARGUMENT_LEGENDS.reset_password,
            False,
        )
        return objects.User(
            self.api(headers=headers, token=token, **query_args)["data"][
                "resetPassword"
            ],
        )

    def update_user(
        self,
        input: inputs.UserUpdateInput,
        fields: List[
            fields_module.UserFields
        ] = fields_module.UserFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.User:
        query_args = self._query_builder(
            "mutation",
            "updateUser",
            fields,
            {"input": input,},
            _ARGUMENT_LEGENDS.update_user,
            False,
        )
        return objects.User(
            self.api(headers=headers, token=token, **query_args)["data"]["updateUser"],
        )

    def create_vendor(
        self,
        input: inputs.VendorInput,
        fields: List[
            fields_module.VendorFields
        ] = fields_module.VendorFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.Vendor:
        query_args = self._query_builder(
            "mutation",
            "createVendor",
            fields,
            {"input": input,},
            _ARGUMENT_LEGENDS.create_vendor,
            False,
        )
        return objects.Vendor(
            self.api(headers=headers, token=token, **query_args)["data"][
                "createVendor"
            ],
        )

    def update_vendor(
        self,
        input: inputs.VendorUpdateInput,
        id: str,
        fields: List[
            fields_module.VendorFields
        ] = fields_module.VendorFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.Vendor:
        query_args = self._query_builder(
            "mutation",
            "updateVendor",
            fields,
            {"input": input, "id": id,},
            _ARGUMENT_LEGENDS.update_vendor,
            False,
        )
        return objects.Vendor(
            self.api(headers=headers, token=token, **query_args)["data"][
                "updateVendor"
            ],
        )

    def update_vendors(
        self,
        input: inputs.VendorUpdateInput,
        sort: Union[inputs.SortInput, None, CinnamonUndefined] = CinnamonUndefined,
        filter: Union[dict, None, CinnamonUndefined] = CinnamonUndefined,
        show_deleted: Union[bool, None, CinnamonUndefined] = CinnamonUndefined,
        fields: List[
            fields_module.VendorConnectionFields
        ] = fields_module.VendorConnectionFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.VendorConnection:
        query_args = self._query_builder(
            "mutation",
            "updateVendors",
            fields,
            {
                "input": input,
                "sort": sort,
                "filter": filter,
                "show_deleted": show_deleted,
            },
            _ARGUMENT_LEGENDS.update_vendors,
            True,
        )
        return self.iterate_edges(
            objects.VendorConnection, query_args, headers, token, "updateVendors",
        )

    def delete_vendor(
        self,
        id: str,
        fields: List[
            fields_module.DeletionFields
        ] = fields_module.DeletionFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.Deletion:
        query_args = self._query_builder(
            "mutation",
            "deleteVendor",
            fields,
            {"id": id,},
            _ARGUMENT_LEGENDS.delete_vendor,
            False,
        )
        return objects.Deletion(
            self.api(headers=headers, token=token, **query_args)["data"][
                "deleteVendor"
            ],
        )

    def create_vendor_token(
        self,
        input: inputs.VendorTokenInput,
        fields: List[
            fields_module.VendorTokenFields
        ] = fields_module.VendorTokenFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.VendorToken:
        query_args = self._query_builder(
            "mutation",
            "createVendorToken",
            fields,
            {"input": input,},
            _ARGUMENT_LEGENDS.create_vendor_token,
            False,
        )
        return objects.VendorToken(
            self.api(headers=headers, token=token, **query_args)["data"][
                "createVendorToken"
            ],
        )

    def login_vendor(
        self,
        input: inputs.LoginVendorInput,
        fields: List[
            fields_module.VendorTokenFields
        ] = fields_module.VendorTokenFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.VendorToken:
        query_args = self._query_builder(
            "mutation",
            "loginVendor",
            fields,
            {"input": input,},
            _ARGUMENT_LEGENDS.login_vendor,
            False,
        )
        return objects.VendorToken(
            self.api(headers=headers, token=token, **query_args)["data"]["loginVendor"],
        )

    def set_vendor_password(
        self,
        input: inputs.SetVendorPasswordInput,
        fields: List[
            fields_module.VendorTokenFields
        ] = fields_module.VendorTokenFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.VendorToken:
        query_args = self._query_builder(
            "mutation",
            "setVendorPassword",
            fields,
            {"input": input,},
            _ARGUMENT_LEGENDS.set_vendor_password,
            False,
        )
        return objects.VendorToken(
            self.api(headers=headers, token=token, **query_args)["data"][
                "setVendorPassword"
            ],
        )

    def delete_vendor_token(
        self,
        id: str,
        fields: List[
            fields_module.DeletionFields
        ] = fields_module.DeletionFields._default_fields(),
        headers: Union[dict, None] = None,
        token: Union[str, None] = None,
    ) -> objects.Deletion:
        query_args = self._query_builder(
            "mutation",
            "deleteVendorToken",
            fields,
            {"id": id,},
            _ARGUMENT_LEGENDS.delete_vendor_token,
            False,
        )
        return objects.Deletion(
            self.api(headers=headers, token=token, **query_args)["data"][
                "deleteVendorToken"
            ],
        )


__all__ = ['Cinnamon']
