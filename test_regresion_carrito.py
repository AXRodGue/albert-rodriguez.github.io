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
    
    # Agregar Producto
    driver.find_element(By.ID, "add-item-1").click()
    driver.find_element(By.ID, "add-item-2").click()
    
    driver.find_element(By.ID, "ver-carrito").click()
    
    txt_subtotal = driver.find_element(By.ID, "subtotal-val").text 
    txt_envio = driver.find_element(By.ID, "envio-val").text        
    txt_total = driver.find_element(By.ID, "total-val").text        
    
    subtotal = float(txt_subtotal.replace("$", ""))
    envio = float(txt_envio.replace("$", ""))
    total_esperado = subtotal + envio
    total_real = float(txt_total.replace("$", ""))
    
    assert total_real == total_esperado, f"Error en regresión: El total calculado ({total_real}) no coincide con la suma ({total_esperado})."
