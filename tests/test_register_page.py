
from pages.register_page import RegisterPage


def test_cadastro_data_nascimento_obrigatoria_vazia(driver, capturar_print):
    cadastro = RegisterPage(driver)

    # Etapa 1 - Acessar a tela de cadastro
    cadastro.abrir()
    capturar_print("01_tela_cadastro")

    # Etapa 2 - Tentar cadastrar sem preencher os campos
    cadastro.clicar_cadastrar()
    capturar_print("02_tentativa_cadastro_sem_preenchimento")

    # Etapa 3 - Capturar a mensagem de validação
    mensagem = cadastro.obter_mensagem_data_obrigatoria()
    capturar_print("03_mensagem_data_nascimento_obrigatoria")

    # Etapa 4 - Validar o resultado
    assert mensagem == "Date of Birth is required"
    assert "/auth/register" in driver.current_url
