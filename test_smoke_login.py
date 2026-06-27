import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.implicitly_wait(3)
    yield browser
    browser.quit()

def test_smoke_login_exitoso(driver):
    driver.get("https://ejemplo-tech.com")
    driver.find_element(By.ID, "username").send_keys("usuario_qa")
    driver.find_element(By.ID, "password").send_keys("Password123!")
    driver.find_element(By.ID, "btn-submit").click()
    
    assert "dashboard" in driver.current_url

def test_login_invalido_muestra_error(driver):
    driver.get("https://ejemplo-tech.com")
    driver.find_element(By.ID, "username").send_keys("usuario_falso")
    driver.find_element(By.ID, "password").send_keys("WrongPass")
    driver.find_element(By.ID, "btn-submit").click()
    
    error_texto = driver.find_element(By.ID, "error-message").text
    assert error_texto == "Credenciales incorrectas. Intente de nuevo."
