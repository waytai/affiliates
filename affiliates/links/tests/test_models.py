from nose.tools import eq_

from affiliates.base.tests import TestCase
from affiliates.links.tests import DataPointFactory, LinkFactory


class LinkTests(TestCase):
    def test_get_metric_total(self):
        """
        _get_metric_total should combine the aggregate data on the link
        and the data stored in multiple data points.
        """
        link = LinkFactory.create(aggregate_link_clicks=58)
        DataPointFactory.create(link=link, link_clicks=5)
        DataPointFactory.create(link=link, link_clicks=2)
        DataPointFactory.create(link=link, link_clicks=87)

        eq_(link._get_metric_total('link_clicks'), 58 + 5 + 2 + 87)
