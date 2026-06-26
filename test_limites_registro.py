import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()

# Lista de comprobación de valores límites parametrizada en PyTest
@pytest.mark.parametrize("edad, deba_permitir", [
    (17, False),  # Justo abajo del límite inferior (Inválido)
    (18, True),   # Límite inferior exacto (Válido)
    (65, True),   # Límite superior exacto (Válido)
    (66, False)   # Justo arriba del límite superior (Inválido)
])
def test_limites_edad_registro(driver, edad, deba_permitir):
    driver.get("https://ejemplo-tech.com")
    
    # Llenar campo de edad
    campo_edad = driver.find_element(By.ID, "age-input")
    campo_edad.send_keys(str(edad))
    driver.find_element(By.ID, "btn-registrar").click()
    
    if deba_permitir:
        # Validación de datos: Registro exitoso
        assert "Bienvenido" in driver.find_element(By.ID, "welcome-msg").text
    else:
        # Validación de datos: Mensaje de restricción visible
        error_msg = driver.find_element(By.CLASS_NAME, "alert-danger").text
        assert "Edad no permitida" in error_msg
