from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Especifica la ruta al Edge WebDriver
driver_path = r'C:\Users\KIWIRAZER\Downloads\edgedriver_win64\msedgedriver.exe'
service = Service(executable_path=driver_path)

# Configura el WebDriver para Edge
driver = webdriver.Edge(service=service)
driver.maximize_window()  # Maximiza la ventana del navegador

try:
    # Abre la página de contacto
    driver.get('https://www.clubpromerica.com/costarica/contactus')

    # Rellena el formulario
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "FullName"))).send_keys("Tu Nombre")
    driver.find_element(By.ID, "Email").send_keys("tucorreo@example.com")
    driver.find_element(By.ID, "Enquiry").send_keys("Este es un mensaje de prueba.")
    
    # Envía el formulario
    driver.find_element(By.NAME, "send-email").click()
    
    # Verifica si la página de destino contiene un mensaje de éxito
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".result"))
    )
    print("Mensaje de éxito encontrado.")
    
except TimeoutException:
    print("Mensaje de éxito no encontrado.")
except Exception as e:
    print(f"Se produjo un error: {e}")
finally:
    # Cierra el navegador después de una breve pausa para que puedas ver los resultados
    import time
    time.sleep(5)  # Espera 5 segundos
    driver.quit()
