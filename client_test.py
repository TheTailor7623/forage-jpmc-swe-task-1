import unittest
from client3 import getDataPoint
from client3 import getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      #Version 1 of my answer
      #self.assertEqual(getDataPoint(quote), quote["top_bid"]["price"])
      #self.assertEqual(getDataPoint(quote), quote["top_ask"]["price"])
      #self.assertEqual(getDataPoint(quote), (quote["bid_price"] + quote["ask_price"]) / 2)

      #Version 2 of my answer
      #self.assertEqual(getDataPoint(quote), quote["stock"], quote["top_bid"]["price"], quote["top_ask"]["price"], (quote["top_bid"]["price"] + quote["top_ask"]["price"]) / 2)

      #Final version of my answer
      expected_price = (quote["top_bid"]["price"] + quote["top_ask"]["price"]) / 2
      expected_output = (quote["stock"], quote["top_bid"]["price"], quote["top_ask"]["price"], expected_price)
      self.assertEqual(getDataPoint(quote), expected_output)

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      #Version 1 of my answer
      expected_price = (quote["top_bid"]["price"] + quote["top_ask"]["price"]) / 2
      expected_output = (quote["stock"], quote["top_bid"]["price"], quote["top_ask"]["price"], expected_price)
      self.assertEqual(getDataPoint(quote), expected_output)
      
  """ ------------ Add more unit tests ------------ """
  def test_getRatio_calculate(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
      #Version 1 of my answer
      #self.assertEqual(getRatio(quote["top_ask"]["price"], quote["top_bid"]["price"]), quote["top_ask"]["price"] / quote["top_bid"]["price"])

      #Final answer
    for quote in quotes:
      expected_ratio = quote["top_ask"]["price"] / quote["top_bid"]["price"]
      price_a = quote["top_ask"]["price"]
      price_b = quote["top_bid"]["price"]
      self.assertEqual(getRatio(price_a, price_b), expected_ratio)

  def test_getRatio_zeroDivision(self):
      price_a = 120.48
      price_b = 0
      # Check if getRatio handles division by zero
      self.assertIsNone(getRatio(price_a, price_b))



if __name__ == '__main__':
    unittest.main()
