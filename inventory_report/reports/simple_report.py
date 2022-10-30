from inventory_report.reports.date_filter import DateFilter
from inventory_report.reports.company_filter import CompanyFilter


class SimpleReport:
    @staticmethod
    def generate(stock):
        oldst_manufacturing_date = DateFilter.oldst_date(stock)
        closest_expiration_date = DateFilter.closest_date(stock)
        company = CompanyFilter.more_products(stock)

        return (
          f"Data de fabricação mais antiga: {oldst_manufacturing_date}\n"
          f"Data de validade mais próxima: {closest_expiration_date}\n"
          f"Empresa com mais produtos: {company}"
        )
