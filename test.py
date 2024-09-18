import unittest
import main
import data_download


class DataTest(unittest.TestCase):
    def test_fetch_stock_data(self):
        st = stock_data
        self.assertTrue(stock_data)