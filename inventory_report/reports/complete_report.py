from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.date_filter import DateFilter
from inventory_report.reports.company_filter import CompanyFilter
from inventory_report.reports.info_complete_report import (result)


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(stock):
        oldest = DateFilter.oldst_date(stock)
        closest = DateFilter.closest_date(stock)
        company = CompanyFilter.more_products(stock)
        return result(
              oldest,
              closest,
              company, stock)
