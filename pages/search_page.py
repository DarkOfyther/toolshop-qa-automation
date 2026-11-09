
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SearchPage:

    URL = "https://practicesoftwaretesting.com/"

    CAMPO_PESQUISA = (By.ID, "search-query")
    NOME_PRODUTO = (By.CSS_SELECTOR, '[data-test="product-name"]')

    MENSAGEM_RESULTADO = (
        By.CSS_SELECTOR,
        '[data-test="search-result-count"]'
    )

    SLIDER_MIN = (
        By.CSS_SELECTOR,
        ".ngx-slider-pointer-min"
    )

    SLIDER_MAX = (
        By.CSS_SELECTOR,
        ".ngx-slider-pointer-max"
    )

    PRECO_PRODUTO = (
        By.CSS_SELECTOR,
        '[data-test="product-price"]'
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def abrir(self):
        self.driver.get(self.URL)

    def pesquisar_produto(self, produto):
        campo = self.wait.until(
            EC.visibility_of_element_located(self.CAMPO_PESQUISA)
        )

        campo.clear()
        campo.send_keys(produto)
        campo.submit()

    def obter_nome_produto(self):
        elemento = self.wait.until(
            EC.visibility_of_element_located(self.NOME_PRODUTO)
        )

        return elemento

    def obter_mensagem_resultado(self):
        elemento = self.wait.until(
            lambda driver: (
                elemento
                if (
                    elemento := driver.find_element(
                        *self.MENSAGEM_RESULTADO
                    )
                ).text.startswith("0 products found")
                else False
            )
        )

        return elemento.text

    def ajustar_slider(self, seletor, valor):
        elemento = self.wait.until(
            EC.element_to_be_clickable(seletor)
        )

        elemento.click()
        elemento.send_keys(Keys.HOME)

        valor_atual = int(
            self.driver.find_element(*seletor)
            .get_attribute("aria-valuenow")
        )

        while valor_atual != valor:

            elemento = self.driver.find_element(*seletor)

            if valor_atual < valor:
                elemento.send_keys(Keys.ARROW_RIGHT)
            else:
                elemento.send_keys(Keys.ARROW_LEFT)

            self.wait.until(
                lambda driver: int(
                    driver.find_element(*seletor)
                    .get_attribute("aria-valuenow")
                ) != valor_atual
            )

            valor_atual = int(
                self.driver.find_element(*seletor)
                .get_attribute("aria-valuenow")
            )

        print(
            f"\nSlider: {seletor[1]} | "
            f"Valor selecionado: {valor_atual}"
        )

    def filtrar_por_preco(self, minimo, maximo):
        self.ajustar_slider(self.SLIDER_MAX, maximo)
        self.ajustar_slider(self.SLIDER_MIN, minimo)

        self.wait.until(
            lambda driver: (
                len(driver.find_elements(*self.PRECO_PRODUTO)) > 0
                and all(
                    minimo <= float(
                        elemento.text.replace("$", "").strip()
                    ) <= maximo
                    for elemento in driver.find_elements(
                        *self.PRECO_PRODUTO
                    )
                )
            )
        )

    def obter_precos_produtos(self):
        self.wait.until(
            lambda driver: len(
                driver.find_elements(*self.PRECO_PRODUTO)
            ) > 0
        )

        return self.driver.execute_script("""
            return Array.from(
                document.querySelectorAll('[data-test="product-price"]')
            ).map(elemento =>
                parseFloat(
                    elemento.textContent.replace('$', '').trim()
                )
            );
        """)
