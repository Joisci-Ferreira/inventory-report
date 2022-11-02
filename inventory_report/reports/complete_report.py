from collections import Counter
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def complete_report_result(stock):
        empresas = [empresa["nome_da_empresa"] for empresa in stock]
        empresas_produtos = Counter(empresas)
        qtd_products = ""

        for company in empresas_produtos:
            qtd_products += (
                f"- {company}: {empresas_produtos[company]}\n"
                )

        return qtd_products

    @classmethod
    def generate(self, stock):
        simple_report_result = super().generate(stock)
        texto = self.complete_report_result(stock)
        return (
                f"{simple_report_result}\n"
                f"Produtos estocados por empresa:\n"
                f"{texto}"
            )
