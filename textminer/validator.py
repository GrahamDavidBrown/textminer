import re


def binary(text):
    binary = re.findall(r'[0-1]+', text)
    non_binary = re.findall(r'[2-9A-Za-z]', text)
    if len(non_binary) > 0:
        return False
    if len(binary) == 1:
        return binary


def binary_even(text):
    binary = re.findall(r'[0-1]+', text)
    non_binary = re.findall(r'[2-9]', text)
    if len(non_binary) > 0:
        return False
    if len(binary) == 1 and text[-1] == "0":
        return binary


def hex(text):
    hex_digits = re.findall(r'[0-9a-fA-F]+', text)
    if (len(hex_digits) == 1) and len(text) > 0:
        return hex_digits


def word(text):
    word = re.findall(r'[A-Z-a-z]+', text)
    if len(word) == 1:
        return word


def words(text, count=None):
    words = re.findall(r'[1-9A-Z-a-z^\s!]+', text)
    print(words)
    words_str = ""
    if count and len(words) > count:
        counter = 0
        for word in words:
            if count > counter:
                words_str += word
                count += 1
            else:
                break
    else:
        for word in words:
            words_str += word
    return words_str
