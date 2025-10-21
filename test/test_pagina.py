import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from selenium.webdriver.common.by import By
from utils.funciones import login_saucedemo, get_driver


@pytest.fixture

# configuracion de los drivers de selenium
def driver():
    driver = get_driver()
    yield driver
    driver.quit()


# abrir el navegador
# dirigirse a la pagina "saucedemo.com"
# ingresar usuario y contraseña
# validar login exitoso
def test_login (driver):
    login_saucedemo(driver)
    assert "/inventory.html" in driver.current_url
    titulo = driver.find_element(By.CSS_SELECTOR, 'div.header_secondary_container .title').text
    assert titulo == 'Products'
    logo = driver.find_element(By.CLASS_NAME, 'app_logo').text
    assert logo == 'Swag Labs'

# hacer login en la pagina
# verificar el titulo de la pagina
# comprobar si hay productos visibles
def test_catalogo(driver):
    login_saucedemo(driver)
    products = driver.find_elements(By.CLASS_NAME, 'inventory_list')
    assert len(products) > 0


# hacer login en la pagina
# añadir un producto al carrito
# ingresar al carrito
# comprobar que el producto este en el carrito
def test_carrito(driver):
    login_saucedemo(driver)
    products = driver.find_elements(By.CLASS_NAME, 'inventory_list')
    total_products = len(products)

    if total_products >= 2:
        products[0].find_element(By.TAG_NAME, 'button').click()
        products[1].find_element(By.TAG_NAME, 'button').click()

        badge = driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').text
        assert badge == "2"