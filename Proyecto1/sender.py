import requests

# URL del servidor HTTP (donde corre Flask)
SERVER_URL = "http://127.0.0.1:5000/api/sensor_data"  # localhost y puerto por defecto de Flask

# Datos simulados (formato JSON: {"humidity": float, "temperature": float, "n": float, "p": float, "k": float})
data = {
    "humidity": 45.5,
    "temperature": 25.3,
    "n": 120.0,
    "p": 80.5,
    "k": 150.2
}

# Enviar el mensaje al servidor via HTTP POST
response = requests.post(SERVER_URL, json=data)

if response.status_code == 200:
    print(f"Datos enviados exitosamente: {data}")
    print(f"Respuesta del servidor: {response.json()}")
else:
    print(f"Error al enviar datos: {response.status_code} - {response.text}")
