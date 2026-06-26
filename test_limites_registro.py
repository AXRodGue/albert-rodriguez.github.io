import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()

# Lista de comprobación de valores límites
@pytest.mark.parametrize("edad, deba_permitir", [
    (17, False),  # Límite inferior (Inválido)
    (18, True),   # Límite inferior (Válido)
    (65, True),   # Límite superior (Válido)
    (66, False)   # Límite superior (Inválido)
])
def test_limites_edad_registro(driver, edad, deba_permitir):
    driver.get("https://ejemplo-tech.com")
    
    campo_edad = driver.find_element(By.ID, "age-input")
    campo_edad.send_keys(str(edad))
    driver.find_element(By.ID, "btn-registrar").click()
    
    if deba_permitir:
        assert "Bienvenido" in driver.find_element(By.ID, "welcome-msg").text
    else:
        error_msg = driver.find_element(By.CLASS_NAME, "alert-danger").text
        assert "Edad no permitida" in error_msg
