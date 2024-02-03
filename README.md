# Documentación de Scripts de Automatización Selenium para Club Promerica Costa Rica

## Pre-requisitos

- Python 3.6 o superior
- pip (gestor de paquetes de Python)
- virtualenv

## Instalación de Selenium

1. Crea un entorno virtual para gestionar las dependencias del proyecto:
   ```bash
   python -m venv myvenv
   ```
2. Activa el entorno virtual:
   - En Windows:
     ```bash
     myvenv\Scripts\activate
     ```
   - En macOS/Linux:
     ```bash
     source myvenv/bin/activate
     ```
3. Instala Selenium dentro del entorno virtual:
   ```bash
   pip install -U selenium
   ```

## Descarga y Configuración del WebDriver

Este proyecto utiliza Microsoft Edge WebDriver. Sigue estos pasos para configurarlo:

1. Descarga la versión del Microsoft Edge WebDriver que corresponda con tu versión de Microsoft Edge desde [este enlace](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/).
2. Extrae el archivo descargado y coloca el `msedgedriver.exe` en una carpeta de tu elección.
3. Asegúrate de actualizar la ruta del WebDriver en cada script de prueba (`test1.py`, `test2.py`, `test3.py`) a la ubicación donde hayas colocado el `msedgedriver.exe`.

   Por ejemplo, cambia la línea:

   ```python
   driver_path = r'C:\Users\KIWIRAZER\Downloads\edgedriver_win64\msedgedriver.exe'
   ```

   Por la ruta donde tienes el WebDriver en tu PC.

## Ejecución de los Scripts

Para ejecutar los scripts de prueba, asegúrate de que tu entorno virtual esté activado y ejecuta:

```bash
python test1.py
python test2.py
python test3.py
```

Reemplaza `test1.py`, `test2.py`, y `test3.py` con el nombre de archivo correcto si es diferente.

## Información Adicional

- Desarrollado con Python 3.8 y Selenium 3.141.0.
- Microsoft Edge WebDriver versión 90.0 (Asegúrate de usar la versión correcta para tu navegador).
- Para cualquier consulta adicional o problemas, por favor revisa la documentación oficial de Selenium o contacta al equipo de soporte.
