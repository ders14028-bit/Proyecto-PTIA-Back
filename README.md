# Sentiment Analysis API

API REST que analiza el sentimiento de textos (positivo, negativo, neutro) usando el modelo BERT multilingüe de HuggingFace.

---

## Requisitos del Sistema

- **Python 3.11** (no compatible con Python 3.12, 3.13 o 3.14)
- **RAM:** mínimo 4 GB
- **Disco:** mínimo 3 GB libres (torch ~192MB + modelo BERT ~500MB)
- **Conexión a internet** (para descargar el modelo la primera vez)

Descarga Python 3.11 aquí: https://www.python.org/downloads/release/python-3119/
> Durante la instalación marca **"Add Python to PATH"**

---

## Instalación y Ejecución

**1. Crear el entorno virtual con Python 3.11**
```bash
py -3.11 -m venv venv311
```

**2. Activar el entorno virtual**
```bash
venv311\Scripts\activate
```

**3. Instalar dependencias**
```bash
pip install fastapi==0.104.1 uvicorn==0.24.0 transformers==4.35.2 torch==2.1.1 python-dotenv==1.0.0 pydantic==2.5.0 requests==2.31.0 python-multipart==0.0.6 numpy==1.24.3
```

**4. Correr el servidor**
```bash
python main.py
```
