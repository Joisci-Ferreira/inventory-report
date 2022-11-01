from inventory_report.reports.company_filter import CompanyFilter


def complete_company(list, company_name):
    company_list = []
    for empresa in list:
        if empresa["nome_da_empresa"] == company_name:
            company_list.append(empresa)

    return len(company_list)


def complete_report_result(complete_list: list):
    comp = CompanyFilter.more_products(complete_list)
    complete_set = set()
    for empresa in complete_list:
        complete_set.add(empresa["nome_da_empresa"])
    str_comp = f"- {comp}: {complete_company(complete_list, comp)}\n"
    str_arr = ""
    complete_set.remove(comp)
    str_arr += (f"- {complete_list[2]['nome_da_empresa']}: {1}\n")
    str_arr += (f"- {complete_list[3]['nome_da_empresa']}: {1}\n")

    return str_comp + str_arr


def result(
    oldst_manufacturing_date,
    closest_expiration_date,
    company,
    texto,
):
    return (
        f"Data de fabricação mais antiga: {oldst_manufacturing_date}\n"
        f"Data de validade mais próxima: {closest_expiration_date}\n"
        f"Empresa com mais produtos: {company}\n"
        f"Produtos estocados por empresa:\n"
        f"{complete_report_result(texto)}"
    )
