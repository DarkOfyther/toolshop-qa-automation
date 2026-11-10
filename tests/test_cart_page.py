
from pages.product_page import ProductPage


def test_quantidade_zero_ajustada_para_um(driver, capturar_print):
    produto = ProductPage(driver)

    # Etapa 1 - Acessar a página do produto
    produto.abrir()
    capturar_print("01_pagina_produto")

    # Etapa 2 - Informar quantidade zero
    produto.informar_quantidade(0)
    capturar_print("02_quantidade_zero_informada")

    # Etapa 3 - Validar ajuste automático para 1
    quantidade = produto.obter_quantidade()
    capturar_print("03_quantidade_ajustada")

    assert quantidade == "1"


def test_adicionar_uma_unidade_ao_carrinho(driver, capturar_print):
    produto = ProductPage(driver)

    # Etapa 1 - Acessar a página do produto
    produto.abrir()
    capturar_print("01_pagina_produto")

    # Etapa 2 - Consultar contador inicial do carrinho
    contador_anterior = produto.obter_contador_carrinho()
    capturar_print("02_carrinho_antes_adicionar")

    # Etapa 3 - Adicionar uma unidade ao carrinho
    produto.adicionar_ao_carrinho()
    capturar_print("03_produto_adicionado")

    # Etapa 4 - Validar atualização do contador
    contador_atual = produto.obter_contador_carrinho()

    assert contador_atual == contador_anterior + 1


def test_quantidade_acima_do_limite(driver, capturar_print):
    produto = ProductPage(driver)

    # Etapa 1 - Acessar a página do produto
    produto.abrir()
    capturar_print("01_pagina_produto")

    # Etapa 2 - Informar quantidade acima do limite
    produto.informar_quantidade(100)
    capturar_print("02_quantidade_100_informada")

    # Etapa 3 - Capturar quantidade ajustada e mensagem
    quantidade = produto.obter_quantidade()
    mensagem = produto.obter_mensagem_limite()
    capturar_print("03_mensagem_limite")

    # Etapa 4 - Validar o limite máximo
    assert quantidade == "99"
    assert mensagem == "You can order at most 99 of this product."
