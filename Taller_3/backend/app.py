################## PIPELINE #######################
from flask import Flask, request, jsonify
from flask_cors import CORS
from models.translation_models import load_translation_pipelines
from config import MAX_CHARACTERS, HOST, PORT

app = Flask(__name__)
CORS(app)

# Cargamos la traducción desde el archivo de configuración
translation_pipelines = load_translation_pipelines()

@app.route('/translate', methods=['POST'])
def translate():
    data = request.get_json()
    if not data or not all(k in data for k in ("text", "source", "target")):
        return jsonify({"error": "Json debería incluir 'text', 'idioma origen', e 'idioma destino'."}), 400
    
    text = data['text'].strip()
    source = data['source'].lower().strip()
    target = data['target'].lower().strip()

    # Validación de caracteres máximos
    if len(text) > MAX_CHARACTERS:
        return jsonify({"error": f"El texto ha escedido el límite. Máximo: {MAX_CHARACTERS} caracteres."}), 400

    # Pares de lenguajes validos
    if (source, target) not in translation_pipelines:
        return jsonify({"error": "Origen y Destino Incorrectos. Solo se puede traducir los siguientes pares: en-es, es-en, en-fr, fr-en."}), 400

    try:
        translator = translation_pipelines[(source, target)]
        result = translator(text)
        translated_text = result[0]['translation_text']
        return jsonify({"translated_text": translated_text})
    except Exception as e:
        return jsonify({"error": f"La traducción ha fallado: {str(e)}"}), 500

@app.route("/")
def home():
    return "Translation API is up and running!"

if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=True)

##################### MARIANMT ############################
# from flask import Flask, request, jsonify
# from flask_cors import CORS
# from models.translation_models import load_models, translate_text
# from config import MAX_CHARACTERS, HOST, PORT

# app = Flask(__name__)
# CORS(app)

# # Load models once when the application starts
# models_dict = load_models()

# @app.route('/translate', methods=['POST'])
# def translate():
#     data = request.get_json()
#     if not data or not all(k in data for k in ("text", "source", "target")):
#         return jsonify({"error": "JSON must include 'text', 'source', and 'target' keys."}), 400

#     text = data['text'].strip()
#     source = data['source'].lower().strip()
#     target = data['target'].lower().strip()

#     if len(text) > MAX_CHARACTERS:
#         return jsonify({"error": f"Text exceeds the {MAX_CHARACTERS}-character limit."}), 400

#     if (source, target) not in models_dict:
#         return jsonify({"error": "Unsupported language pair."}), 400

#     try:
#         translated_text = translate_text(text, source, target, models_dict)
#         return jsonify({"translated_text": translated_text})
#     except Exception as e:
#         return jsonify({"error": f"Translation failed: {str(e)}"}), 500

# @app.route("/")
# def home():
#     return "LA API DE TRADUCCIÓN ESTÁ EN LINEA!"

# if __name__ == '__main__':
#     app.run(host=HOST, port=PORT, debug=True)


### PRUEBA ESPAÑOL A INGLÉS MARIAN MT
#El siguiente texto está siendo traducido utilizando MARIAN MT en vez de Pipeline de "Hugging Face". Esto lo hacemos para ver cómo varia la traducción utilizando ambos esquemas, podrías encontrarnos que, efectivamente estamos traduciendolo de mejor manera.
#The following text is being translated using MARIAN MT instead of Pipeline of "Hugging Face". This we do to see how the translation varies using both schemas, you could find us that we are effectively translating it better.
#GOOGLE TRANSLATE: The following text is being translated using MARIAN MT instead of the "Hugging Face" Pipeline. We do this to see how the translation varies using both schemes, you might find that we are actually translating it better.
#CHATGPT: The following text is being translated using MARIAN MT instead of the "Hugging Face" Pipeline. We do this to see how the translation varies using both approaches; you might find that, in fact, we are translating it better.

