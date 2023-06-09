from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(self, path):
        if path.endswith(".csv"):
            stock = []
            with open(path) as file:
                stock_csv = csv.DictReader(file)
                for elemento in stock_csv:
                    stock.append(elemento)
            return stock
        else:
            raise (ValueError("Arquivo inválido"))
