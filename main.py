import data_download as dd
import data_plotting as dplt


def main():
    """ Основная функция, управляющая процессом загрузки, обработки данных и их визуализации. Запрашивает
     у пользователя ввод данных, вызывает функции загрузки и обработки данных, а затем передаёт результаты
      на визуализацию.
    """
    print("Добро пожаловать в инструмент получения и построения графиков биржевых данных.")
    print(
        "Вот несколько примеров биржевых тикеров, которые вы можете рассмотреть: AAPL (Apple Inc), GOOGL (Alphabet Inc),"
        " MSFT (Microsoft Corporation), AMZN (Amazon.com Inc), TSLA (Tesla Inc).")
    print(
        "Общие периоды времени для данных о запасах включают: 1д, 5д, 1мес, 3мес, 6мес, 1г, 2г, 5г, 10л, с начала года,"
        " макс.")

    ticker = input("Введите тикер акции (например, «AAPL» для Apple Inc):»")
    period = input("Введите период для данных (например: '1mo', '1d', '5d', '1mo', '3mo', '6mo', '1y',"
                   " '2y', '5y', '10y', 'ytd', 'max', 'yyyy-mm-dd, yyyy-mm-dd'): ")
    start = input("Введите дату начала анализа(yyyy-mm-dd):")
    end = input("Введите дату окончания для анализа данных(yyyy-mm-dd):")

    # Fetch stock data
    stock_data = dd.fetch_stock_data(ticker, period)

    # Add moving average to the data
    stock_data = dd.add_moving_average(stock_data)

    # Plot the data
    dplt.create_and_save_plot(stock_data, ticker, period, style=input)

    # Вычисляется среднее значение колонки 'Close'. Результат выводится в консоль.
    print('Средняя цена закрытия акций за заданный период: ', dd.calculate_and_display_average_price(stock_data))

    threshold = input("Уведомление о сильных колебаниях. Введите порог колебания цен в процентах: ")
    dd.notify_if_strong_fluctuations(stock_data, threshold)

    # Принимает DataFrame и имя файла и сохраняет данные об акциях в указанный файл.
    dd.export_data_to_csv(stock_data, "dataframe.csv'")

    #  Добавление дополнительных технических индикаторов
    data_rsi = dd.calculate_rsi_from_yfinance(ticker, period)
    data_macd = dd.calculate_macd_from_yfinance(ticker, period)

    # Визуализация технических индикаторов
    dplt.plot_technical_indicators(data_rsi, ticker, 'RSI')
    dplt.plot_technical_indicators(data_macd, ticker, 'MACD')

    #  Стандартное отклонение цены закрытия
    dd.statistical_indicator(stock_data, ticker)

    #  Интерактивный график
    dd.interactive_chart(stock_data, ticker)

    # Построение данных
    dplt.create_and_save_plot(stock_data, ticker, period, style='dark_background')


if __name__ == "__main__":
    main()
