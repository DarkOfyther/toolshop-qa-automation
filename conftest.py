
import pytest
from pathlib import Path
from datetime import datetime
from selenium import webdriver


PASTA_SCREENSHOTS = Path(__file__).resolve().parent / "screenshots"


@pytest.fixture
def driver(request):
    navegador = webdriver.Chrome()
    navegador.maximize_window()

    PASTA_SCREENSHOTS.mkdir(exist_ok=True)

    yield navegador

    relatorio = getattr(request.node, "rep_call", None)

    if relatorio and relatorio.failed:
        pasta = PASTA_SCREENSHOTS / "falhas"
        pasta.mkdir(parents=True, exist_ok=True)

        horario = datetime.now().strftime("%Y%m%d_%H%M%S")
        caminho = pasta / f"{request.node.name}_{horario}.png"

        navegador.save_screenshot(str(caminho))
        print(f"\nEvidência da falha salva: {caminho}")

    navegador.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    resultado = yield
    relatorio = resultado.get_result()

    setattr(item, f"rep_{relatorio.when}", relatorio)


@pytest.fixture
def capturar_print(driver, request):

    def salvar(nome):
        pasta = PASTA_SCREENSHOTS / request.node.name
        pasta.mkdir(parents=True, exist_ok=True)

        caminho = pasta / f"{nome}.png"

        driver.save_screenshot(str(caminho))

        print(f"\nEvidência salva: {caminho}")

        return caminho

    return salvar
