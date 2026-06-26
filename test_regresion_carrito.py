import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()

@pytest.mark.regression
def test_regresion_calculo_total_carrito(driver):
    driver.get("https://ejemplo-tech.com")
    
    # 1. Agregar Producto 1 (Precio simulado en UI: $10.00)
    driver.find_element(By.ID, "add-item-1").click()
    # 2. Agregar Producto 2 (Precio simulado en UI: $20.00)
    driver.find_element(By.ID, "add-item-2").click()
    
    # Ir al Carrito
    driver.find_element(By.ID, "ver-carrito").click()
    
    # 3. Validación de Datos (Extracción y Conversión)
    txt_subtotal = driver.find_element(By.ID, "subtotal-val").text  # Ejemplo: "$30.00"
    txt_envio = driver.find_element(By.ID, "envio-val").text        # Ejemplo: "$5.00"
    txt_total = driver.find_element(By.ID, "total-val").text        # Ejemplo: "$35.00"
    
    # Limpieza y conversión de strings a números para validar operaciones matemáticas
    subtotal = float(txt_subtotal.replace("$", ""))
    envio = float(txt_envio.replace("$", ""))
    total_esperado = subtotal + envio
    total_real = float(txt_total.replace("$", ""))
    
    # Aserción de regresión matemática
    assert total_real == total_esperado, f"Error en regresión: El total calculado ({total_real}) no coincide con la suma ({total_esperado})."
