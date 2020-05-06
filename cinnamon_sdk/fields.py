from functools import lru_cache
from .internals.base_classes import QueryFieldSet, QueryField


class _CampaignTemplateBase(QueryFieldSet):
    _sdk_default_fields = [
        QueryField("id"),
        QueryField("creationDate"),
        QueryField("lastChangeDate"),
        QueryField("name"),
        QueryField("description"),
        QueryField("platform"),
        QueryField("remoteId"),
        QueryField("systemStatus"),
        QueryField("errors"),
        QueryField("warnings"),
        QueryField("kpi"),
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
    def marketing_campaigns(self) -> "_MarketingCampaignConnectionBase":
        return self._sdk_embed(_MarketingCampaignConnectionBase, "marketingCampaigns.")

    @property
    @lru_cache()
    def gcpx_history(self) -> "_GCPXConnectionBase":
        return self._sdk_embed(_GCPXConnectionBase, "GCPXHistory.")

    @property
    @lru_cache()
    def current_gcpx(self) -> "_GCPXBase":
        return self._sdk_embed(_GCPXBase, "currentGCPX.")


class _MarketplaceBase(QueryFieldSet):
    _sdk_default_fields = [
        QueryField("id"),
        QueryField("creationDate"),
        QueryField("lastChangeDate"),
        QueryField("name"),
        QueryField("systemStatus"),
        QueryField("errors"),
        QueryField("warnings"),
        QueryField("currencyCode"),
        QueryField("currencySymbol"),
        QueryField("currencyOffset"),
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
    def media_channels(self) -> "_MediaChannelConnectionBase":
        return self._sdk_embed(_MediaChannelConnectionBase, "mediaChannels.")

    @property
    @lru_cache()
    def campaign_templates(self) -> "_CampaignTemplateConnectionBase":
        return self._sdk_embed(_CampaignTemplateConnectionBase, "campaignTemplates.")

    @property
    @lru_cache()
    def vendors(self) -> "_VendorConnectionBase":
        return self._sdk_embed(_VendorConnectionBase, "vendors.")

    @property
    @lru_cache()
    def vendor_tokens(self) -> "_VendorTokenConnectionBase":
        return self._sdk_embed(_VendorTokenConnectionBase, "vendorTokens.")

    @property
    @lru_cache()
    def creative_templates(self) -> "_CreativeTemplateConnectionBase":
        return self._sdk_embed(_CreativeTemplateConnectionBase, "creativeTemplates.")

    @property
    @lru_cache()
    def products(self) -> "_ProductConnectionBase":
        return self._sdk_embed(_ProductConnectionBase, "products.")


class _EntitlementResourceBase(QueryFieldSet):
    _sdk_default_fields = [
        QueryField("id"),
        QueryField("creationDate"),
        QueryField("lastChangeDate"),
        QueryField("name"),
        QueryField("systemStatus"),
        QueryField("errors"),
        QueryField("warnings"),
    ]
    id = QueryField("id")
    creation_date = QueryField("creationDate")
    last_change_date = QueryField("lastChangeDate")
    name = QueryField("name")
    system_status = QueryField("systemStatus")
    errors = QueryField("errors")
    warnings = QueryField("warnings")


class _OrganizationBase(QueryFieldSet):
    _sdk_default_fields = [
        QueryField("id"),
        QueryField("creationDate"),
        QueryField("lastChangeDate"),
        QueryField("name"),
        QueryField("systemStatus"),
        QueryField("errors"),
        QueryField("warnings"),
        QueryField("tier"),
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
    def users(self) -> "_UserConnectionBase":
        return self._sdk_embed(_UserConnectionBase, "users.")

    @property
    @lru_cache()
    def marketplaces(self) -> "_MarketplaceConnectionBase":
        return self._sdk_embed(_MarketplaceConnectionBase, "marketplaces.")


class _UserConnectionBase(QueryFieldSet):
    _sdk_default_fields = [
        QueryField("id", "edges.node."),
        QueryField("creationDate", "edges.node."),
        QueryField("lastChangeDate", "edges.node."),
        QueryField("email", "edges.node."),
        QueryField("firstName", "edges.node."),
        QueryField("lastName", "edges.node."),
        QueryField("noticeOptIn", "edges.node."),
        QueryField("newsletterOptIn", "edges.node."),
        QueryField("totalCount"),
    ]

    @property
    @lru_cache()
    def edges(self) -> "_UserEdgeBase":
        return self._sdk_embed(_UserEdgeBase, "edges.")

    @property
    @lru_cache()
    def page_info(self) -> "_PageInfoBase":
        return self._sdk_embed(_PageInfoBase, "pageInfo.")

    total_count = QueryField("totalCount")


class _UserEdgeBase(QueryFieldSet):
    _sdk_default_fields = [QueryField("cursor")]

    @property
    @lru_cache()
    def node(self) -> "_UserBase":
        return self._sdk_embed(_UserBase, "node.")

    cursor = QueryField("cursor")


class _UserBase(QueryFieldSet):
    _sdk_default_fields = [
        QueryField("id"),
        QueryField("creationDate"),
        QueryField("lastChangeDate"),
        QueryField("email"),
        QueryField("firstName"),
        QueryField("lastName"),
        QueryField("noticeOptIn"),
        QueryField("newsletterOptIn"),
    ]
    id = QueryField("id")
    creation_date = QueryField("creationDate")
    last_change_date = QueryField("lastChangeDate")
    email = QueryField("email")
    first_name = QueryField("firstName")
    last_name = QueryField("lastName")

    @property
    @lru_cache()
    def organizations(self) -> "_OrganizationConnectionBase":
        return self._sdk_embed(_OrganizationConnectionBase, "organizations.")

    @property
    @lru_cache()
    def entitlements(self) -> "_EntitlementConnectionBase":
        return self._sdk_embed(_EntitlementConnectionBase, "entitlements.")

    notice_opt_in = QueryField("noticeOptIn")
    newsletter_opt_in = QueryField("newsletterOptIn")


class _MeBase(QueryFieldSet):
    _sdk_default_fields = [
        QueryField("id"),
        QueryField("creationDate"),
        QueryField("lastChangeDate"),
    ]
    id = QueryField("id")
    creation_date = QueryField("creationDate")
    last_change_date = QueryField("lastChangeDate")


class _OrganizationConnectionBase(QueryFieldSet):
    _sdk_default_fields = [
        QueryField("id", "edges.node."),
        QueryField("creationDate", "edges.node."),
        QueryField("lastChangeDate", "edges.node."),
        QueryField("name", "edges.node."),
        QueryField("systemStatus", "edges.node."),
        QueryField("errors", "edges.node."),
        QueryField("warnings", "edges.node."),
        QueryField("tier", "edges.node."),
        QueryField("totalCount"),
    ]

    @property
    @lru_cache()
    def edges(self) -> "_OrganizationEdgeBase":
        return self._sdk_embed(_OrganizationEdgeBase, "edges.")

    @property
    @lru_cache()
    def page_info(self) -> "_PageInfoBase":
        return self._sdk_embed(_PageInfoBase, "pageInfo.")

    total_count = QueryField("totalCount")


class _OrganizationEdgeBase(QueryFieldSet):
    _sdk_default_fields = [QueryField("cursor")]

    @property
    @lru_cache()
    def node(self) -> "_OrganizationBase":
        return self._sdk_embed(_OrganizationBase, "node.")

    cursor = QueryField("cursor")


class _PageInfoBase(QueryFieldSet):
    _sdk_default_fields = [
        QueryField("endCursor"),
        QueryField("startCursor"),
        QueryField("hasNextPage"),
        QueryField("hasPreviousPage"),
    ]
    end_cursor = QueryField("endCursor")
    start_cursor = QueryField("startCursor")
    has_next_page = QueryField("hasNextPage")
    has_previous_page = QueryField("hasPreviousPage")


class _EntitlementConnectionBase(QueryFieldSet):
    _sdk_default_fields = [
        QueryField("id", "edges.node."),
        QueryField("creationDate", "edges.node."),
        QueryField("lastChangeDate", "edges.node."),
        QueryField("type", "edges.node."),
        QueryField("permissions", "edges.node."),
        QueryField("resource", "edges.node."),
        QueryField("totalCount"),
    ]

    @property
    @lru_cache()
    def edges(self) -> "_EntitlementEdgeBase":
        return self._sdk_embed(_EntitlementEdgeBase, "edges.")

    @property
    @lru_cache()
    def page_info(self) -> "_PageInfoBase":
        return self._sdk_embed(_PageInfoBase, "pageInfo.")

    total_count = QueryField("totalCount")


class _EntitlementEdgeBase(QueryFieldSet):
    _sdk_default_fields = [QueryField("cursor")]

    @property
    @lru_cache()
    def node(self) -> "_EntitlementBase":
        return self._sdk_embed(_EntitlementBase, "node.")

    cursor = QueryField("cursor")


class _EntitlementBase(QueryFieldSet):
    _sdk_default_fields = [
        QueryField("id"),
        QueryField("creationDate"),
        QueryField("lastChangeDate"),
        QueryField("type"),
        QueryField("permissions"),
        QueryField("resource"),
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


class _MarketplaceConnectionBase(QueryFieldSet):
    _sdk_default_fields = [
        QueryField("id", "edges.node."),
        QueryField("creationDate", "edges.node."),
        QueryField("lastChangeDate", "edges.node."),
        QueryField("name", "edges.node."),
        QueryField("systemStatus", "edges.node."),
        QueryField("errors", "edges.node."),
        QueryField("warnings", "edges.node."),
        QueryField("currencyCode", "edges.node."),
        QueryField("currencySymbol", "edges.node."),
        QueryField("currencyOffset", "edges.node."),
        QueryField("totalCount"),
    ]

    @property
    @lru_cache()
    def edges(self) -> "_MarketplaceEdgeBase":
        return self._sdk_embed(_MarketplaceEdgeBase, "edges.")

    @property
    @lru_cache()
    def page_info(self) -> "_PageInfoBase":
        return self._sdk_embed(_PageInfoBase, "pageInfo.")

    total_count = QueryField("totalCount")


class _MarketplaceEdgeBase(QueryFieldSet):
    _sdk_default_fields = [QueryField("cursor")]

    @property
    @lru_cache()
    def node(self) -> "_MarketplaceBase":
        return self._sdk_embed(_MarketplaceBase, "node.")

    cursor = QueryField("cursor")


class _MediaChannelConnectionBase(QueryFieldSet):
    _sdk_default_fields = [
        QueryField("id", "edges.node."),
        QueryField("creationDate", "edges.node."),
        QueryField("lastChangeDate", "edges.node."),
        QueryField("name", "edges.node."),
        QueryField("systemStatus", "edges.node."),
        QueryField("errors", "edges.node."),
        QueryField("warnings", "edges.node."),
        QueryField("platform", "edges.node."),
        QueryField("remoteId", "edges.node."),
        QueryField("remoteState", "edges.node."),
        QueryField("currencyCode", "edges.node."),
        QueryField("currencySymbol", "edges.node."),
        QueryField("currencyOffset", "edges.node."),
        QueryField("timezone", "edges.node."),
        QueryField("tokenStatus", "edges.node."),
        QueryField("totalCount"),
    ]

    @property
    @lru_cache()
    def edges(self) -> "_MediaChannelEdgeBase":
        return self._sdk_embed(_MediaChannelEdgeBase, "edges.")

    @property
    @lru_cache()
    def page_info(self) -> "_PageInfoBase":
        return self._sdk_embed(_PageInfoBase, "pageInfo.")

    total_count = QueryField("totalCount")


class _MediaChannelEdgeBase(QueryFieldSet):
    _sdk_default_fields = [QueryField("cursor")]

    @property
    @lru_cache()
    def node(self) -> "_MediaChannelBase":
        return self._sdk_embed(_MediaChannelBase, "node.")

    cursor = QueryField("cursor")


class _MediaChannelBase(QueryFieldSet):
    _sdk_default_fields = [
        QueryField("id"),
        QueryField("creationDate"),
        QueryField("lastChangeDate"),
        QueryField("name"),
        QueryField("systemStatus"),
        QueryField("errors"),
        QueryField("warnings"),
        QueryField("platform"),
        QueryField("remoteId"),
        QueryField("remoteState"),
        QueryField("currencyCode"),
        QueryField("currencySymbol"),
        QueryField("currencyOffset"),
        QueryField("timezone"),
        QueryField("tokenStatus"),
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
    def catalogs(self) -> "_CatalogConnectionBase":
        return self._sdk_embed(_CatalogConnectionBase, "catalogs.")

    @property
    @lru_cache()
    def marketplace(self) -> "_MarketplaceBase":
        return self._sdk_embed(_MarketplaceBase, "marketplace.")


class _CatalogConnectionBase(QueryFieldSet):
    _sdk_default_fields = [
        QueryField("id", "edges.node."),
        QueryField("creationDate", "edges.node."),
        QueryField("lastChangeDate", "edges.node."),
        QueryField("name", "edges.node."),
        QueryField("catalogType", "edges.node."),
        QueryField("remoteId", "edges.node."),
        QueryField("systemStatus", "edges.node."),
        QueryField("remoteState", "edges.node."),
        QueryField("dataFeedId", "edges.node."),
        QueryField("externalEventSourceIds", "edges.node."),
        QueryField("productSource", "edges.node."),
        QueryField("errors", "edges.node."),
        QueryField("warnings", "edges.node."),
        QueryField("totalCount"),
    ]

    @property
    @lru_cache()
    def edges(self) -> "_CatalogEdgeBase":
        return self._sdk_embed(_CatalogEdgeBase, "edges.")

    @property
    @lru_cache()
    def page_info(self) -> "_PageInfoBase":
        return self._sdk_embed(_PageInfoBase, "pageInfo.")

    total_count = QueryField("totalCount")


class _CatalogEdgeBase(QueryFieldSet):
    _sdk_default_fields = [QueryField("cursor")]

    @property
    @lru_cache()
    def node(self) -> "_CatalogBase":
        return self._sdk_embed(_CatalogBase, "node.")

    cursor = QueryField("cursor")


class _CatalogBase(QueryFieldSet):
    _sdk_default_fields = [
        QueryField("id"),
        QueryField("creationDate"),
        QueryField("lastChangeDate"),
        QueryField("name"),
        QueryField("catalogType"),
        QueryField("remoteId"),
        QueryField("systemStatus"),
        QueryField("remoteState"),
        QueryField("dataFeedId"),
        QueryField("externalEventSourceIds"),
        QueryField("productSource"),
        QueryField("errors"),
        QueryField("warnings"),
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
    def products(self) -> "_ProductConnectionBase":
        return self._sdk_embed(_ProductConnectionBase, "products.")


class _ProductConnectionBase(QueryFieldSet):
    _sdk_default_fields = [
        QueryField("id", "edges.node."),
        QueryField("creationDate", "edges.node."),
        QueryField("lastChangeDate", "edges.node."),
        QueryField("resultsSource", "edges.node."),
        QueryField("kpi", "edges.node."),
        QueryField("systemStatus", "edges.node."),
        QueryField("errors", "edges.node."),
        QueryField("warnings", "edges.node."),
        QueryField("name", "edges.node."),
        QueryField("sku", "edges.node."),
        QueryField("remoteState", "edges.node."),
        QueryField("metadata", "edges.node."),
        QueryField("imported", "edges.node."),
        QueryField("totalCount"),
    ]

    @property
    @lru_cache()
    def edges(self) -> "_ProductEdgeBase":
        return self._sdk_embed(_ProductEdgeBase, "edges.")

    @property
    @lru_cache()
    def page_info(self) -> "_PageInfoBase":
        return self._sdk_embed(_PageInfoBase, "pageInfo.")

    total_count = QueryField("totalCount")


class _ProductEdgeBase(QueryFieldSet):
    _sdk_default_fields = [QueryField("cursor")]

    @property
    @lru_cache()
    def node(self) -> "_ProductBase":
        return self._sdk_embed(_ProductBase, "node.")

    cursor = QueryField("cursor")


class _ProductBase(QueryFieldSet):
    _sdk_default_fields = [
        QueryField("id"),
        QueryField("creationDate"),
        QueryField("lastChangeDate"),
        QueryField("resultsSource"),
        QueryField("kpi"),
        QueryField("systemStatus"),
        QueryField("errors"),
        QueryField("warnings"),
        QueryField("name"),
        QueryField("sku"),
        QueryField("remoteState"),
        QueryField("metadata"),
        QueryField("imported"),
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
    def results(self) -> "_ResultConnectionBase":
        return self._sdk_embed(_ResultConnectionBase, "results.")

    @property
    @lru_cache()
    def marketing_campaigns(self) -> "_MarketingCampaignConnectionBase":
        return self._sdk_embed(_MarketingCampaignConnectionBase, "marketingCampaigns.")

    @property
    @lru_cache()
    def catalog(self) -> "_CatalogBase":
        return self._sdk_embed(_CatalogBase, "catalog.")


class _ResultResourceBase(QueryFieldSet):
    _sdk_default_fields = [
        QueryField("id"),
        QueryField("creationDate"),
        QueryField("lastChangeDate"),
        QueryField("resultsSource"),
        QueryField("kpi"),
        QueryField("systemStatus"),
        QueryField("errors"),
        QueryField("warnings"),
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
    _sdk_default_fields = [
        QueryField("id"),
        QueryField("creationDate"),
        QueryField("lastChangeDate"),
        QueryField("name"),
        QueryField("systemStatus"),
        QueryField("errors"),
        QueryField("warnings"),
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
    def vendor_tokens(self) -> "_VendorTokenConnectionBase":
        return self._sdk_embed(_VendorTokenConnectionBase, "vendorTokens.")

    @property
    @lru_cache()
    def products(self) -> "_ProductConnectionBase":
        return self._sdk_embed(_ProductConnectionBase, "products.")


class _VendorTokenConnectionBase(QueryFieldSet):
    _sdk_default_fields = [
        QueryField("id", "edges.node."),
        QueryField("creationDate", "edges.node."),
        QueryField("lastChangeDate", "edges.node."),
        QueryField("token", "edges.node."),
        QueryField("email", "edges.node."),
        QueryField("totalCount"),
    ]

    @property
    @lru_cache()
    def edges(self) -> "_VendorTokenEdgeBase":
        return self._sdk_embed(_VendorTokenEdgeBase, "edges.")

    @property
    @lru_cache()
    def page_info(self) -> "_PageInfoBase":
        return self._sdk_embed(_PageInfoBase, "pageInfo.")

    total_count = QueryField("totalCount")


class _VendorTokenEdgeBase(QueryFieldSet):
    _sdk_default_fields = [QueryField("cursor")]

    @property
    @lru_cache()
    def node(self) -> "_VendorTokenBase":
        return self._sdk_embed(_VendorTokenBase, "node.")

    cursor = QueryField("cursor")


class _VendorTokenBase(QueryFieldSet):
    _sdk_default_fields = [
        QueryField("id"),
        QueryField("creationDate"),
        QueryField("lastChangeDate"),
        QueryField("token"),
        QueryField("email"),
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


class _ResultConnectionBase(QueryFieldSet):
    _sdk_default_fields = [
        QueryField("id", "edges.node."),
        QueryField("creationDate", "edges.node."),
        QueryField("lastChangeDate", "edges.node."),
        QueryField("date", "edges.node."),
        QueryField("type", "edges.node."),
        QueryField("breakdownType", "edges.node."),
        QueryField("resource", "edges.node."),
        QueryField("breakdown", "edges.node."),
        QueryField("totalCount"),
    ]

    @property
    @lru_cache()
    def edges(self) -> "_ResultEdgeBase":
        return self._sdk_embed(_ResultEdgeBase, "edges.")

    @property
    @lru_cache()
    def page_info(self) -> "_PageInfoBase":
        return self._sdk_embed(_PageInfoBase, "pageInfo.")

    total_count = QueryField("totalCount")


class _ResultEdgeBase(QueryFieldSet):
    _sdk_default_fields = [QueryField("cursor")]

    @property
    @lru_cache()
    def node(self) -> "_ResultBase":
        return self._sdk_embed(_ResultBase, "node.")

    cursor = QueryField("cursor")


class _ResultBase(QueryFieldSet):
    _sdk_default_fields = [
        QueryField("id"),
        QueryField("creationDate"),
        QueryField("lastChangeDate"),
        QueryField("date"),
        QueryField("type"),
        QueryField("breakdownType"),
        QueryField("resource"),
        QueryField("breakdown"),
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
    _sdk_default_fields = [
        QueryField("results"),
        QueryField("impressions"),
        QueryField("clicks"),
        QueryField("spend"),
        QueryField("purchases"),
        QueryField("purchasesValue"),
    ]
    results = QueryField("results")
    impressions = QueryField("impressions")
    clicks = QueryField("clicks")
    spend = QueryField("spend")
    purchases = QueryField("purchases")
    purchases_value = QueryField("purchasesValue")


class _MarketingCampaignConnectionBase(QueryFieldSet):
    _sdk_default_fields = [
        QueryField("id", "edges.node."),
        QueryField("creationDate", "edges.node."),
        QueryField("lastChangeDate", "edges.node."),
        QueryField("resultsSource", "edges.node."),
        QueryField("kpi", "edges.node."),
        QueryField("systemStatus", "edges.node."),
        QueryField("errors", "edges.node."),
        QueryField("warnings", "edges.node."),
        QueryField("name", "edges.node."),
        QueryField("status", "edges.node."),
        QueryField("creativeSpec", "edges.node."),
        QueryField("runTimeSpec", "edges.node."),
        QueryField("locationSpec", "edges.node."),
        QueryField("conversionSpec", "edges.node."),
        QueryField("startDate", "edges.node."),
        QueryField("endDate", "edges.node."),
        QueryField("delivering", "edges.node."),
        QueryField("totalCount"),
    ]

    @property
    @lru_cache()
    def edges(self) -> "_MarketingCampaignEdgeBase":
        return self._sdk_embed(_MarketingCampaignEdgeBase, "edges.")

    @property
    @lru_cache()
    def page_info(self) -> "_PageInfoBase":
        return self._sdk_embed(_PageInfoBase, "pageInfo.")

    total_count = QueryField("totalCount")


class _MarketingCampaignEdgeBase(QueryFieldSet):
    _sdk_default_fields = [QueryField("cursor")]

    @property
    @lru_cache()
    def node(self) -> "_MarketingCampaignBase":
        return self._sdk_embed(_MarketingCampaignBase, "node.")

    cursor = QueryField("cursor")


class _MarketingCampaignBase(QueryFieldSet):
    _sdk_default_fields = [
        QueryField("id"),
        QueryField("creationDate"),
        QueryField("lastChangeDate"),
        QueryField("resultsSource"),
        QueryField("kpi"),
        QueryField("systemStatus"),
        QueryField("errors"),
        QueryField("warnings"),
        QueryField("name"),
        QueryField("status"),
        QueryField("creativeSpec"),
        QueryField("runTimeSpec"),
        QueryField("locationSpec"),
        QueryField("conversionSpec"),
        QueryField("startDate"),
        QueryField("endDate"),
        QueryField("delivering"),
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
    def marketing_ads(self) -> "_MarketingAdConnectionBase":
        return self._sdk_embed(_MarketingAdConnectionBase, "marketingAds.")

    @property
    @lru_cache()
    def products(self) -> "_ProductConnectionBase":
        return self._sdk_embed(_ProductConnectionBase, "products.")

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
    def results(self) -> "_ResultConnectionBase":
        return self._sdk_embed(_ResultConnectionBase, "results.")

    @property
    @lru_cache()
    def notifications(self) -> "_NotificationConnectionBase":
        return self._sdk_embed(_NotificationConnectionBase, "notifications.")


class _NotificationResourceBase(QueryFieldSet):
    _sdk_default_fields = [
        QueryField("id"),
        QueryField("creationDate"),
        QueryField("lastChangeDate"),
        QueryField("systemStatus"),
        QueryField("errors"),
        QueryField("warnings"),
    ]
    id = QueryField("id")
    creation_date = QueryField("creationDate")
    last_change_date = QueryField("lastChangeDate")
    system_status = QueryField("systemStatus")
    errors = QueryField("errors")
    warnings = QueryField("warnings")


class _GCPXBase(QueryFieldSet):
    _sdk_default_fields = [
        QueryField("id"),
        QueryField("creationDate"),
        QueryField("lastChangeDate"),
        QueryField("kpi"),
        QueryField("price"),
        QueryField("startDate"),
        QueryField("endDate"),
        QueryField("minConversions"),
        QueryField("maxConversions"),
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
    def marketing_campaigns(self) -> "_MarketingCampaignConnectionBase":
        return self._sdk_embed(_MarketingCampaignConnectionBase, "marketingCampaigns.")


class _MarketingAdConnectionBase(QueryFieldSet):
    _sdk_default_fields = [
        QueryField("id", "edges.node."),
        QueryField("creationDate", "edges.node."),
        QueryField("lastChangeDate", "edges.node."),
        QueryField("resultsSource", "edges.node."),
        QueryField("kpi", "edges.node."),
        QueryField("systemStatus", "edges.node."),
        QueryField("errors", "edges.node."),
        QueryField("warnings", "edges.node."),
        QueryField("remoteId", "edges.node."),
        QueryField("totalCount"),
    ]

    @property
    @lru_cache()
    def edges(self) -> "_MarketingAdEdgeBase":
        return self._sdk_embed(_MarketingAdEdgeBase, "edges.")

    @property
    @lru_cache()
    def page_info(self) -> "_PageInfoBase":
        return self._sdk_embed(_PageInfoBase, "pageInfo.")

    total_count = QueryField("totalCount")


class _MarketingAdEdgeBase(QueryFieldSet):
    _sdk_default_fields = [QueryField("cursor")]

    @property
    @lru_cache()
    def node(self) -> "_MarketingAdBase":
        return self._sdk_embed(_MarketingAdBase, "node.")

    cursor = QueryField("cursor")


class _MarketingAdBase(QueryFieldSet):
    _sdk_default_fields = [
        QueryField("id"),
        QueryField("creationDate"),
        QueryField("lastChangeDate"),
        QueryField("resultsSource"),
        QueryField("kpi"),
        QueryField("systemStatus"),
        QueryField("errors"),
        QueryField("warnings"),
        QueryField("remoteId"),
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
    def results(self) -> "_ResultConnectionBase":
        return self._sdk_embed(_ResultConnectionBase, "results.")

    @property
    @lru_cache()
    def marketing_campaign(self) -> "_MarketingCampaignBase":
        return self._sdk_embed(_MarketingCampaignBase, "marketingCampaign.")


class _AdPreviewBase(QueryFieldSet):
    _sdk_default_fields = [
        QueryField("url"),
        QueryField("dimensions"),
        QueryField("placement"),
    ]
    url = QueryField("url")
    dimensions = QueryField("dimensions")
    placement = QueryField("placement")


class _NotificationConnectionBase(QueryFieldSet):
    _sdk_default_fields = [
        QueryField("id", "edges.node."),
        QueryField("creationDate", "edges.node."),
        QueryField("lastChangeDate", "edges.node."),
        QueryField("title", "edges.node."),
        QueryField("message", "edges.node."),
        QueryField("status", "edges.node."),
        QueryField("severity", "edges.node."),
        QueryField("code", "edges.node."),
        QueryField("source", "edges.node."),
        QueryField("resource", "edges.node."),
        QueryField("totalCount"),
    ]

    @property
    @lru_cache()
    def edges(self) -> "_NotificationEdgeBase":
        return self._sdk_embed(_NotificationEdgeBase, "edges.")

    @property
    @lru_cache()
    def page_info(self) -> "_PageInfoBase":
        return self._sdk_embed(_PageInfoBase, "pageInfo.")

    total_count = QueryField("totalCount")


class _NotificationEdgeBase(QueryFieldSet):
    _sdk_default_fields = [QueryField("cursor")]

    @property
    @lru_cache()
    def node(self) -> "_NotificationBase":
        return self._sdk_embed(_NotificationBase, "node.")

    cursor = QueryField("cursor")


class _NotificationBase(QueryFieldSet):
    _sdk_default_fields = [
        QueryField("id"),
        QueryField("creationDate"),
        QueryField("lastChangeDate"),
        QueryField("title"),
        QueryField("message"),
        QueryField("status"),
        QueryField("severity"),
        QueryField("code"),
        QueryField("source"),
        QueryField("resource"),
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


class _CampaignTemplateConnectionBase(QueryFieldSet):
    _sdk_default_fields = [
        QueryField("id", "edges.node."),
        QueryField("creationDate", "edges.node."),
        QueryField("lastChangeDate", "edges.node."),
        QueryField("name", "edges.node."),
        QueryField("description", "edges.node."),
        QueryField("platform", "edges.node."),
        QueryField("remoteId", "edges.node."),
        QueryField("systemStatus", "edges.node."),
        QueryField("errors", "edges.node."),
        QueryField("warnings", "edges.node."),
        QueryField("kpi", "edges.node."),
        QueryField("totalCount"),
    ]

    @property
    @lru_cache()
    def edges(self) -> "_CampaignTemplateEdgeBase":
        return self._sdk_embed(_CampaignTemplateEdgeBase, "edges.")

    @property
    @lru_cache()
    def page_info(self) -> "_PageInfoBase":
        return self._sdk_embed(_PageInfoBase, "pageInfo.")

    total_count = QueryField("totalCount")


class _CampaignTemplateEdgeBase(QueryFieldSet):
    _sdk_default_fields = [QueryField("cursor")]

    @property
    @lru_cache()
    def node(self) -> "_CampaignTemplateBase":
        return self._sdk_embed(_CampaignTemplateBase, "node.")

    cursor = QueryField("cursor")


class _VendorConnectionBase(QueryFieldSet):
    _sdk_default_fields = [
        QueryField("id", "edges.node."),
        QueryField("creationDate", "edges.node."),
        QueryField("lastChangeDate", "edges.node."),
        QueryField("name", "edges.node."),
        QueryField("systemStatus", "edges.node."),
        QueryField("errors", "edges.node."),
        QueryField("warnings", "edges.node."),
        QueryField("totalCount"),
    ]

    @property
    @lru_cache()
    def edges(self) -> "_VendorEdgeBase":
        return self._sdk_embed(_VendorEdgeBase, "edges.")

    @property
    @lru_cache()
    def page_info(self) -> "_PageInfoBase":
        return self._sdk_embed(_PageInfoBase, "pageInfo.")

    total_count = QueryField("totalCount")


class _VendorEdgeBase(QueryFieldSet):
    _sdk_default_fields = [QueryField("cursor")]

    @property
    @lru_cache()
    def node(self) -> "_VendorBase":
        return self._sdk_embed(_VendorBase, "node.")

    cursor = QueryField("cursor")


class _CreativeTemplateConnectionBase(QueryFieldSet):
    _sdk_default_fields = [
        QueryField("id", "edges.node."),
        QueryField("creationDate", "edges.node."),
        QueryField("lastChangeDate", "edges.node."),
        QueryField("name", "edges.node."),
        QueryField("height", "edges.node."),
        QueryField("width", "edges.node."),
        QueryField("systemStatus", "edges.node."),
        QueryField("errors", "edges.node."),
        QueryField("warnings", "edges.node."),
        QueryField("totalCount"),
    ]

    @property
    @lru_cache()
    def edges(self) -> "_CreativeTemplateEdgeBase":
        return self._sdk_embed(_CreativeTemplateEdgeBase, "edges.")

    @property
    @lru_cache()
    def page_info(self) -> "_PageInfoBase":
        return self._sdk_embed(_PageInfoBase, "pageInfo.")

    total_count = QueryField("totalCount")


class _CreativeTemplateEdgeBase(QueryFieldSet):
    _sdk_default_fields = [QueryField("cursor")]

    @property
    @lru_cache()
    def node(self) -> "_CreativeTemplateBase":
        return self._sdk_embed(_CreativeTemplateBase, "node.")

    cursor = QueryField("cursor")


class _CreativeTemplateBase(QueryFieldSet):
    _sdk_default_fields = [
        QueryField("id"),
        QueryField("creationDate"),
        QueryField("lastChangeDate"),
        QueryField("name"),
        QueryField("height"),
        QueryField("width"),
        QueryField("systemStatus"),
        QueryField("errors"),
        QueryField("warnings"),
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
    def marketing_campaigns(self) -> "_MarketingCampaignConnectionBase":
        return self._sdk_embed(_MarketingCampaignConnectionBase, "marketingCampaigns.")

    @property
    @lru_cache()
    def creative_layers(self) -> "_CreativeLayerConnectionBase":
        return self._sdk_embed(_CreativeLayerConnectionBase, "creativeLayers.")


class _CreativeLayerConnectionBase(QueryFieldSet):
    _sdk_default_fields = [
        QueryField("id", "edges.node."),
        QueryField("creationDate", "edges.node."),
        QueryField("lastChangeDate", "edges.node."),
        QueryField("name", "edges.node."),
        QueryField("height", "edges.node."),
        QueryField("width", "edges.node."),
        QueryField("x", "edges.node."),
        QueryField("y", "edges.node."),
        QueryField("order", "edges.node."),
        QueryField("type", "edges.node."),
        QueryField("properties", "edges.node."),
        QueryField("systemStatus", "edges.node."),
        QueryField("errors", "edges.node."),
        QueryField("warnings", "edges.node."),
        QueryField("totalCount"),
    ]

    @property
    @lru_cache()
    def edges(self) -> "_CreativeLayerEdgeBase":
        return self._sdk_embed(_CreativeLayerEdgeBase, "edges.")

    @property
    @lru_cache()
    def page_info(self) -> "_PageInfoBase":
        return self._sdk_embed(_PageInfoBase, "pageInfo.")

    total_count = QueryField("totalCount")


class _CreativeLayerEdgeBase(QueryFieldSet):
    _sdk_default_fields = [QueryField("cursor")]

    @property
    @lru_cache()
    def node(self) -> "_CreativeLayerBase":
        return self._sdk_embed(_CreativeLayerBase, "node.")

    cursor = QueryField("cursor")


class _CreativeLayerBase(QueryFieldSet):
    _sdk_default_fields = [
        QueryField("id"),
        QueryField("creationDate"),
        QueryField("lastChangeDate"),
        QueryField("name"),
        QueryField("height"),
        QueryField("width"),
        QueryField("x"),
        QueryField("y"),
        QueryField("order"),
        QueryField("type"),
        QueryField("properties"),
        QueryField("systemStatus"),
        QueryField("errors"),
        QueryField("warnings"),
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


class _GCPXConnectionBase(QueryFieldSet):
    _sdk_default_fields = [
        QueryField("id", "edges.node."),
        QueryField("creationDate", "edges.node."),
        QueryField("lastChangeDate", "edges.node."),
        QueryField("kpi", "edges.node."),
        QueryField("price", "edges.node."),
        QueryField("startDate", "edges.node."),
        QueryField("endDate", "edges.node."),
        QueryField("minConversions", "edges.node."),
        QueryField("maxConversions", "edges.node."),
        QueryField("totalCount"),
    ]

    @property
    @lru_cache()
    def edges(self) -> "_GCPXEdgeBase":
        return self._sdk_embed(_GCPXEdgeBase, "edges.")

    @property
    @lru_cache()
    def page_info(self) -> "_PageInfoBase":
        return self._sdk_embed(_PageInfoBase, "pageInfo.")

    total_count = QueryField("totalCount")


class _GCPXEdgeBase(QueryFieldSet):
    _sdk_default_fields = [QueryField("cursor")]

    @property
    @lru_cache()
    def node(self) -> "_GCPXBase":
        return self._sdk_embed(_GCPXBase, "node.")

    cursor = QueryField("cursor")


class _CreativeFontBase(QueryFieldSet):
    _sdk_default_fields = [
        QueryField("id"),
        QueryField("creationDate"),
        QueryField("lastChangeDate"),
        QueryField("name"),
        QueryField("url"),
        QueryField("properties"),
        QueryField("systemStatus"),
        QueryField("errors"),
        QueryField("warnings"),
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


class _CreativeFontConnectionBase(QueryFieldSet):
    _sdk_default_fields = [
        QueryField("id", "edges.node."),
        QueryField("creationDate", "edges.node."),
        QueryField("lastChangeDate", "edges.node."),
        QueryField("name", "edges.node."),
        QueryField("url", "edges.node."),
        QueryField("properties", "edges.node."),
        QueryField("systemStatus", "edges.node."),
        QueryField("errors", "edges.node."),
        QueryField("warnings", "edges.node."),
        QueryField("totalCount"),
    ]

    @property
    @lru_cache()
    def edges(self) -> "_CreativeFontEdgeBase":
        return self._sdk_embed(_CreativeFontEdgeBase, "edges.")

    @property
    @lru_cache()
    def page_info(self) -> "_PageInfoBase":
        return self._sdk_embed(_PageInfoBase, "pageInfo.")

    total_count = QueryField("totalCount")


class _CreativeFontEdgeBase(QueryFieldSet):
    _sdk_default_fields = [QueryField("cursor")]

    @property
    @lru_cache()
    def node(self) -> "_CreativeFontBase":
        return self._sdk_embed(_CreativeFontBase, "node.")

    cursor = QueryField("cursor")


class _CreativeImageBase(QueryFieldSet):
    _sdk_default_fields = [
        QueryField("id"),
        QueryField("creationDate"),
        QueryField("lastChangeDate"),
        QueryField("name"),
        QueryField("url"),
        QueryField("properties"),
        QueryField("systemStatus"),
        QueryField("errors"),
        QueryField("warnings"),
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


class _CreativeImageConnectionBase(QueryFieldSet):
    _sdk_default_fields = [
        QueryField("id", "edges.node."),
        QueryField("creationDate", "edges.node."),
        QueryField("lastChangeDate", "edges.node."),
        QueryField("name", "edges.node."),
        QueryField("url", "edges.node."),
        QueryField("properties", "edges.node."),
        QueryField("systemStatus", "edges.node."),
        QueryField("errors", "edges.node."),
        QueryField("warnings", "edges.node."),
        QueryField("totalCount"),
    ]

    @property
    @lru_cache()
    def edges(self) -> "_CreativeImageEdgeBase":
        return self._sdk_embed(_CreativeImageEdgeBase, "edges.")

    @property
    @lru_cache()
    def page_info(self) -> "_PageInfoBase":
        return self._sdk_embed(_PageInfoBase, "pageInfo.")

    total_count = QueryField("totalCount")


class _CreativeImageEdgeBase(QueryFieldSet):
    _sdk_default_fields = [QueryField("cursor")]

    @property
    @lru_cache()
    def node(self) -> "_CreativeImageBase":
        return self._sdk_embed(_CreativeImageBase, "node.")

    cursor = QueryField("cursor")


class _TokenBase(QueryFieldSet):
    _sdk_default_fields = [
        QueryField("token"),
        QueryField("refreshToken"),
        QueryField("expiryDate"),
    ]
    token = QueryField("token")
    refresh_token = QueryField("refreshToken")
    expiry_date = QueryField("expiryDate")

    @property
    @lru_cache()
    def user(self) -> "_UserBase":
        return self._sdk_embed(_UserBase, "user.")


class _DeletionBase(QueryFieldSet):
    _sdk_default_fields = [QueryField("id")]
    id = QueryField("id")


class _RequestResultBase(QueryFieldSet):
    _sdk_default_fields = [QueryField("result")]
    result = QueryField("result")


class _MarketingCampaignSnapshotBase(QueryFieldSet):
    _sdk_default_fields = [
        QueryField("id"),
        QueryField("creationDate"),
        QueryField("lastChangeDate"),
        QueryField("successful"),
        QueryField("name"),
        QueryField("status"),
        QueryField("creativeSpec"),
        QueryField("runTimeSpec"),
        QueryField("locationSpec"),
        QueryField("kpi"),
        QueryField("productIds"),
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


class _MarketingCampaignSnapshotEdgeBase(QueryFieldSet):
    _sdk_default_fields = [QueryField("cursor")]

    @property
    @lru_cache()
    def node(self) -> "_MarketingCampaignSnapshotBase":
        return self._sdk_embed(_MarketingCampaignSnapshotBase, "node.")

    cursor = QueryField("cursor")


class _MarketingCampaignSnapshotConnectionBase(QueryFieldSet):
    _sdk_default_fields = [
        QueryField("id", "edges.node."),
        QueryField("creationDate", "edges.node."),
        QueryField("lastChangeDate", "edges.node."),
        QueryField("successful", "edges.node."),
        QueryField("name", "edges.node."),
        QueryField("status", "edges.node."),
        QueryField("creativeSpec", "edges.node."),
        QueryField("runTimeSpec", "edges.node."),
        QueryField("locationSpec", "edges.node."),
        QueryField("kpi", "edges.node."),
        QueryField("productIds", "edges.node."),
        QueryField("totalCount"),
    ]

    @property
    @lru_cache()
    def edges(self) -> "_MarketingCampaignSnapshotEdgeBase":
        return self._sdk_embed(_MarketingCampaignSnapshotEdgeBase, "edges.")

    @property
    @lru_cache()
    def page_info(self) -> "_PageInfoBase":
        return self._sdk_embed(_PageInfoBase, "pageInfo.")

    total_count = QueryField("totalCount")


class _SingleUseTokenBase(QueryFieldSet):
    _sdk_default_fields = [
        QueryField("id"),
        QueryField("creationDate"),
        QueryField("lastChangeDate"),
        QueryField("token"),
    ]
    id = QueryField("id")
    creation_date = QueryField("creationDate")
    last_change_date = QueryField("lastChangeDate")
    token = QueryField("token")

    @property
    @lru_cache()
    def user(self) -> "_UserBase":
        return self._sdk_embed(_UserBase, "user.")


class _SingleUseTokenEdgeBase(QueryFieldSet):
    _sdk_default_fields = [QueryField("cursor")]

    @property
    @lru_cache()
    def node(self) -> "_SingleUseTokenBase":
        return self._sdk_embed(_SingleUseTokenBase, "node.")

    cursor = QueryField("cursor")


class _SingleUseTokenConnectionBase(QueryFieldSet):
    _sdk_default_fields = [
        QueryField("id", "edges.node."),
        QueryField("creationDate", "edges.node."),
        QueryField("lastChangeDate", "edges.node."),
        QueryField("token", "edges.node."),
        QueryField("totalCount"),
    ]

    @property
    @lru_cache()
    def edges(self) -> "_SingleUseTokenEdgeBase":
        return self._sdk_embed(_SingleUseTokenEdgeBase, "edges.")

    @property
    @lru_cache()
    def page_info(self) -> "_PageInfoBase":
        return self._sdk_embed(_PageInfoBase, "pageInfo.")

    total_count = QueryField("totalCount")


CampaignTemplateFields = _CampaignTemplateBase()
MarketplaceFields = _MarketplaceBase()
EntitlementResourceFields = _EntitlementResourceBase()
OrganizationFields = _OrganizationBase()
UserConnectionFields = _UserConnectionBase()
UserEdgeFields = _UserEdgeBase()
UserFields = _UserBase()
MeFields = _MeBase()
OrganizationConnectionFields = _OrganizationConnectionBase()
OrganizationEdgeFields = _OrganizationEdgeBase()
PageInfoFields = _PageInfoBase()
EntitlementConnectionFields = _EntitlementConnectionBase()
EntitlementEdgeFields = _EntitlementEdgeBase()
EntitlementFields = _EntitlementBase()
MarketplaceConnectionFields = _MarketplaceConnectionBase()
MarketplaceEdgeFields = _MarketplaceEdgeBase()
MediaChannelConnectionFields = _MediaChannelConnectionBase()
MediaChannelEdgeFields = _MediaChannelEdgeBase()
MediaChannelFields = _MediaChannelBase()
CatalogConnectionFields = _CatalogConnectionBase()
CatalogEdgeFields = _CatalogEdgeBase()
CatalogFields = _CatalogBase()
ProductConnectionFields = _ProductConnectionBase()
ProductEdgeFields = _ProductEdgeBase()
ProductFields = _ProductBase()
ResultResourceFields = _ResultResourceBase()
VendorFields = _VendorBase()
VendorTokenConnectionFields = _VendorTokenConnectionBase()
VendorTokenEdgeFields = _VendorTokenEdgeBase()
VendorTokenFields = _VendorTokenBase()
ResultConnectionFields = _ResultConnectionBase()
ResultEdgeFields = _ResultEdgeBase()
ResultFields = _ResultBase()
ResultAnalyticsFields = _ResultAnalyticsBase()
MarketingCampaignConnectionFields = _MarketingCampaignConnectionBase()
MarketingCampaignEdgeFields = _MarketingCampaignEdgeBase()
MarketingCampaignFields = _MarketingCampaignBase()
NotificationResourceFields = _NotificationResourceBase()
GCPXFields = _GCPXBase()
MarketingAdConnectionFields = _MarketingAdConnectionBase()
MarketingAdEdgeFields = _MarketingAdEdgeBase()
MarketingAdFields = _MarketingAdBase()
AdPreviewFields = _AdPreviewBase()
NotificationConnectionFields = _NotificationConnectionBase()
NotificationEdgeFields = _NotificationEdgeBase()
NotificationFields = _NotificationBase()
CampaignTemplateConnectionFields = _CampaignTemplateConnectionBase()
CampaignTemplateEdgeFields = _CampaignTemplateEdgeBase()
VendorConnectionFields = _VendorConnectionBase()
VendorEdgeFields = _VendorEdgeBase()
CreativeTemplateConnectionFields = _CreativeTemplateConnectionBase()
CreativeTemplateEdgeFields = _CreativeTemplateEdgeBase()
CreativeTemplateFields = _CreativeTemplateBase()
CreativeLayerConnectionFields = _CreativeLayerConnectionBase()
CreativeLayerEdgeFields = _CreativeLayerEdgeBase()
CreativeLayerFields = _CreativeLayerBase()
GCPXConnectionFields = _GCPXConnectionBase()
GCPXEdgeFields = _GCPXEdgeBase()
CreativeFontFields = _CreativeFontBase()
CreativeFontConnectionFields = _CreativeFontConnectionBase()
CreativeFontEdgeFields = _CreativeFontEdgeBase()
CreativeImageFields = _CreativeImageBase()
CreativeImageConnectionFields = _CreativeImageConnectionBase()
CreativeImageEdgeFields = _CreativeImageEdgeBase()
TokenFields = _TokenBase()
DeletionFields = _DeletionBase()
RequestResultFields = _RequestResultBase()
MarketingCampaignSnapshotFields = _MarketingCampaignSnapshotBase()
MarketingCampaignSnapshotEdgeFields = _MarketingCampaignSnapshotEdgeBase()
MarketingCampaignSnapshotConnectionFields = _MarketingCampaignSnapshotConnectionBase()
SingleUseTokenFields = _SingleUseTokenBase()
SingleUseTokenEdgeFields = _SingleUseTokenEdgeBase()
SingleUseTokenConnectionFields = _SingleUseTokenConnectionBase()

__all__ = [
    "CampaignTemplateFields",
    "MarketplaceFields",
    "EntitlementResourceFields",
    "OrganizationFields",
    "UserConnectionFields",
    "UserEdgeFields",
    "UserFields",
    "MeFields",
    "OrganizationConnectionFields",
    "OrganizationEdgeFields",
    "PageInfoFields",
    "EntitlementConnectionFields",
    "EntitlementEdgeFields",
    "EntitlementFields",
    "MarketplaceConnectionFields",
    "MarketplaceEdgeFields",
    "MediaChannelConnectionFields",
    "MediaChannelEdgeFields",
    "MediaChannelFields",
    "CatalogConnectionFields",
    "CatalogEdgeFields",
    "CatalogFields",
    "ProductConnectionFields",
    "ProductEdgeFields",
    "ProductFields",
    "ResultResourceFields",
    "VendorFields",
    "VendorTokenConnectionFields",
    "VendorTokenEdgeFields",
    "VendorTokenFields",
    "ResultConnectionFields",
    "ResultEdgeFields",
    "ResultFields",
    "ResultAnalyticsFields",
    "MarketingCampaignConnectionFields",
    "MarketingCampaignEdgeFields",
    "MarketingCampaignFields",
    "NotificationResourceFields",
    "GCPXFields",
    "MarketingAdConnectionFields",
    "MarketingAdEdgeFields",
    "MarketingAdFields",
    "AdPreviewFields",
    "NotificationConnectionFields",
    "NotificationEdgeFields",
    "NotificationFields",
    "CampaignTemplateConnectionFields",
    "CampaignTemplateEdgeFields",
    "VendorConnectionFields",
    "VendorEdgeFields",
    "CreativeTemplateConnectionFields",
    "CreativeTemplateEdgeFields",
    "CreativeTemplateFields",
    "CreativeLayerConnectionFields",
    "CreativeLayerEdgeFields",
    "CreativeLayerFields",
    "GCPXConnectionFields",
    "GCPXEdgeFields",
    "CreativeFontFields",
    "CreativeFontConnectionFields",
    "CreativeFontEdgeFields",
    "CreativeImageFields",
    "CreativeImageConnectionFields",
    "CreativeImageEdgeFields",
    "TokenFields",
    "DeletionFields",
    "RequestResultFields",
    "MarketingCampaignSnapshotFields",
    "MarketingCampaignSnapshotEdgeFields",
    "MarketingCampaignSnapshotConnectionFields",
    "SingleUseTokenFields",
    "SingleUseTokenEdgeFields",
    "SingleUseTokenConnectionFields",
]
