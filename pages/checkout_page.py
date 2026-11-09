
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:

    BOTAO_PROSSEGUIR_1 = (
        By.CSS_SELECTOR, '[data-test="proceed-1"]'
    )

    BOTAO_PROSSEGUIR_2 = (
        By.CSS_SELECTOR, '[data-test="proceed-2"]'
    )

    MENSAGEM_LOGIN = (
        By.XPATH,
        "//p[contains(text(), 'you are already logged in')]"
    )

    CAMPO_EMAIL = (By.ID, "email")
    CAMPO_SENHA = (By.ID, "password")

    BOTAO_ENTRAR = (
        By.CSS_SELECTOR, '[data-test="login-submit"]'
    )

    CAMPO_PAIS = (By.ID, "country")
    CAMPO_CEP = (By.ID, "postal_code")
    CAMPO_NUMERO = (By.ID, "house_number")
    CAMPO_RUA = (By.ID, "street")
    CAMPO_CIDADE = (By.ID, "city")
    CAMPO_ESTADO = (By.ID, "state")

    BOTAO_PROSSEGUIR_3 = (
        By.CSS_SELECTOR, '[data-test="proceed-3"]'
    )

    CAMPO_PAGAMENTO = (By.ID, "payment-method")
    CAMPO_NOME_BANCO = (By.ID, "bank_name")
    CAMPO_NOME_CONTA = (By.ID, "account_name")
    CAMPO_NUMERO_CONTA = (By.ID, "account_number")

    BOTAO_FINALIZAR = (
        By.CSS_SELECTOR, '[data-test="finish"]'
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def clicar(self, seletor):
        botao = self.wait.until(
            EC.element_to_be_clickable(seletor)
        )
        botao.click()

    def preencher(self, seletor, valor):
        campo = self.wait.until(
            EC.visibility_of_element_located(seletor)
        )

        campo.clear()
        campo.send_keys(valor)

        self.wait.until(
            lambda driver: driver.find_element(
                *seletor
            ).get_attribute("value") == valor
        )

    def selecionar(self, seletor, valor):
        elemento = self.wait.until(
            EC.presence_of_element_located(seletor)
        )

        Select(elemento).select_by_value(valor)

        self.wait.until(
            lambda driver: Select(
                driver.find_element(*seletor)
            ).first_selected_option.get_attribute("value") == valor
        )

    def prosseguir_do_carrinho(self):
        self.clicar(self.BOTAO_PROSSEGUIR_1)

    def realizar_login(self):
        self.preencher(
            self.CAMPO_EMAIL,
            "customer@practicesoftwaretesting.com"
        )

        self.preencher(
            self.CAMPO_SENHA,
            "welcome01"
        )

        self.clicar(self.BOTAO_ENTRAR)

        self.wait.until(
            EC.visibility_of_element_located(
                self.MENSAGEM_LOGIN
            )
        )

        self.clicar(self.BOTAO_PROSSEGUIR_2)

    def preencher_endereco(self):

        # Primeira seleção de Azerbaijan
        self.selecionar(
            self.CAMPO_PAIS,
            "AZ"
        )

        # Primeiro preenchimento do CEP
        self.preencher(
            self.CAMPO_CEP,
            "09750000"
        )

        # Primeiro preenchimento do número
        self.preencher(
            self.CAMPO_NUMERO,
            "100"
        )

        # Aguarda 5 segundos
        time.sleep(5)

        # Segunda seleção de Azerbaijan
        self.selecionar(
            self.CAMPO_PAIS,
            "AZ"
        )

        # Segundo preenchimento do CEP
        self.preencher(
            self.CAMPO_CEP,
            "09750000"
        )

        # Segundo preenchimento do número
        self.preencher(
            self.CAMPO_NUMERO,
            "100"
        )

        # Clica em Proceed to checkout
        self.clicar(self.BOTAO_PROSSEGUIR_3)

    def selecionar_pagamento(self):
        self.selecionar(
            self.CAMPO_PAGAMENTO,
            "bank-transfer"
        )

    def finalizar_pagamento(self):

        # Preenche o nome do banco
        self.preencher(
            self.CAMPO_NOME_BANCO,
            "QA Test Bank"
        )

        # Preenche o nome da conta
        self.preencher(
            self.CAMPO_NOME_CONTA,
            "Teste QA"
        )

        # Preenche o número da conta
        self.preencher(
            self.CAMPO_NUMERO_CONTA,
            "123456789"
        )

        # Clica em Check payment
        self.clicar(self.BOTAO_FINALIZAR)
