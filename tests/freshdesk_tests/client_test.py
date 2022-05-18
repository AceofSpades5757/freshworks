""" Test Client """
import unittest

from freshdesk import Client


class TestClient(unittest.TestCase):
    """Test Freshdesk Client"""

    def test_simple(self) -> None:
        """The most simple set of tests."""
        client = Client('dummy-domain', 'API_KEY')

    def test_paths(self) -> None:
        """Test the client paths."""
        client = Client('test', 'API_KEY')

        self.assertEqual(client.domain, 'test')
        self.assertEqual(client.hostname, 'https://test.freshdesk.com')
        self.assertEqual(client.base_url, 'https://test.freshdesk.com/api/v2')
