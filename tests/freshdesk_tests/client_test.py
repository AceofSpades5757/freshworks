import unittest

from freshdesk import Client


class TestClient(unittest.TestCase):
    """ Test Freshdesk Client """

    def test_simple(self) -> None:
        """ The most simple set of tests. """
        client = Client('dummy-domain', 'API_KEY')
