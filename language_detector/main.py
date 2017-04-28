# -*- coding: utf-8 -*-

"""This is the entry point of the program."""

def detect_language(text, languages):
    """Returns the detected language of given text."""
    # implement your solution here
    words_in_dict = 0
    lang_match = ''

    for language in languages:
        words = len([word for word in language['common_words'] if word in text])
        if words > words_in_dict:
            words_in_dict = words
            lang_match = language['name']

    return lang_match