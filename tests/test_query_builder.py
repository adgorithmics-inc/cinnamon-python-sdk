import unittest
from unittest.mock import patch

from cinnamon_sdk import Cinnamon, MarketingCampaignFields


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
