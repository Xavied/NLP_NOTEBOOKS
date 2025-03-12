...
# Translation Web Service - Back-End

This repository contains the back-end component of the Translation Web Service. It provides a RESTful API for translating text between supported languages using pre-trained Hugging Face models.

## Features

- **Multi-language Support:**  
  Supports translation between English, Spanish, and French.
  
- **Character Limit Enforcement:**  
  Both the back-end and front-end enforce a 250-character limit for input texts.
  
- **Configurable:**  
  Application settings (e.g., max characters, port, supported models) are managed via `config.py`.

- **Containerized Deployment:**  
  Easily deployable using Docker and Docker Compose.

## Project Structure

translation_service/
├── docker-compose.yml          #  Multi-container orchestration file
├── Dockerfile.backend          # Dockerfile for building the Flask back-end container
├── Dockerfile.frontend         # Dockerfile for building the front-end container (e.g., using Nginx)
├── README.md                   # Project documentation
├── .gitignore                  # Git ignore file

├── backend/                    # Back-end API code (Flask)
│   ├── app.py                  # Main Flask application and API endpoints (including /translate)
│   ├── requirements.txt        # Python dependencies (Flask, transformers, etc.)
│   ├── config.py               # Configuration settings (e.g., port, character limits)
│   └── models/                 # (Optional) Subfolder for model management if you add more models
│
└── frontend/                   # Front-end application code (UI)
    ├── public/
    │   └── index.html          # Main HTML file for the user interface
    │
    └── src/
        ├── css/
        │   └── styles.css      # CSS file for styling (using neon blue and black palette)
        └── js/
            └── main.js         # JavaScript file to handle tab switching, input validation (250-character limit), and API calls


## Setup and Installation

1. **Clone the Repository:**
   ```bash
   git clone ...
   cd translation_service/backend

2. **Create a Virtual Environment:**
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

3. **Install Dependencies:**
pip install -r requirements.txt

4. **Run the app**
python app.py
The API will be available at http://0.0.0.0:5555.   