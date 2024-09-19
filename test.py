import unittest
from data_download import fetch_stock_data, add_moving_average, notify_if_strong_fluctuations
from data_plotting import create_and_save_plot
import pandas as pd
import os


class Close(unittest.TestCase):
    def setUp(self):
        self.ticker = 'AAPL'
        self.period = '1mo'
        self.threshold = 10

        # Получение исторических данных об акциях для указанного тикера и временного периода

    def test_return_dataframe(self):
        data = fetch_stock_data(self.ticker, self.period)
        self.assertIsInstance(data, pd.DataFrame)

        # Добавление в DataFrame колонки со скользящим средним, рассчитанным на основе цен закрытия

    def test_add_moving_average(self):
        data = fetch_stock_data(self.ticker, self.period)
        data = add_moving_average(data)
        self.assertTrue('Moving_Average' in data.columns)

        # Проверка на вывод данных в консоль

    def test_output_to_console(self):
        data = fetch_stock_data(self.ticker, self.period)
        self.assertTrue(data)

if __name__ == '__main__':
    unittest.main()