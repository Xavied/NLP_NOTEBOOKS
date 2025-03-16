...
# Servicio Web de Traducción - Back-End

Este repositorio contiene el componente de back-end del Servicio Web de Traducción. Proporciona una API RESTful para traducir texto entre los idiomas 
soportados utilizando modelos pre-entrenados de Hugging Face.


## Características

- **Soporte Multilingüe::**  
  Soporta traducción entre inglés, español y francés.
  
- **Limitación de Caracteres::**  
Tanto el back-end como el front-end imponen un límite de 255 caracteres para los textos de entrada.

- **Config File:**  
  La configuración de la aplicación (por ejemplo, caracteres máximos, puerto, modelos soportados) se gestiona a través de 
  **config.py**.


- **Despliegue en Contenedores:**  
 Fácil de desplegar utilizando Docker y Docker Compose.

## Estructura del Proyecto

translation_service:

├── backend/                              # Back-end API code (Flask)
│   ├── app.py                            # Aplicación principal de Flask API (including /translate)
│   ├── requirements.txt                  # Python dependencies (Flask, transformers, etc.)
│   ├── config.py                         # Configuración: Caracteres max; Host, Port, Models Names for supported Translations
│   └── models/
|       └── translation_models.py         #Carga los modelos de traducción    
│
└── frontend/                             # Código de la aplicación de front-end (Interfaz de usuario)
    ├── index.hetml                       # Archivo HTML principal para la interfaz de usuario
    │           
    │
    └── src/
        ├── css/
        │   └── styles.css      #  # Archivo CSS para el estilo
        └── js/
            └── main.js         # Archivo JavaScript


## Instalación y Configuración BACKEND - FRONTEND

1. **CClonar el Repositorio:**

   bash git clone https://github.com/Xavied/NLP_NOTEBOOKS.git
   cd translation_service/backend

BACKEND:

2. **Create a Virtual Environment:**
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

3. **Install Dependencies:**
pip install -r requirements.txt

4. **Run the app**
python app.py
El API está disponible en: http://0.0.0.0:5555.   

FRONTEND:

cd frontend
''bash  python -m http.server 8080
La interfaz de ususario estará disponible en: https://localhost:8080