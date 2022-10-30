from statistics import mode


class CompanyFilter:
    def more_products(stock):
        empresas = [
          empresa['nome_da_empresa']
          for empresa in stock
        ]
        return mode(empresas)
