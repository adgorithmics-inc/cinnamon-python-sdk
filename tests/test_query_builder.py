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
            ],
        )
        self.assertEqual(
            api.mock_calls[0][2]["query"],
            "query($id: ObjectId!) { marketingCampaign(id: $id) { id runTimeSpec GCPX{id}  } }",
        )
