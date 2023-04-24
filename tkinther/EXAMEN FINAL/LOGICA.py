import tkinter as tk
from tkinter import messagebox
    
def arabe_romano(arabic_numeral):
    roman_dict = {1: 'I', 5: 'V', 10: 'X', 50: 'L'}
    roman_numeral = ''
    for arabic, roman in sorted(roman_dict.items(), reverse=True):
        while arabic_numeral >= arabic:
            roman_numeral += roman
            arabic_numeral -= arabic
    return roman_numeral


def romano_arabe(roman_numeral):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50}
    arabic_numeral = 0
    for i, c in enumerate(roman_numeral):
        if (i + 1) == len(roman_numeral) or roman_dict[c] >= roman_dict[roman_numeral[i + 1]]:
            arabic_numeral += roman_dict[c]
        else:
            arabic_numeral -= roman_dict[c]
    if arabe_romano(arabic_numeral) != roman_numeral:
        return None
    return arabic_numeral