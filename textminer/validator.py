import re


def binary(text):
    binary = re.findall(r'[0-1]+', text)
    non_binary = re.findall(r'[2-9]', text)
    if len(non_binary) > 0:
        return False
    if len(binary) == 1:
        return True


def binary_even(text):
    binary = re.findall(r'[0-1]+', text)
    non_binary = re.findall(r'[2-9]', text)
    if len(non_binary) > 0:
        return False
    if len(binary) == 1 and text[-1] == "0":
        return True


def hex(text):
    hex_digits = re.findall(r'[0-9A-F]+', text)
    if (len(hex_digits) == len(text)) and len(text) != 0:
        return True
