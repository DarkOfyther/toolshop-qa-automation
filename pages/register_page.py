
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RegisterPage:

    URL = "https://practicesoftwaretesting.com/auth/register"

    BOTAO_CADASTRAR = (By.CSS_SELECTOR, '[data-test="register-submit"]')
    MENSAGEM_DATA_OBRIGATORIA = (
        By.XPATH,
        "//*[contains(text(), 'Date of Birth is required')]"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def abrir(self):
        self.driver.get(self.URL)

    def clicar_cadastrar(self):
        botao = self.wait.until(
            EC.element_to_be_clickable(self.BOTAO_CADASTRAR)
        )
        botao.click()

    def obter_mensagem_data_obrigatoria(self):
        elemento = self.wait.until(
            EC.visibility_of_element_located(
                self.MENSAGEM_DATA_OBRIGATORIA
            )
        )
        return elemento.text
