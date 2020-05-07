import unittest
import datetime

from cinnamon_sdk.objects import (
    MarketingCampaign,
    Vendor,
    CampaignTemplate,
    VendorToken,
    VendorTokenConnection,
)


class TestObjectMapper(unittest.TestCase):
    def test_object_mapping(self):
        api_data = {
            "id": 1,
            "vendor": {"id": 2},
        }
        mc = MarketingCampaign(api_data)
        self.assertTrue(isinstance(mc, MarketingCampaign))
        self.assertTrue(mc.id, 1)
        self.assertTrue(isinstance(mc.vendor, Vendor))
        self.assertTrue(mc.vendor.id, 2)

    def test_object_mapping_iterable_scalars(self):
        errors = [{"one": "one"}, {"two": "two"}]
        api_data = {"id": 1, "errors": errors}
        ct = CampaignTemplate(api_data)
        self.assertTrue(isinstance(ct, CampaignTemplate))
        self.assertTrue(ct.id, 1)
        self.assertEqual(ct.errors, errors)

    def test_object_mapping_nested_iterable_objects(self):
        vendor_token = {"id": 3}
        api_data = {
            "id": 1,
            "vendor": {"id": 2, "vendorTokens": {"edges": [{"node": vendor_token}]}},
        }
        mc = MarketingCampaign(api_data)
        self.assertTrue(isinstance(mc, MarketingCampaign))
        self.assertTrue(mc.id, 1)
        self.assertTrue(isinstance(mc.vendor, Vendor))
        self.assertTrue(mc.vendor.id, 2)
        self.assertTrue(isinstance(mc.vendor.vendor_tokens, VendorTokenConnection))
        self.assertTrue(isinstance(mc.vendor.vendor_tokens.edges, list))
        self.assertTrue(isinstance(mc.vendor.vendor_tokens.edges[0].node, VendorToken))
        self.assertTrue(mc.vendor.vendor_tokens.edges[0].node.id, 3)

        arr = [token for token in mc.vendor.vendor_tokens]
        self.assertEqual(len(arr), 1)
        self.assertTrue(isinstance(arr[0], VendorToken))
        self.assertTrue(arr[0].id, 3)

    def test_interprets_datetime(self):
        api_data = {
            "id": 1,
            "creationDate": "2020-01-01T01:01:01.001Z",
        }
        mc = MarketingCampaign(api_data)
        self.assertTrue(isinstance(mc.creation_date, datetime.datetime))
        self.assertEqual(mc.creation_date.year, 2020)
        self.assertEqual(mc.creation_date.month, 1)
        self.assertEqual(mc.creation_date.day, 1)
        self.assertEqual(mc.creation_date.hour, 1)
        self.assertEqual(mc.creation_date.minute, 1)
        self.assertEqual(mc.creation_date.second, 1)
        self.assertEqual(mc.creation_date.microsecond, 1000)
