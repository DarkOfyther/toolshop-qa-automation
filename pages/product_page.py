from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage:

    URL = "https://practicesoftwaretesting.com/product/01M70M1ZC1QT4C590D2JF44H4V"

    CAMPO_QUANTIDADE = (By.ID, "quantity-input")

    BOTAO_ADICIONAR_CARRINHO = (
        By.CSS_SELECTOR,
        '[data-test="add-to-cart"]'
    )

    CONTADOR_CARRINHO = (
        By.CSS_SELECTOR,
        '[data-test="cart-quantity"]'
    )

    MENSAGEM_LIMITE = (
        By.CSS_SELECTOR,
        '[role="alert"]'
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def abrir(self):
        self.driver.get(self.URL)

    def informar_quantidade(self, quantidade):
        campo = self.wait.until(
            EC.visibility_of_element_located(self.CAMPO_QUANTIDADE)
        )

        campo.clear()
        campo.send_keys(str(quantidade))
        campo.send_keys(Keys.TAB)

    def obter_quantidade(self):
        campo = self.wait.until(
            EC.visibility_of_element_located(self.CAMPO_QUANTIDADE)
        )

        return campo.get_attribute("value")

    def obter_contador_carrinho(self):
        elementos = self.driver.find_elements(
            *self.CONTADOR_CARRINHO
        )

        if not elementos:
            return 0

        return int(elementos[0].text)

    def adicionar_ao_carrinho(self):
        contador_anterior = self.obter_contador_carrinho()

        botao = self.wait.until(
            EC.element_to_be_clickable(
                self.BOTAO_ADICIONAR_CARRINHO
            )
        )

        botao.click()

        self.wait.until(
            lambda driver: (
                self.obter_contador_carrinho()
                > contador_anterior
            )
        )

        return contador_anterior

    def obter_mensagem_limite(self):
        elemento = self.wait.until(
            lambda driver: next(
                (
                    alerta
                    for alerta in driver.find_elements(
                        *self.MENSAGEM_LIMITE
                    )
                    if "You can order at most 99"
                    in alerta.text
                ),
                False
            )
        )

        return elemento.text