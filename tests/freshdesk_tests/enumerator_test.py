""" Test general enumerators. """
import unittest

from freshdesk import APIVersion
from freshdesk import Plan


class TestPlan(unittest.TestCase):
    """Test Freshdesk enumerators"""

    def test_variants(self) -> None:
        """Test different variants, and their interface.

        WARNING: The tests were copy and pasted values. There doesn't need to
        be this many tests.
        """
        blossom = Plan.BLOSSOM
        garden = Plan.GARDEN
        estate = Plan.ESTATE
        forest = Plan.FOREST

        self.assertEqual(blossom.rates.per_minute, 100)
        self.assertEqual(blossom.rates.ticket_create, 40)
        self.assertEqual(blossom.rates.ticket_update, 40)
        self.assertEqual(blossom.rates.ticket_list, 40)
        self.assertEqual(blossom.rates.contacts_list, 40)

        self.assertEqual(garden.rates.per_minute, 200)
        self.assertEqual(garden.rates.ticket_create, 80)
        self.assertEqual(garden.rates.ticket_update, 60)
        self.assertEqual(garden.rates.ticket_list, 60)
        self.assertEqual(garden.rates.contacts_list, 60)

        self.assertEqual(estate.rates.per_minute, 400)
        self.assertEqual(estate.rates.ticket_create, 160)
        self.assertEqual(estate.rates.ticket_update, 160)
        self.assertEqual(estate.rates.ticket_list, 100)
        self.assertEqual(estate.rates.contacts_list, 100)

        self.assertEqual(forest.rates.per_minute, 700)
        self.assertEqual(forest.rates.ticket_create, 280)
        self.assertEqual(forest.rates.ticket_update, 280)
        self.assertEqual(forest.rates.ticket_list, 200)
        self.assertEqual(forest.rates.contacts_list, 200)


class TestAPIVersion(unittest.TestCase):
    """Test Freshdesk APIVersion"""

    def test_paths(self) -> None:
        """Test url path."""

        v1 = APIVersion(1)
        v2 = APIVersion(2)

        self.assertEqual(v1.path, '/v1')
        self.assertEqual(v2.path, '/v2')

    def test_constructors(self) -> None:
        """Test the different ways a user would want to generate a version."""

        v1_int = APIVersion(1)
        v1_dot = APIVersion.V1
        v2_int = APIVersion(2)
        v2_dot = APIVersion.V2

        self.assertEqual(v1_int, v1_dot)
        self.assertEqual(v2_int, v2_dot)
