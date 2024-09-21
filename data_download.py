import yfinance as yf
import logging
import csv
import pandas as pd

logging.basicConfig(level=logging.INFO,
                    handlers=[logging.FileHandler('LOGGING/logging_download_plotting.log', 'w', 'utf-8')]
                    )


def fetch_stock_data(ticker, period='1mo'):
    """ Получает исторические данные об акциях для указанного тикера и временного периода.
     Возвращает DataFrame с данными."""
    stock = yf.Ticker(ticker)
    logging.info(f'Объект "Ticker" {stock}')
    data = stock.history(period=period)
    return data


def add_moving_average(data, window_size=5):
    """ Добавляет в DataFrame колонку со скользящим средним, рассчитанным на основе цен закрытия."""
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    logging.info(f'В DataFrame добавлено свойство "Moving_Average" {type(data)}')
    return data


def calculate_and_display_average_price(data):
    """Вычисляет и выводит среднюю цену закрытия акций за заданный период."""
    average_price = data['Close'].mean(axis=0)
    logging.info(f'Выводится среднее значение колонки "Close": {average_price}')
    print(f'Среднее значение колонки "Close": {average_price}\n')
    return data


def notify_if_strong_fluctuations(data, threshold):
    """Анализирует данные и уведомляет пользователя, если цена акций колебалась более чем на заданный процент за период.
    """
    list_prices_close = data['Close'].tolist()
    max_price, min_price = max(list_prices_close), min(list_prices_close)
    difference = max_price - min_price
    """Средняя цена и порог колебания цен в процентах:"""
    average_price = (max_price + min_price) / 2
    threshold = difference / (average_price / 100)
    """Разница между максимальной и минимальной ценой в процентах."""
    max_percent_price = max_price / (average_price / 100)
    min_percent_price = min_price / (average_price / 100)
    dif_percent_price = max_percent_price - min_percent_price
    if dif_percent_price > threshold:
        logging.info(f'Значение колебаний: {dif_percent_price}')
        print(f'Превышен порог цен -{dif_percent_price}, допустимое значение -{threshold}')


def export_data_to_csv(data, filename):
    """Принимает DataFrame и имя файла и сохраняет данные об акциях в указанный файл. """
    csv_filename = "dataframe.csv'"
    df = pd.DataFrame(data)
    df.to_csv('dataframe.csv', index=False)
    logging.info(f'Объект {type(data)} экспортирован в файл')
