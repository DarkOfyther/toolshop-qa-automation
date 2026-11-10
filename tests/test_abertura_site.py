
def test_abrir_site(driver, capturar_print):

    # Etapa 1 - Acessar o site
    driver.get("https://practicesoftwaretesting.com/")

    # Etapa 2 - Capturar a página inicial
    capturar_print("01_pagina_inicial")

    # Etapa 3 - Validar o título
    assert "Practice Software Testing" in driver.title
