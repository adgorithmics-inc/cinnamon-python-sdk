import os
import unittest

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

    # def test_single_object_and_delete(self):
    #     vendor = self.cinnamon.create_vendor(
    #         input=VendorInput(name="CinnaPy Vendor", marketplace_id=self.marketplace.id)
    #     )
    #     vendor_queried = self.cinnamon.vendor(id=vendor.id)
    #     self.assertEqual(vendor.id, vendor_queried.id)

    def test_paging(self):
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
        vendors_query = self.cinnamon.vendors(
            filter=FilterInput(
                field="id", operator=FilterOperator.IN, value=vendor_ids
            ),
            fields=[VendorConnectionFields.id],
        )
        for queried_vendor in vendors_query:
            self.assertFalse(queried_vendor.id in verified_vendor_ids)
            self.assertTrue(queried_vendor.id in vendor_ids)
            verified_vendor_ids.append(queried_vendor.id)
        self.assertEqual(len(vendor_ids), len(verified_vendor_ids))

    def test_sorting(self):
        pass

    def test_nested(self):
        pass
