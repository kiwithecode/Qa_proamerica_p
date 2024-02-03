from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Configura el WebDriver para Edge
driver_path = r'C:\Users\KIWIRAZER\Downloads\edgedriver_win64\msedgedriver.exe'
service = Service(executable_path=driver_path)
driver = webdriver.Edge(service=service)
driver.maximize_window()

# Navega a la sección "Promociones y Descuentos"
driver.get('https://www.clubpromerica.com/costarica/promociones-y-descuentos')

# Lista de las secciones a verificar
secciones = [
    ("/costarica/sabores-3", "Restaurantes"),
    ("/costarica/compras", "Compras"),
    ("/costarica/estilo-de-vida", "Estilo de Vida"),
    ("/costarica/viajes-8", "Viajes")
]

# Itera por cada sección para realizar la verificación
for seccion in secciones:
    try:
        # Navega a la sección
        driver.get(f'https://www.clubpromerica.com{seccion[0]}')
        
        # Espera y verifica que el título de la sección sea visible
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, f"//h1[contains(text(), '{seccion[1]}')]"))
        )
        print(f"Sección '{seccion[1]}' verificada con éxito.")
    except TimeoutException:
        print(f"La sección '{seccion[1]}' no se verificó correctamente.")
    except Exception as e:
        print(f"Se produjo un error al verificar la sección '{seccion[1]}': {e}")

# Cierra el navegador después de completar las verificaciones
driver.quit()
