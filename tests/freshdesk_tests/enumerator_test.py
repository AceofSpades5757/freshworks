""" Test general enumerators. """
import unittest

from freshdesk import APIVersion
from freshdesk import Plan


class TestPlan(unittest.TestCase):
    """ Test Freshdesk enumerators """

    def test_variants(self) -> None:
        """ Test different variants, and their interface.

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
