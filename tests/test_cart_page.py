from pages.product_page import ProductPage


def test_quantidade_zero_ajustada_para_um(driver):
    produto = ProductPage(driver)

    produto.abrir()
    produto.informar_quantidade(0)

    quantidade = produto.obter_quantidade()

    assert quantidade == "1"


def test_adicionar_uma_unidade_ao_carrinho(driver):
    produto = ProductPage(driver)

    produto.abrir()

    contador_anterior = produto.obter_contador_carrinho()

    produto.adicionar_ao_carrinho()

    contador_atual = produto.obter_contador_carrinho()

    assert contador_atual == contador_anterior + 1


def test_quantidade_acima_do_limite(driver):
    produto = ProductPage(driver)

    produto.abrir()
    produto.informar_quantidade(100)

    quantidade = produto.obter_quantidade()
    mensagem = produto.obter_mensagem_limite()

    assert quantidade == "99"
    assert mensagem == "You can order at most 99 of this product."