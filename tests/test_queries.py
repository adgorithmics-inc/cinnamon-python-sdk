import os
import unittest
import datetime

from cinnamon_sdk import (
    Cinnamon,
    OrganizationInput,
    MarketplaceInput,
    VendorInput,
    Organization,
    Marketplace,
    FilterOperator,
    FilterInput,
    VendorConnectionFields,
    VendorFields,
    SortInput,
    SORT_ORDER,
)


class TestQueries(unittest.TestCase):
    cinnamon: Cinnamon
    organization: Organization
    marketplace: Marketplace

    def setUp(self):
        self.cinnamon = Cinnamon(url=os.environ.get("CINNAMON_PYTHON_SDK_URL"))
        self.cinnamon.login(
            email=os.environ.get("CINNAMON_PYTHON_SDK_EMAIL"),
            password=os.environ.get("CINNAMON_PYTHON_SDK_PASSWORD"),
        )
        self.organization = self.cinnamon.create_organization(
            input=OrganizationInput(name="CinnaPy Organization")
        )
        self.marketplace = self.cinnamon.create_marketplace(
            input=MarketplaceInput(
                name="CinnaPy Marketplace", organization_id=self.organization.id
            )
        )

    def tearDown(self):
        if self.organization:
            self.cinnamon.delete_organization(id=self.organization.id)

    def test_single_object_and_delete(self):
        vendor = self.cinnamon.create_vendor(
            input=VendorInput(name="CinnaPy Vendor", marketplace_id=self.marketplace.id)
        )
        vendor_queried = self.cinnamon.vendor(id=vendor.id)
        self.assertEqual(vendor.id, vendor_queried.id)

    def test_paging_and_filtering(self):
        vendors = [
            self.cinnamon.create_vendor(
                input=VendorInput(
                    name=f"CinnaPy Vendor {i}", marketplace_id=self.marketplace.id
                )
            )
            for i in range(0, 100)
        ]
        vendor_ids = [vendor.id for vendor in vendors]
        verified_vendor_ids = []
        vendors_query = self.cinnamon.vendors_each(
            filter=FilterInput(
                field="id", operator=FilterOperator.IN, value=vendor_ids
            ),
            fields=[VendorConnectionFields.edges.node.id],
        )
        for queried_vendor in vendors_query:
            self.assertFalse(queried_vendor.id in verified_vendor_ids)
            self.assertTrue(queried_vendor.id in vendor_ids)
            verified_vendor_ids.append(queried_vendor.id)
        self.assertEqual(len(vendor_ids), len(verified_vendor_ids))

    def test_sorting(self):
        vendor = self.cinnamon.create_vendor(
            input=VendorInput(
                name="CinnaPy Vendor 1", marketplace_id=self.marketplace.id
            )
        )
        vendor_2 = self.cinnamon.create_vendor(
            input=VendorInput(
                name="CinnaPy Vendor 2", marketplace_id=self.marketplace.id
            )
        )
        queried_vendors = [
            v.id
            for v in self.cinnamon.vendors_each(
                filter=FilterInput("id", FilterOperator.IN, [vendor.id, vendor_2.id]),
                sort=SortInput("name", SORT_ORDER.DESC),
            )
        ]
        self.assertEqual([vendor_2.id, vendor.id], queried_vendors)

    def test_nested(self):
        vendor = self.cinnamon.create_vendor(
            input=VendorInput(
                name="CinnaPy Vendor 1", marketplace_id=self.marketplace.id
            )
        )
        queried_vendor = self.cinnamon.vendor(
            vendor.id, fields=[VendorFields.marketplace.organization.name]
        )
        self.assertEqual(
            queried_vendor.marketplace.organization.name, self.organization.name
        )

    def test_scalar_decodes(self):
        vendor = self.cinnamon.create_vendor(
            input=VendorInput(name="CinnaPy Vendor", marketplace_id=self.marketplace.id)
        )
        self.assertIsInstance(vendor.creation_date, datetime.datetime)

    def test_query_with_blank_results(self):
        # This test should not raise an exception
        [v for v in self.cinnamon.creative_templates_each()]

    def test_auto_refresh_login(self):
        self.cinnamon.refresh_login()
