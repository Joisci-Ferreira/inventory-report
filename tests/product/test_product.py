from inventory_report.inventory.product import Product


product = [
    1,
    "Cafe",
    "Cafes Nature",
    "2020-07-04",
    "2023-02-09",
    "FR48",
    "instrucao"
]


def test_cria_produto():
    pass  # Seu teste deve ser escrito aqui

    new_product = Product(*product)
    assert new_product.id == 1
    assert new_product.nome_do_produto == "Cafe"
    assert new_product.nome_da_empresa == "Cafes Nature"
    assert new_product.data_de_fabricacao == "2020-07-04"
    assert new_product.data_de_validade == "2023-02-09"
    assert new_product.numero_de_serie == "FR48"
    assert new_product.instrucoes_de_armazenamento == "instrucao"
