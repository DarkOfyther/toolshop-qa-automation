from pages.checkout_page import CheckoutPage


def test_checkout_completo(driver):
    checkout = CheckoutPage(driver)

    # Etapa 1 - Carrinho
    driver.get(
        "https://practicesoftwaretesting.com/product/"
        "01M70QFRJSCAT65XR6WTSAG4EH"
    )

    # Adiciona uma unidade ao carrinho
    from pages.product_page import ProductPage

    produto = ProductPage(driver)
    produto.informar_quantidade(1)
    produto.adicionar_ao_carrinho()

    # Acessa o carrinho
    driver.get("https://practicesoftwaretesting.com/checkout")

    checkout.prosseguir_do_carrinho()

    # Etapa 2 - Login
    checkout.realizar_login()

    # Etapa 3 - Endereço de cobrança
    checkout.preencher_endereco()

    # Etapa 4 - Pagamento
    checkout.selecionar_pagamento()
    checkout.finalizar_pagamento()

    # Exibe o resultado para identificarmos a confirmação
    print("\nURL final:", driver.current_url)
    print("\nConteúdo final da página:")
    print(driver.find_element("tag name", "body").text)