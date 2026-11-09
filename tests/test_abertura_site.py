def test_abrir_site(driver):
    driver.get("https://practicesoftwaretesting.com/")

    assert "Practice Software Testing" in driver.title