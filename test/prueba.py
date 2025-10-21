import pytest
from utils.funciones import login_saucedemo, get_driver

@pytest.fixture

# configuracion de los drivers de selenium
def driver():
    driver = get_driver()
    yield driver


# abrir el navegador
# dirigirse a la pagina "saucedemo.com"
# ingresar usuario y contraseña
# validar login exitoso
def test_login ():


# hacer login en la pagina
# verificar el titulo de la pagina
# comprobar si hay productos visibles
def test_catalogo():


# hacer login en la pagina
# añadir un producto al carrito
# ingresar al carrito
# comprobar que el producto este en el carrito
def test_carrito ():