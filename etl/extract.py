import requests

def extract_driver_data(url: str):
    """Función que extrae los datos de la API de los conductores."""
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()  # Retorna los datos en formato JSON
    else:
        raise Exception(f"Error al obtener datos: {response.status_code}")
