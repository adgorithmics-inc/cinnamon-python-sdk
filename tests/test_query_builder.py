import json
import datetime
import unittest
from unittest.mock import patch

from cinnamon_sdk import (
    Cinnamon,
    MarketingCampaignFields,
    VendorConnectionFields,
    MarketingCampaignUpdateInput,
)
from cinnamon_sdk.internals.json_codecs import datetime_encoder


class TestQueryBuilder(unittest.TestCase):
    @patch("cinnamon_sdk.cinnamon.Cinnamon.api")
    def test_query_builder(self, api):
        api.return_value = {"data": {"marketingCampaign": {"id": 1}}}
        cinna = Cinnamon(url="")
        cinna.marketing_campaign(
            "1",
            [
                MarketingCampaignFields.id,
                MarketingCampaignFields.run_time_spec,
                MarketingCampaignFields.gcpx.id,
                MarketingCampaignFields.gcpx.price,
                MarketingCampaignFields.gcpx.campaign_template.id,
                MarketingCampaignFields.gcpx.campaign_template.name,
                "tarst",
                MarketingCampaignFields.products.id,
            ],
        )
        self.assertEqual(
            api.mock_calls[0][2]["query"],
            "query($id: ObjectId!) { marketingCampaign(id: $id) { tarst id runTimeSpec GCPX{id price campaignTemplate{id name}} products{edges{node{id}}}  } }",
        )

    @patch("cinnamon_sdk.cinnamon.Cinnamon.api")
    def test_query_builder_adds_paging_vars(self, api):
        # This tests the spacing between given QueryField and string variables for auto-paged queries
        api.return_value = {"data": {"vendors": {"edges": [{"node": {"id": 1}}]}}}
        cinna = Cinnamon(url="")
        next(cinna.vendors(fields=[VendorConnectionFields.id, "totalCount"]))
        self.assertEqual(
            api.mock_calls[0][2]["query"],
            "query($after: String) { vendors(after: $after) { totalCount edges{node{id}} pageInfo{endCursor hasNextPage}  } }",
        )

    @patch("cinnamon_sdk.cinnamon.Cinnamon._network_request")
    def test_query_builder_converts_datetime_objects(self, network_request):
        class FakeResponse:
            def json(self):
                return {"data": {"updateMarketingCampaign": {}}}

        the_time = datetime.datetime.utcnow()
        network_request.return_value = FakeResponse()
        cinna = Cinnamon(url="")
        cinna.update_marketing_campaign(
            id=1,
            input=MarketingCampaignUpdateInput(
                product_ids=[], run_time_spec={"startDate": the_time}
            ),
        )
        sent_dict = json.loads(network_request.mock_calls[0][2]["data"])
        self.assertEqual(
            sent_dict["variables"]["input"]["runTimeSpec"]["startDate"],
            datetime_encoder(the_time),
        )

    @patch("cinnamon_sdk.cinnamon.Cinnamon.api")
    def test_query_builder_translates_snake_case_correctly(self, api):
        api.return_value = {"data": {"approveMarketingCampaign": {}}}
        cinna = Cinnamon(url="")
        the_time = datetime.datetime.utcnow()
        cinna.approve_marketing_campaign(id=1, last_change_date=the_time)
        self.assertEqual(
            api.mock_calls[0][2]["variables"], {"id": 1, "lastChangeDate": the_time}
        )
