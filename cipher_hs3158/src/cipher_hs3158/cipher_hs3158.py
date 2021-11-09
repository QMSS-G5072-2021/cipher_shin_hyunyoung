import pandas as pd

def cipher(text, shift, encrypt=True):
    """
    Each letter in the plain text is replaced by another letter at some fixed positions from the current letter in the alphabet.
    
    Prameters
    ---------
    text : string that you want to encrypt or decrypt
    shift: the number of positions the letter want to move to
    encrypt: True if you want to encrypt the string and False if you want to decrypt it.
    
    Returns
    -------
    Newly replaced string
    
    Examples
    --------
    Input: cipher('hello', 1, True)
    Output: 'ifmmp'
    
    Input: cipher('hello', 1, False)
    Output: 'gdkkn'
    
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text
