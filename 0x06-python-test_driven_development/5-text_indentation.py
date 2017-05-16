#!/usr/bin/python3
def text_indentation(text):
    new_text = ""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if "." not in text and "?" not in text and ":" not in text:
        print("{}".format(text))
    else:
        new_text = text.replace(". ", ".\n\n")
        new_text = new_text.replace("? ", "?\n\n")
        new_text = new_text.replace(": ", ":\n\n")
        print("{}".format(new_text), sep="", end="")
