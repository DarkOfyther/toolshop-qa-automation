
from pages.search_page import SearchPage


def test_buscar_produto_existente(driver):
    busca = SearchPage(driver)

    produto_pesquisado = "Combination Pliers"

    busca.abrir()
    busca.pesquisar_produto(produto_pesquisado)

    resultado = busca.obter_nome_produto()

    assert resultado.is_displayed()
    assert resultado.text.strip() == produto_pesquisado


def test_buscar_produto_inexistente(driver):
    busca = SearchPage(driver)

    produto_pesquisado = "ProdutoInexistente123"

    busca.abrir()
    busca.pesquisar_produto(produto_pesquisado)

    mensagem = busca.obter_mensagem_resultado()

    assert mensagem == (
        "0 products found for 'ProdutoInexistente123'"
    )


def test_filtrar_produtos_por_faixa_de_preco(driver):
    busca = SearchPage(driver)

    preco_minimo = 10
    preco_maximo = 50

    busca.abrir()
    busca.filtrar_por_preco(preco_minimo, preco_maximo)

    precos = busca.obter_precos_produtos()

    assert len(precos) > 0

    for preco in precos:
        assert preco_minimo <= preco <= preco_maximo, (
            f"Produto com preço fora da faixa: ${preco}"
        )
