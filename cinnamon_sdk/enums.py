from enum import Enum

class Platform(Enum):
    facebook = "facebook"
    sandbox = "sandbox"


class SystemStatus(Enum):
    PENDING = "PENDING"
    PENDING_SYNC = "PENDING_SYNC"
    PENDING_DELETION = "PENDING_DELETION"
    PENDING_APPROVAL = "PENDING_APPROVAL"
    PROCESSING = "PROCESSING"
    PROCESSING_SYNC = "PROCESSING_SYNC"
    PROCESSING_DELETION = "PROCESSING_DELETION"
    PROCESSED = "PROCESSED"
    ERROR = "ERROR"
    DELETED = "DELETED"


class OrganizationTierEnum(Enum):
    Standard = "Standard"
    Developer = "Developer"


class SORT_ORDER(Enum):
    ASC = "ASC"
    DESC = "DESC"


class EntitlementResourceTypeEnum(Enum):
    Organization = "Organization"
    Marketplace = "Marketplace"
    MediaChannel = "MediaChannel"


class AuthPermission(Enum):
    READ = "READ"
    WRITE = "WRITE"
    DELETE = "DELETE"
    MANAGE_ENTITLEMENTS = "MANAGE_ENTITLEMENTS"


class TokenStatus(Enum):
    PENDING = "PENDING"
    MISSING = "MISSING"
    VALID = "VALID"
    INVALID = "INVALID"


class CatalogType(Enum):
    bookable = "bookable"
    commerce = "commerce"
    destinations = "destinations"
    flights = "flights"
    home_listings = "home_listings"
    hotels = "hotels"
    offline_commerce = "offline_commerce"
    ticketed_experiences = "ticketed_experiences"
    transactable_items = "transactable_items"
    vehicles = "vehicles"


class MarketingCampaignStatus(Enum):
    ACTIVE = "ACTIVE"
    PAUSED = "PAUSED"


class ResultResourceTypeEnum(Enum):
    MarketingAd = "MarketingAd"
    MarketingCampaign = "MarketingCampaign"


class NOTIFICATION_STATUS(Enum):
    UNREAD = "UNREAD"
    READ = "READ"


class NOTIFICATION_SEVERITY(Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"


class NOTIFICATION_CODE(Enum):
    CAMPAIGN_ISSUE = "CAMPAIGN_ISSUE"
    CAMPAIGN_PERFORMANCE = "CAMPAIGN_PERFORMANCE"
    CAMPAIGN_INFO = "CAMPAIGN_INFO"


class CreativeLayerTypes(Enum):
    CREATIVE_TEXT_LAYER = "CREATIVE_TEXT_LAYER"
    CREATIVE_IMAGE_LAYER = "CREATIVE_IMAGE_LAYER"


class ReconcileStateEnum(Enum):
    LOCAL = "LOCAL"
    REMOTE = "REMOTE"


__all__ = [
    "Platform",
    "SystemStatus",
    "OrganizationTierEnum",
    "SORT_ORDER",
    "EntitlementResourceTypeEnum",
    "AuthPermission",
    "TokenStatus",
    "CatalogType",
    "MarketingCampaignStatus",
    "ResultResourceTypeEnum",
    "NOTIFICATION_STATUS",
    "NOTIFICATION_SEVERITY",
    "NOTIFICATION_CODE",
    "CreativeLayerTypes",
    "ReconcileStateEnum",
]
