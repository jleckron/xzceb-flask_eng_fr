"Translates between English and French."

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url(url)
# languages = language_translator.list_languages().get_result()

def english_to_french(english_text):
    "Translate given english test to french."
    french_text = language_translator.translate(
        text=english_text,
        model_id="en-fr").get_result()['translations'][0]
    return french_text['translation']

def french_to_english(french_text):
    "Translate given french text to english."
    english_text = language_translator.translate(
        text=french_text,
        model_id="fr-en").get_result()['translations'][0]
    return english_text ['translation']
