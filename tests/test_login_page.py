
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage


def test_login_valido(driver):
    login = LoginPage(driver)

    login.abrir()

    login.realizar_login(
        "customer@practicesoftwaretesting.com",
        "welcome01"
    )

    WebDriverWait(driver, 15).until(
        EC.url_contains("/account")
    )

    titulo = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//h1[normalize-space()='My account']")
        )
    )

    assert titulo.is_displayed()


def test_login_senha_incorreta(driver):
    login = LoginPage(driver)

    login.abrir()

    login.realizar_login(
        "customer@practicesoftwaretesting.com",
        "senhaerrada123"
    )

    mensagem = login.obter_mensagem_erro()

    assert mensagem == "Invalid email or password"
    assert "/auth/login" in driver.current_url
