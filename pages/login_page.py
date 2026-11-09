
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    URL = "https://practicesoftwaretesting.com/auth/login"

    # Localizadores
    CAMPO_EMAIL = (By.ID, "email")
    CAMPO_SENHA = (By.ID, "password")
    BOTAO_ENTRAR = (By.CSS_SELECTOR, '[data-test="login-submit"]')
    MENSAGEM_ERRO = (By.CSS_SELECTOR, '[data-test="login-error"]')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def abrir(self):
        self.driver.get(self.URL)

    def preencher_email(self, email):
        campo = self.wait.until(
            EC.visibility_of_element_located(self.CAMPO_EMAIL)
        )
        campo.clear()
        campo.send_keys(email)

    def preencher_senha(self, senha):
        campo = self.wait.until(
            EC.visibility_of_element_located(self.CAMPO_SENHA)
        )
        campo.clear()
        campo.send_keys(senha)

    def clicar_entrar(self):
        botao = self.wait.until(
            EC.element_to_be_clickable(self.BOTAO_ENTRAR)
        )
        botao.click()

    def realizar_login(self, email, senha):
        self.preencher_email(email)
        self.preencher_senha(senha)
        self.clicar_entrar()

    def obter_mensagem_erro(self):
        elemento = self.wait.until(
            EC.visibility_of_element_located(self.MENSAGEM_ERRO)
        )
        return elemento.text
