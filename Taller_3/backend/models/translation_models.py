########################### PIPELINES ###########################
#
#from transformers import pipeline
#from config import SUPPORTED_TRANSLATIONS


# def load_translation_pipelines():
#     """
#     Load translation pipelines for all supported language pairs.
#     Returns:
#         dict: A dictionary mapping language pair tuples (source, target) to their translation pipeline.
#     """
#     pipelines = {}
#     for (source, target), model_name in SUPPORTED_TRANSLATIONS.items():
#         # Construct the task name dynamically based on source and target
#         task = f"translation_{source}_to_{target}"
#         pipelines[(source, target)] = pipeline(task, model=model_name)
#     return pipelines

# if __name__ == "__main__":
#     # Test loading the translation pipelines
#     pipelines = load_translation_pipelines()
#     print("Loaded translation pipelines:")
#     for pair, pipe in pipelines.items():
#         print(f"{pair}: {pipe}")


########################### MARIANMT ###########################

from transformers import MarianMTModel, AutoTokenizer
from config import SUPPORTED_TRANSLATIONS

def load_models():
    """
    Loads MarianMT models and tokenizers for all supported language pairs.
    Returns:
        dict: A dictionary mapping (source, target) tuples to a tuple (model, tokenizer).
    """
    models_dict = {}
    for (source, target), model_name in SUPPORTED_TRANSLATIONS.items():
        model = MarianMTModel.from_pretrained(model_name)
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        models_dict[(source, target)] = (model, tokenizer)
    return models_dict

def translate_text(text, source, target, models_dict):
    """
    Translates the given text from the source to target language using the specified model.
    Args:
        text (str): The text to translate.
        source (str): The source language code.
        target (str): The target language code.
        models_dict (dict): Dictionary of loaded models and tokenizers.
    Returns:
        str: The translated text.
    Raises:
        ValueError: If the language pair is not supported.
    """
    key = (source, target)
    if key not in models_dict:
        raise ValueError("Unsupported language pair.")
    
    model, tokenizer = models_dict[key]
    batch = tokenizer([text], return_tensors="pt")
    generated_ids = model.generate(**batch)
    translation = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
    return translation

if __name__ == "__main__":
    models_dict = load_models()
    sample_text = "où est l'arrêt de bus ?"
    translation = translate_text(sample_text, "fr", "en", models_dict)
    print("Translation:", translation)
