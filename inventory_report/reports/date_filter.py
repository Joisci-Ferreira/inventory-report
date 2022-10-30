from datetime import datetime


class DateFilter:
    def oldst_date(stock):
        data_antiga = [
          data['data_de_fabricacao']
          for data in stock
        ]
        return min(data_antiga)

    def closest_date(stock):
        data_atual = datetime.now().strftime('%Y-%m-%d')
        data_antiga = [
             data['data_de_validade']
             for data in stock
             if data['data_de_validade'] > data_atual
        ]

        return min(data_antiga)
