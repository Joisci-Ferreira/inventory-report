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


phrases = (
    "O produto Cafe"
    " fabricado em 2020-07-04"
    " por Cafes Nature com validade"
    " até 2023-02-09"
    " precisa ser armazenado instrucao."
)


def test_relatorio_produto():
    pass  # Seu teste deve ser escrito aqui

    new_product = Product(*product)
    assert str(new_product) == phrases
