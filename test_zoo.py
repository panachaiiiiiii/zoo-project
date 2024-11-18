import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(5), 50)
       
    # Add your additional test cases here.
    def test_none_age_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(-2000), "No Way!!")
    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(8), 50)
    def test_teenager_price(self):
        self.assertEqual(self.zoo.get_ticket_price(17), 100)
    def test_adult_age_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(27), 150)
    def test_elderly_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(67), 100)
if __name__ == '__main__':
    unittest.main() 