from google.cloud import translate_v2 as translate
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/jackiecisneros/Development/code/phase-3/phase-3-project-2/simple_bot_api.json"

'''list of all languages'''
# def list_languages():
#     """Lists all available languages."""
#     from google.cloud import translate_v2 as translate

#     translate_client = translate.Client()

#     results = translate_client.get_languages()

#     for language in results:
#         print(u"{name} ({language})".format(**language))
#list_languages()

'''Listing supported languages is target language.'''
# def list_languages_with_target(target):
#     """Lists all available languages and localizes them to the target language.

#     Target must be an ISO 639-1 language code.
#     See https://g.co/cloud/translate/v2/translate-reference#supported_languages
#     """
#     from google.cloud import translate_v2 as translate

#     translate_client = translate.Client()

#     results = translate_client.get_languages(target_language=target)

#     for language in results:
#         print(u"{name} ({language})".format(**language))
# list_languages_with_target('en')
