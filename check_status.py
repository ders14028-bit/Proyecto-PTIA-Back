import requests
import time

# Esperar un poco para que el servidor inicie
time.sleep(2)

try:
    response = requests.get("http://localhost:8000/health")
    print("✓ API está respondiendo!")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")
except requests.exceptions.ConnectionError:
    print("⏳ El servidor aún se está iniciando...")
    print("⏳ Por favor espera 2-3 minutos mientras carga el modelo BERT")
except Exception as e:
    print(f"Error: {e}")
