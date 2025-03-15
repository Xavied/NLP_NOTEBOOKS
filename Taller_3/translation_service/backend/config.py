# Maximum allowed characters for translation input
MAX_CHARACTERS = 255

# Flask application settings
DEBUG = True
HOST = "0.0.0.0"
PORT = 5555

# These keys are tuples (source_language, target_language).
SUPPORTED_TRANSLATIONS = {
    ("en", "es"): "Helsinki-NLP/opus-mt-en-es",
    ("es", "en"): "Helsinki-NLP/opus-mt-es-en",
    ("en", "fr"): "Helsinki-NLP/opus-mt-en-fr",
    ("fr", "en"): "Helsinki-NLP/opus-mt-fr-en",
    ("fr", "es"): "Helsinki-NLP/opus-mt-fr-es",
    ("es", "fr"): "Helsinki-NLP/opus-mt-es-fr"
}
