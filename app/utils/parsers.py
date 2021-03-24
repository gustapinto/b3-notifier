from abc import ABC, abstractmethod


class BaseJsonParser(ABC):
    def __init__(self):
        self.parsed_data = []

    @abstractmethod
    def parse_data(self, data):
        pass

    @abstractmethod
    def format_stock_display(self, stock_data):
        pass


class HgBrasilParser(BaseJsonParser):
    def parse_data(self, data):
        fetched_data, stocks_list = data

        for key, stock in enumerate(stocks_list):
            self.uppercase_stock_name = stock.upper()

            stock_data = fetched_data[key]['results'][self.uppercase_stock_name]

            self.format_stock_display(stock_data)

            self.parsed_data.append((self.stock_display, self.stock_price))

        return self.parsed_data

    def format_stock_display(self, stock_data):
        self.stock_price = stock_data['price']

        self.stock_display = f'{self.uppercase_stock_name} R${str(self.stock_price)} | '
