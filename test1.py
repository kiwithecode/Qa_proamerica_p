from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException

# Especifica la ruta al Edge WebDriver
driver_path = r'C:\Users\KIWIRAZER\Downloads\edgedriver_win64\msedgedriver.exe'
service = Service(executable_path=driver_path)

# Configura el WebDriver para Edge
driver = webdriver.Edge(service=service)

# Inicializa la variable para rastrear el éxito de la prueba
prueba_exitosa = False

try:
    # Abre el sitio web
    driver.get('https://www.clubpromerica.com/costarica/')
    
    # Maximiza la ventana del navegador para asegurar que no esté minimizada ni recortada
    driver.maximize_window()
    
    # Espera hasta que el enlace "Contáctenos" sea interactuable y luego haz clic en él
    contact_link_xpath = "//a[@href='/costarica/contactus']"
    try:
        contact_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, contact_link_xpath))
        )
        contact_link.click()
        
        # Si llegamos aquí, la prueba se considera exitosa
        prueba_exitosa = True
        
    except TimeoutException:
        print("El enlace 'Contáctenos' no se cargó en el tiempo esperado.")
    except ElementNotInteractableException:
        
        contact_link = driver.find_element(By.XPATH, contact_link_xpath)
        driver.execute_script("arguments[0].click();", contact_link)
    
        # Consideramos exitosa la prueba si logramos hacer clic mediante JavaScript
        prueba_exitosa = True
   
except NoSuchElementException:
    print("Elemento no encontrado.")
except Exception as e:
    print(f"Se produjo un error: {e}")
finally:
    # Cierra el navegador después de una breve pausa para que puedas ver los resultados
    import time
    time.sleep(5)  # Espera 5 segundos
    driver.quit()
    
    # Imprime el mensaje final basado en el éxito de la prueba
    if prueba_exitosa:
        print("Prueba finalizada exitosamente.")
    else:
        print("Prueba no exitosa.")
