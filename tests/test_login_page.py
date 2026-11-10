
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage


def test_login_valido(driver, capturar_print):
    login = LoginPage(driver)

    # Etapa 1 - Acessar a tela de login
    login.abrir()
    capturar_print("01_tela_login")

    # Etapa 2 - Preencher as credenciais
    login.preencher_email("admin@practicesoftwaretesting.com")
    login.preencher_senha("welcome01")
    capturar_print("02_credenciais_preenchidas")

    # Etapa 3 - Clicar em entrar
    login.clicar_entrar()

    # Etapa 4 - Aguardar o dashboard
    WebDriverWait(driver, 15).until(
        EC.url_contains("/admin/dashboard")
    )
    capturar_print("03_dashboard_acessado")

    assert "/admin/dashboard" in driver.current_url


def test_login_senha_incorreta(driver, capturar_print):
    login = LoginPage(driver)

    # Etapa 1 - Acessar a tela de login
    login.abrir()
    capturar_print("01_tela_login")

    # Etapa 2 - Preencher as credenciais incorretas
    login.preencher_email("admin@practicesoftwaretesting.com")
    login.preencher_senha("senhaerrada123")
    capturar_print("02_credenciais_preenchidas")

    # Etapa 3 - Tentar entrar
    login.clicar_entrar()

    # Etapa 4 - Capturar a mensagem de erro
    mensagem = login.obter_mensagem_erro()
    capturar_print("03_mensagem_erro")

    assert mensagem == "Invalid email or password"
    assert "/auth/login" in driver.current_url
