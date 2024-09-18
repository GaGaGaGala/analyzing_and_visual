import unittest
from data_download import fetch_stock_data, add_moving_average, notify_if_strong_fluctuations
from data_plotting import create_and_save_plot
import pandas as pd
import os


class Close(unittest.TestCase):
    def setUp(self):
        self.ticker = 'AAPL'
        self.period = '1mo'
        self.threshold = 5

        # Получение исторических данных об акциях для указанного тикера и временного периода

    def test_return_dataframe(self):
        stock_data = fetch_stock_data(self.ticker, self.period)
        self.assertIsInstance(stock_data, pd.DataFrame)

        # Добавление в DataFrame колонки со скользящим средним, рассчитанным на основе цен закрытия

    def test_add_moving_average(self):
        stock_data = fetch_stock_data(self.ticker, self.period)
        stock_data = add_moving_average(stock_data)
        self.assertTrue('Moving_Average' in stock_data.columns)

        # Проверка на вывод данных в консоль

    def test_output_to_console(self):
        stock_data = fetch_stock_data(self.ticker, self.period)

if __name__ == '__main__':
    unittest.main()