
from pages.register_page import RegisterPage


def test_cadastro_data_nascimento_obrigatoria_vazia(driver):
    cadastro = RegisterPage(driver)

    cadastro.abrir()
    cadastro.clicar_cadastrar()

    mensagem = cadastro.obter_mensagem_data_obrigatoria()

    assert mensagem == "Date of Birth is required"
    assert "/auth/register" in driver.current_url
