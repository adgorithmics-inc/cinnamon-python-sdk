from functools import lru_cache
from .internals.base_classes import QueryFieldSet, QueryField

class _CampaignTemplateBase(QueryFieldSet):
    _sdk_default_field_names = [
        "id",
        "creation_date",
        "last_change_date",
        "name",
        "description",
        "platform",
        "remote_id",
        "system_status",
        "errors",
        "warnings",
        "kpi",
    ]
    id = QueryField("id")
    creation_date = QueryField("creationDate")
    last_change_date = QueryField("lastChangeDate")
    name = QueryField("name")
    description = QueryField("description")
    platform = QueryField("platform")
    remote_id = QueryField("remoteId")
    system_status = QueryField("systemStatus")
    errors = QueryField("errors")
    warnings = QueryField("warnings")
    kpi = QueryField("kpi")

    @property
    @lru_cache()
    def marketplace(self) -> "_MarketplaceBase":
        return self._sdk_embed(_MarketplaceBase, "marketplace.")

    @property
    @lru_cache()
    def marketing_campaigns(self) -> "_MarketingCampaignBase":
        return self._sdk_embed(_MarketingCampaignBase, "marketingCampaigns.edges.node.")

    @property
    @lru_cache()
    def gcpx_history(self) -> "_GCPXBase":
        return self._sdk_embed(_GCPXBase, "GCPXHistory.edges.node.")

    @property
    @lru_cache()
    def current_gcpx(self) -> "_GCPXBase":
        return self._sdk_embed(_GCPXBase, "currentGCPX.")


class _MarketplaceBase(QueryFieldSet):
    _sdk_default_field_names = [
        "id",
        "creation_date",
        "last_change_date",
        "name",
        "system_status",
        "errors",
        "warnings",
        "currency_code",
        "currency_symbol",
        "currency_offset",
    ]
    id = QueryField("id")
    creation_date = QueryField("creationDate")
    last_change_date = QueryField("lastChangeDate")
    name = QueryField("name")
    system_status = QueryField("systemStatus")
    errors = QueryField("errors")
    warnings = QueryField("warnings")
    currency_code = QueryField("currencyCode")
    currency_symbol = QueryField("currencySymbol")
    currency_offset = QueryField("currencyOffset")

    @property
    @lru_cache()
    def organization(self) -> "_OrganizationBase":
        return self._sdk_embed(_OrganizationBase, "organization.")

    @property
    @lru_cache()
    def media_channels(self) -> "_MediaChannelBase":
        return self._sdk_embed(_MediaChannelBase, "mediaChannels.edges.node.")

    @property
    @lru_cache()
    def campaign_templates(self) -> "_CampaignTemplateBase":
        return self._sdk_embed(_CampaignTemplateBase, "campaignTemplates.edges.node.")

    @property
    @lru_cache()
    def vendors(self) -> "_VendorBase":
        return self._sdk_embed(_VendorBase, "vendors.edges.node.")

    @property
    @lru_cache()
    def vendor_tokens(self) -> "_VendorTokenBase":
        return self._sdk_embed(_VendorTokenBase, "vendorTokens.edges.node.")

    @property
    @lru_cache()
    def creative_templates(self) -> "_CreativeTemplateBase":
        return self._sdk_embed(_CreativeTemplateBase, "creativeTemplates.edges.node.")

    @property
    @lru_cache()
    def products(self) -> "_ProductBase":
        return self._sdk_embed(_ProductBase, "products.edges.node.")


class _EntitlementResourceBase(QueryFieldSet):
    _sdk_default_field_names = [
        "id",
        "creation_date",
        "last_change_date",
        "name",
        "system_status",
        "errors",
        "warnings",
    ]
    id = QueryField("id")
    creation_date = QueryField("creationDate")
    last_change_date = QueryField("lastChangeDate")
    name = QueryField("name")
    system_status = QueryField("systemStatus")
    errors = QueryField("errors")
    warnings = QueryField("warnings")


class _OrganizationBase(QueryFieldSet):
    _sdk_default_field_names = [
        "id",
        "creation_date",
        "last_change_date",
        "name",
        "system_status",
        "errors",
        "warnings",
        "tier",
    ]
    id = QueryField("id")
    creation_date = QueryField("creationDate")
    last_change_date = QueryField("lastChangeDate")
    name = QueryField("name")
    system_status = QueryField("systemStatus")
    errors = QueryField("errors")
    warnings = QueryField("warnings")
    tier = QueryField("tier")

    @property
    @lru_cache()
    def users(self) -> "_UserBase":
        return self._sdk_embed(_UserBase, "users.edges.node.")

    @property
    @lru_cache()
    def marketplaces(self) -> "_MarketplaceBase":
        return self._sdk_embed(_MarketplaceBase, "marketplaces.edges.node.")


class _UserBase(QueryFieldSet):
    _sdk_default_field_names = [
        "id",
        "creation_date",
        "last_change_date",
        "email",
        "first_name",
        "last_name",
        "notice_opt_in",
        "newsletter_opt_in",
    ]
    id = QueryField("id")
    creation_date = QueryField("creationDate")
    last_change_date = QueryField("lastChangeDate")
    email = QueryField("email")
    first_name = QueryField("firstName")
    last_name = QueryField("lastName")

    @property
    @lru_cache()
    def organizations(self) -> "_OrganizationBase":
        return self._sdk_embed(_OrganizationBase, "organizations.edges.node.")

    @property
    @lru_cache()
    def entitlements(self) -> "_EntitlementBase":
        return self._sdk_embed(_EntitlementBase, "entitlements.edges.node.")

    notice_opt_in = QueryField("noticeOptIn")
    newsletter_opt_in = QueryField("newsletterOptIn")


class _MeBase(QueryFieldSet):
    _sdk_default_field_names = ["id", "creation_date", "last_change_date"]
    id = QueryField("id")
    creation_date = QueryField("creationDate")
    last_change_date = QueryField("lastChangeDate")


class _PageInfoBase(QueryFieldSet):
    _sdk_default_field_names = [
        "end_cursor",
        "start_cursor",
        "has_next_page",
        "has_previous_page",
    ]
    end_cursor = QueryField("endCursor")
    start_cursor = QueryField("startCursor")
    has_next_page = QueryField("hasNextPage")
    has_previous_page = QueryField("hasPreviousPage")


class _EntitlementBase(QueryFieldSet):
    _sdk_default_field_names = [
        "id",
        "creation_date",
        "last_change_date",
        "type",
        "permissions",
        "resource",
    ]
    id = QueryField("id")
    creation_date = QueryField("creationDate")
    last_change_date = QueryField("lastChangeDate")
    type = QueryField("type")
    permissions = QueryField("permissions")

    @property
    @lru_cache()
    def user(self) -> "_UserBase":
        return self._sdk_embed(_UserBase, "user.")

    resource = QueryField("resource")


class _MediaChannelBase(QueryFieldSet):
    _sdk_default_field_names = [
        "id",
        "creation_date",
        "last_change_date",
        "name",
        "system_status",
        "errors",
        "warnings",
        "platform",
        "remote_id",
        "remote_state",
        "currency_code",
        "currency_symbol",
        "currency_offset",
        "timezone",
        "token_status",
    ]
    id = QueryField("id")
    creation_date = QueryField("creationDate")
    last_change_date = QueryField("lastChangeDate")
    name = QueryField("name")
    system_status = QueryField("systemStatus")
    errors = QueryField("errors")
    warnings = QueryField("warnings")
    platform = QueryField("platform")
    remote_id = QueryField("remoteId")
    remote_state = QueryField("remoteState")
    currency_code = QueryField("currencyCode")
    currency_symbol = QueryField("currencySymbol")
    currency_offset = QueryField("currencyOffset")
    timezone = QueryField("timezone")
    token_status = QueryField("tokenStatus")

    @property
    @lru_cache()
    def catalogs(self) -> "_CatalogBase":
        return self._sdk_embed(_CatalogBase, "catalogs.edges.node.")

    @property
    @lru_cache()
    def marketplace(self) -> "_MarketplaceBase":
        return self._sdk_embed(_MarketplaceBase, "marketplace.")


class _CatalogBase(QueryFieldSet):
    _sdk_default_field_names = [
        "id",
        "creation_date",
        "last_change_date",
        "name",
        "catalog_type",
        "remote_id",
        "system_status",
        "remote_state",
        "data_feed_id",
        "external_event_source_ids",
        "product_source",
        "errors",
        "warnings",
    ]
    id = QueryField("id")
    creation_date = QueryField("creationDate")
    last_change_date = QueryField("lastChangeDate")
    name = QueryField("name")
    catalog_type = QueryField("catalogType")
    remote_id = QueryField("remoteId")
    system_status = QueryField("systemStatus")
    remote_state = QueryField("remoteState")
    data_feed_id = QueryField("dataFeedId")
    external_event_source_ids = QueryField("externalEventSourceIds")
    product_source = QueryField("productSource")
    errors = QueryField("errors")
    warnings = QueryField("warnings")

    @property
    @lru_cache()
    def media_channel(self) -> "_MediaChannelBase":
        return self._sdk_embed(_MediaChannelBase, "mediaChannel.")

    @property
    @lru_cache()
    def products(self) -> "_ProductBase":
        return self._sdk_embed(_ProductBase, "products.edges.node.")


class _ProductBase(QueryFieldSet):
    _sdk_default_field_names = [
        "id",
        "creation_date",
        "last_change_date",
        "results_source",
        "kpi",
        "system_status",
        "errors",
        "warnings",
        "name",
        "sku",
        "remote_state",
        "metadata",
        "imported",
    ]
    id = QueryField("id")
    creation_date = QueryField("creationDate")
    last_change_date = QueryField("lastChangeDate")
    results_source = QueryField("resultsSource")
    kpi = QueryField("kpi")

    @property
    @lru_cache()
    def vendor(self) -> "_VendorBase":
        return self._sdk_embed(_VendorBase, "vendor.")

    system_status = QueryField("systemStatus")
    errors = QueryField("errors")
    warnings = QueryField("warnings")
    name = QueryField("name")
    sku = QueryField("sku")
    remote_state = QueryField("remoteState")
    metadata = QueryField("metadata")
    imported = QueryField("imported")

    @property
    @lru_cache()
    def results(self) -> "_ResultBase":
        return self._sdk_embed(_ResultBase, "results.edges.node.")

    @property
    @lru_cache()
    def marketing_campaigns(self) -> "_MarketingCampaignBase":
        return self._sdk_embed(_MarketingCampaignBase, "marketingCampaigns.edges.node.")

    @property
    @lru_cache()
    def catalog(self) -> "_CatalogBase":
        return self._sdk_embed(_CatalogBase, "catalog.")


class _ResultResourceBase(QueryFieldSet):
    _sdk_default_field_names = [
        "id",
        "creation_date",
        "last_change_date",
        "results_source",
        "kpi",
        "system_status",
        "errors",
        "warnings",
    ]
    id = QueryField("id")
    creation_date = QueryField("creationDate")
    last_change_date = QueryField("lastChangeDate")
    results_source = QueryField("resultsSource")
    kpi = QueryField("kpi")

    @property
    @lru_cache()
    def vendor(self) -> "_VendorBase":
        return self._sdk_embed(_VendorBase, "vendor.")

    system_status = QueryField("systemStatus")
    errors = QueryField("errors")
    warnings = QueryField("warnings")


class _VendorBase(QueryFieldSet):
    _sdk_default_field_names = [
        "id",
        "creation_date",
        "last_change_date",
        "name",
        "system_status",
        "errors",
        "warnings",
    ]
    id = QueryField("id")
    creation_date = QueryField("creationDate")
    last_change_date = QueryField("lastChangeDate")
    name = QueryField("name")
    system_status = QueryField("systemStatus")
    errors = QueryField("errors")
    warnings = QueryField("warnings")

    @property
    @lru_cache()
    def marketplace(self) -> "_MarketplaceBase":
        return self._sdk_embed(_MarketplaceBase, "marketplace.")

    @property
    @lru_cache()
    def vendor_tokens(self) -> "_VendorTokenBase":
        return self._sdk_embed(_VendorTokenBase, "vendorTokens.edges.node.")

    @property
    @lru_cache()
    def products(self) -> "_ProductBase":
        return self._sdk_embed(_ProductBase, "products.edges.node.")


class _VendorTokenBase(QueryFieldSet):
    _sdk_default_field_names = [
        "id",
        "creation_date",
        "last_change_date",
        "token",
        "email",
    ]
    id = QueryField("id")
    creation_date = QueryField("creationDate")
    last_change_date = QueryField("lastChangeDate")
    token = QueryField("token")

    @property
    @lru_cache()
    def vendor(self) -> "_VendorBase":
        return self._sdk_embed(_VendorBase, "vendor.")

    @property
    @lru_cache()
    def marketplace(self) -> "_MarketplaceBase":
        return self._sdk_embed(_MarketplaceBase, "marketplace.")

    email = QueryField("email")


class _ResultBase(QueryFieldSet):
    _sdk_default_field_names = [
        "id",
        "creation_date",
        "last_change_date",
        "date",
        "type",
        "breakdown_type",
        "resource",
        "breakdown",
    ]
    id = QueryField("id")
    creation_date = QueryField("creationDate")
    last_change_date = QueryField("lastChangeDate")
    date = QueryField("date")

    @property
    @lru_cache()
    def analytics(self) -> "_ResultAnalyticsBase":
        return self._sdk_embed(_ResultAnalyticsBase, "analytics.")

    type = QueryField("type")
    breakdown_type = QueryField("breakdownType")
    resource = QueryField("resource")
    breakdown = QueryField("breakdown")

    @property
    @lru_cache()
    def vendor(self) -> "_VendorBase":
        return self._sdk_embed(_VendorBase, "vendor.")


class _ResultAnalyticsBase(QueryFieldSet):
    _sdk_default_field_names = [
        "results",
        "impressions",
        "clicks",
        "spend",
        "purchases",
        "purchases_value",
    ]
    results = QueryField("results")
    impressions = QueryField("impressions")
    clicks = QueryField("clicks")
    spend = QueryField("spend")
    purchases = QueryField("purchases")
    purchases_value = QueryField("purchasesValue")


class _MarketingCampaignBase(QueryFieldSet):
    _sdk_default_field_names = [
        "id",
        "creation_date",
        "last_change_date",
        "results_source",
        "kpi",
        "system_status",
        "errors",
        "warnings",
        "name",
        "status",
        "creative_spec",
        "run_time_spec",
        "location_spec",
        "conversion_spec",
        "start_date",
        "end_date",
        "delivering",
    ]
    id = QueryField("id")
    creation_date = QueryField("creationDate")
    last_change_date = QueryField("lastChangeDate")
    results_source = QueryField("resultsSource")
    kpi = QueryField("kpi")

    @property
    @lru_cache()
    def vendor(self) -> "_VendorBase":
        return self._sdk_embed(_VendorBase, "vendor.")

    system_status = QueryField("systemStatus")
    errors = QueryField("errors")
    warnings = QueryField("warnings")
    name = QueryField("name")
    status = QueryField("status")
    creative_spec = QueryField("creativeSpec")
    run_time_spec = QueryField("runTimeSpec")
    location_spec = QueryField("locationSpec")
    conversion_spec = QueryField("conversionSpec")
    start_date = QueryField("startDate")
    end_date = QueryField("endDate")

    @property
    @lru_cache()
    def gcpx(self) -> "_GCPXBase":
        return self._sdk_embed(_GCPXBase, "GCPX.")

    delivering = QueryField("delivering")

    @property
    @lru_cache()
    def marketing_ads(self) -> "_MarketingAdBase":
        return self._sdk_embed(_MarketingAdBase, "marketingAds.edges.node.")

    @property
    @lru_cache()
    def products(self) -> "_ProductBase":
        return self._sdk_embed(_ProductBase, "products.edges.node.")

    @property
    @lru_cache()
    def catalog(self) -> "_CatalogBase":
        return self._sdk_embed(_CatalogBase, "catalog.")

    @property
    @lru_cache()
    def campaign_template(self) -> "_CampaignTemplateBase":
        return self._sdk_embed(_CampaignTemplateBase, "campaignTemplate.")

    @property
    @lru_cache()
    def media_channel(self) -> "_MediaChannelBase":
        return self._sdk_embed(_MediaChannelBase, "mediaChannel.")

    @property
    @lru_cache()
    def results(self) -> "_ResultBase":
        return self._sdk_embed(_ResultBase, "results.edges.node.")

    @property
    @lru_cache()
    def notifications(self) -> "_NotificationBase":
        return self._sdk_embed(_NotificationBase, "notifications.edges.node.")


class _NotificationResourceBase(QueryFieldSet):
    _sdk_default_field_names = [
        "id",
        "creation_date",
        "last_change_date",
        "system_status",
        "errors",
        "warnings",
    ]
    id = QueryField("id")
    creation_date = QueryField("creationDate")
    last_change_date = QueryField("lastChangeDate")
    system_status = QueryField("systemStatus")
    errors = QueryField("errors")
    warnings = QueryField("warnings")


class _GCPXBase(QueryFieldSet):
    _sdk_default_field_names = [
        "id",
        "creation_date",
        "last_change_date",
        "kpi",
        "price",
        "start_date",
        "end_date",
        "min_conversions",
        "max_conversions",
    ]
    id = QueryField("id")
    creation_date = QueryField("creationDate")
    last_change_date = QueryField("lastChangeDate")
    kpi = QueryField("kpi")
    price = QueryField("price")
    start_date = QueryField("startDate")
    end_date = QueryField("endDate")
    min_conversions = QueryField("minConversions")
    max_conversions = QueryField("maxConversions")

    @property
    @lru_cache()
    def campaign_template(self) -> "_CampaignTemplateBase":
        return self._sdk_embed(_CampaignTemplateBase, "campaignTemplate.")

    @property
    @lru_cache()
    def marketplace(self) -> "_MarketplaceBase":
        return self._sdk_embed(_MarketplaceBase, "marketplace.")

    @property
    @lru_cache()
    def marketing_campaigns(self) -> "_MarketingCampaignBase":
        return self._sdk_embed(_MarketingCampaignBase, "marketingCampaigns.edges.node.")


class _MarketingAdBase(QueryFieldSet):
    _sdk_default_field_names = [
        "id",
        "creation_date",
        "last_change_date",
        "results_source",
        "kpi",
        "system_status",
        "errors",
        "warnings",
        "remote_id",
    ]
    id = QueryField("id")
    creation_date = QueryField("creationDate")
    last_change_date = QueryField("lastChangeDate")
    results_source = QueryField("resultsSource")
    kpi = QueryField("kpi")

    @property
    @lru_cache()
    def vendor(self) -> "_VendorBase":
        return self._sdk_embed(_VendorBase, "vendor.")

    system_status = QueryField("systemStatus")
    errors = QueryField("errors")
    warnings = QueryField("warnings")
    remote_id = QueryField("remoteId")

    @property
    @lru_cache()
    def ad_previews(self) -> "_AdPreviewBase":
        return self._sdk_embed(_AdPreviewBase, "adPreviews.")

    @property
    @lru_cache()
    def results(self) -> "_ResultBase":
        return self._sdk_embed(_ResultBase, "results.edges.node.")

    @property
    @lru_cache()
    def marketing_campaign(self) -> "_MarketingCampaignBase":
        return self._sdk_embed(_MarketingCampaignBase, "marketingCampaign.")


class _AdPreviewBase(QueryFieldSet):
    _sdk_default_field_names = ["url", "dimensions", "placement"]
    url = QueryField("url")
    dimensions = QueryField("dimensions")
    placement = QueryField("placement")


class _NotificationBase(QueryFieldSet):
    _sdk_default_field_names = [
        "id",
        "creation_date",
        "last_change_date",
        "title",
        "message",
        "status",
        "severity",
        "code",
        "source",
        "resource",
    ]
    id = QueryField("id")
    creation_date = QueryField("creationDate")
    last_change_date = QueryField("lastChangeDate")
    title = QueryField("title")
    message = QueryField("message")
    status = QueryField("status")
    severity = QueryField("severity")
    code = QueryField("code")
    source = QueryField("source")
    resource = QueryField("resource")


class _CreativeTemplateBase(QueryFieldSet):
    _sdk_default_field_names = [
        "id",
        "creation_date",
        "last_change_date",
        "name",
        "height",
        "width",
        "system_status",
        "errors",
        "warnings",
    ]
    id = QueryField("id")
    creation_date = QueryField("creationDate")
    last_change_date = QueryField("lastChangeDate")
    name = QueryField("name")
    height = QueryField("height")
    width = QueryField("width")
    system_status = QueryField("systemStatus")
    errors = QueryField("errors")
    warnings = QueryField("warnings")

    @property
    @lru_cache()
    def marketplace(self) -> "_MarketplaceBase":
        return self._sdk_embed(_MarketplaceBase, "marketplace.")

    @property
    @lru_cache()
    def marketing_campaigns(self) -> "_MarketingCampaignBase":
        return self._sdk_embed(_MarketingCampaignBase, "marketingCampaigns.edges.node.")

    @property
    @lru_cache()
    def creative_layers(self) -> "_CreativeLayerBase":
        return self._sdk_embed(_CreativeLayerBase, "creativeLayers.edges.node.")


class _CreativeLayerBase(QueryFieldSet):
    _sdk_default_field_names = [
        "id",
        "creation_date",
        "last_change_date",
        "name",
        "height",
        "width",
        "x",
        "y",
        "order",
        "type",
        "properties",
        "system_status",
        "errors",
        "warnings",
    ]
    id = QueryField("id")
    creation_date = QueryField("creationDate")
    last_change_date = QueryField("lastChangeDate")
    name = QueryField("name")
    height = QueryField("height")
    width = QueryField("width")
    x = QueryField("x")
    y = QueryField("y")
    order = QueryField("order")
    type = QueryField("type")
    properties = QueryField("properties")
    system_status = QueryField("systemStatus")
    errors = QueryField("errors")
    warnings = QueryField("warnings")

    @property
    @lru_cache()
    def creative_template(self) -> "_CreativeTemplateBase":
        return self._sdk_embed(_CreativeTemplateBase, "creativeTemplate.")


class _CreativeFontBase(QueryFieldSet):
    _sdk_default_field_names = [
        "id",
        "creation_date",
        "last_change_date",
        "name",
        "url",
        "properties",
        "system_status",
        "errors",
        "warnings",
    ]
    id = QueryField("id")
    creation_date = QueryField("creationDate")
    last_change_date = QueryField("lastChangeDate")
    name = QueryField("name")
    url = QueryField("url")
    properties = QueryField("properties")
    system_status = QueryField("systemStatus")
    errors = QueryField("errors")
    warnings = QueryField("warnings")

    @property
    @lru_cache()
    def marketplace(self) -> "_MarketplaceBase":
        return self._sdk_embed(_MarketplaceBase, "marketplace.")


class _CreativeImageBase(QueryFieldSet):
    _sdk_default_field_names = [
        "id",
        "creation_date",
        "last_change_date",
        "name",
        "url",
        "properties",
        "system_status",
        "errors",
        "warnings",
    ]
    id = QueryField("id")
    creation_date = QueryField("creationDate")
    last_change_date = QueryField("lastChangeDate")
    name = QueryField("name")
    url = QueryField("url")
    properties = QueryField("properties")
    system_status = QueryField("systemStatus")
    errors = QueryField("errors")
    warnings = QueryField("warnings")

    @property
    @lru_cache()
    def marketplace(self) -> "_MarketplaceBase":
        return self._sdk_embed(_MarketplaceBase, "marketplace.")


class _TokenBase(QueryFieldSet):
    _sdk_default_field_names = ["token", "refresh_token", "expiry_date"]
    token = QueryField("token")
    refresh_token = QueryField("refreshToken")
    expiry_date = QueryField("expiryDate")

    @property
    @lru_cache()
    def user(self) -> "_UserBase":
        return self._sdk_embed(_UserBase, "user.")


class _DeletionBase(QueryFieldSet):
    _sdk_default_field_names = ["id"]
    id = QueryField("id")


class _RequestResultBase(QueryFieldSet):
    _sdk_default_field_names = ["result"]
    result = QueryField("result")


class _MarketingCampaignSnapshotBase(QueryFieldSet):
    _sdk_default_field_names = [
        "id",
        "creation_date",
        "last_change_date",
        "successful",
        "name",
        "status",
        "creative_spec",
        "run_time_spec",
        "location_spec",
        "kpi",
        "product_ids",
    ]
    id = QueryField("id")
    creation_date = QueryField("creationDate")
    last_change_date = QueryField("lastChangeDate")

    @property
    @lru_cache()
    def marketing_campaign(self) -> "_MarketingCampaignBase":
        return self._sdk_embed(_MarketingCampaignBase, "marketingCampaign.")

    successful = QueryField("successful")
    name = QueryField("name")
    status = QueryField("status")
    creative_spec = QueryField("creativeSpec")
    run_time_spec = QueryField("runTimeSpec")
    location_spec = QueryField("locationSpec")
    kpi = QueryField("kpi")
    product_ids = QueryField("productIds")


class _SingleUseTokenBase(QueryFieldSet):
    _sdk_default_field_names = ["id", "creation_date", "last_change_date", "token"]
    id = QueryField("id")
    creation_date = QueryField("creationDate")
    last_change_date = QueryField("lastChangeDate")
    token = QueryField("token")

    @property
    @lru_cache()
    def user(self) -> "_UserBase":
        return self._sdk_embed(_UserBase, "user.")


CampaignTemplateFields = _CampaignTemplateBase()
MarketplaceFields = _MarketplaceBase()
EntitlementResourceFields = _EntitlementResourceBase()
OrganizationFields = _OrganizationBase()
UserFields = _UserBase()
MeFields = _MeBase()
PageInfoFields = _PageInfoBase()
EntitlementFields = _EntitlementBase()
MediaChannelFields = _MediaChannelBase()
CatalogFields = _CatalogBase()
ProductFields = _ProductBase()
ResultResourceFields = _ResultResourceBase()
VendorFields = _VendorBase()
VendorTokenFields = _VendorTokenBase()
ResultFields = _ResultBase()
ResultAnalyticsFields = _ResultAnalyticsBase()
MarketingCampaignFields = _MarketingCampaignBase()
NotificationResourceFields = _NotificationResourceBase()
GCPXFields = _GCPXBase()
MarketingAdFields = _MarketingAdBase()
AdPreviewFields = _AdPreviewBase()
NotificationFields = _NotificationBase()
CreativeTemplateFields = _CreativeTemplateBase()
CreativeLayerFields = _CreativeLayerBase()
CreativeFontFields = _CreativeFontBase()
CreativeImageFields = _CreativeImageBase()
TokenFields = _TokenBase()
DeletionFields = _DeletionBase()
RequestResultFields = _RequestResultBase()
MarketingCampaignSnapshotFields = _MarketingCampaignSnapshotBase()
SingleUseTokenFields = _SingleUseTokenBase()
UserConnectionFields = _UserBase("edges.node.")
OrganizationConnectionFields = _OrganizationBase("edges.node.")
EntitlementConnectionFields = _EntitlementBase("edges.node.")
MarketplaceConnectionFields = _MarketplaceBase("edges.node.")
MediaChannelConnectionFields = _MediaChannelBase("edges.node.")
CatalogConnectionFields = _CatalogBase("edges.node.")
ProductConnectionFields = _ProductBase("edges.node.")
VendorTokenConnectionFields = _VendorTokenBase("edges.node.")
ResultConnectionFields = _ResultBase("edges.node.")
MarketingCampaignConnectionFields = _MarketingCampaignBase("edges.node.")
MarketingAdConnectionFields = _MarketingAdBase("edges.node.")
NotificationConnectionFields = _NotificationBase("edges.node.")
CampaignTemplateConnectionFields = _CampaignTemplateBase("edges.node.")
VendorConnectionFields = _VendorBase("edges.node.")
CreativeTemplateConnectionFields = _CreativeTemplateBase("edges.node.")
CreativeLayerConnectionFields = _CreativeLayerBase("edges.node.")
GCPXConnectionFields = _GCPXBase("edges.node.")
CreativeFontConnectionFields = _CreativeFontBase("edges.node.")
CreativeImageConnectionFields = _CreativeImageBase("edges.node.")
MarketingCampaignSnapshotConnectionFields = _MarketingCampaignSnapshotBase(
    "edges.node."
)
SingleUseTokenConnectionFields = _SingleUseTokenBase("edges.node.")
__all__ = [
    "CampaignTemplateFields",
    "MarketplaceFields",
    "EntitlementResourceFields",
    "OrganizationFields",
    "UserConnectionFields",
    "UserFields",
    "MeFields",
    "OrganizationConnectionFields",
    "PageInfoFields",
    "EntitlementConnectionFields",
    "EntitlementFields",
    "MarketplaceConnectionFields",
    "MediaChannelConnectionFields",
    "MediaChannelFields",
    "CatalogConnectionFields",
    "CatalogFields",
    "ProductConnectionFields",
    "ProductFields",
    "ResultResourceFields",
    "VendorFields",
    "VendorTokenConnectionFields",
    "VendorTokenFields",
    "ResultConnectionFields",
    "ResultFields",
    "ResultAnalyticsFields",
    "MarketingCampaignConnectionFields",
    "MarketingCampaignFields",
    "NotificationResourceFields",
    "GCPXFields",
    "MarketingAdConnectionFields",
    "MarketingAdFields",
    "AdPreviewFields",
    "NotificationConnectionFields",
    "NotificationFields",
    "CampaignTemplateConnectionFields",
    "VendorConnectionFields",
    "CreativeTemplateConnectionFields",
    "CreativeTemplateFields",
    "CreativeLayerConnectionFields",
    "CreativeLayerFields",
    "GCPXConnectionFields",
    "CreativeFontFields",
    "CreativeFontConnectionFields",
    "CreativeImageFields",
    "CreativeImageConnectionFields",
    "TokenFields",
    "DeletionFields",
    "RequestResultFields",
    "MarketingCampaignSnapshotFields",
    "MarketingCampaignSnapshotConnectionFields",
    "SingleUseTokenFields",
    "SingleUseTokenConnectionFields",
]
