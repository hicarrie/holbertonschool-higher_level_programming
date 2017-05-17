#!/usr/bin/python3
"""
Module that prints text with 2 new lines after ., ?, and :
"""


def text_indentation(text):
    """
    Function that prints text with 2 new lines after ., ?, and :
    """

    new_text = ""

    """Checks if text is a string"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    """Checks if delimiters are in the text"""
    if "." not in text and "?" not in text and ":" not in text:
        print("{}".format(text))
    else:
        new_text = text.replace(". ", ".")
        new_text = new_text.replace("? ", "?")
        new_text = new_text.replace(": ", ":")
        new_text = new_text.replace(".", ".\n\n")
        new_text = new_text.replace("?", "?\n\n")
        new_text = new_text.replace(":", ":\n\n")
        " ".join(new_text.split())
        print("{}".format(new_text), sep="", end="")
