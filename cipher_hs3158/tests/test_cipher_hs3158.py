from cipher_hs3158 import cipher_hs3158

import pytest

def cipher(text, shift, encrypt=True):
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


@pytest.mark.parametrize('example, expected',[
    ('hello', 'ifmmp')
])

def test_cipher(example, expected):
    result = cipher("hello", 1, True)
    assert result == expected