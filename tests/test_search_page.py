
from pages.search_page import SearchPage


def test_buscar_produto_existente(driver, capturar_print):
    busca = SearchPage(driver)

    produto_pesquisado = "Combination Pliers"

    # Etapa 1 - Acessar a página inicial
    busca.abrir()
    capturar_print("01_pagina_inicial")

    # Etapa 2 - Pesquisar produto existente
    busca.pesquisar_produto(produto_pesquisado)
    capturar_print("02_produto_pesquisado")

    # Etapa 3 - Obter o resultado
    resultado = busca.obter_nome_produto()
    capturar_print("03_resultado_encontrado")

    # Etapa 4 - Validar o resultado
    assert resultado.is_displayed()
    assert resultado.text.strip() == produto_pesquisado


def test_buscar_produto_inexistente(driver, capturar_print):
    busca = SearchPage(driver)

    produto_pesquisado = "ProdutoInexistente123"

    # Etapa 1 - Acessar a página inicial
    busca.abrir()
    capturar_print("01_pagina_inicial")

    # Etapa 2 - Pesquisar produto inexistente
    busca.pesquisar_produto(produto_pesquisado)
    capturar_print("02_produto_inexistente_pesquisado")

    # Etapa 3 - Obter a mensagem de resultado
    mensagem = busca.obter_mensagem_resultado()
    capturar_print("03_mensagem_sem_resultados")

    # Etapa 4 - Validar a mensagem
    assert mensagem == (
        "0 products found for 'ProdutoInexistente123'"
    )


def test_filtrar_produtos_por_faixa_de_preco(driver, capturar_print):
    busca = SearchPage(driver)

    preco_minimo = 10
    preco_maximo = 50

    # Etapa 1 - Acessar a página inicial
    busca.abrir()
    capturar_print("01_pagina_inicial")

    # Etapa 2 - Aplicar o filtro de preço
    busca.filtrar_por_preco(preco_minimo, preco_maximo)
    capturar_print("02_filtro_de_preco_aplicado")

    # Etapa 3 - Obter os preços dos produtos
    precos = busca.obter_precos_produtos()
    capturar_print("03_produtos_filtrados")

    # Etapa 4 - Validar os resultados
    assert len(precos) > 0

    for preco in precos:
        assert preco_minimo <= preco <= preco_maximo, (
            f"Produto com preço fora da faixa: ${preco}"
        )
