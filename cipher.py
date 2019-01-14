import string 

def caesar_cipher(text, n=13, *alphabets):
    '''Caesar cipher of some text.
    
    Uses ord() to get the Unicode code point (in decimal) of characters, 
    determines the code point of the replacement, and uses chr() to get the 
    replacement. 

    The implementation of the translation table is taken from:
    https://www.tutorialspoint.com/python/string_maketrans.htm

    Parameters:
        text : str
            The text to shift.
        n : int, optional
            The number of alphabet characters to shift forward by (default: 13).
        *alphabets : tuple(str)
            The alphabets we are shifting (default is 
            ('abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')).

    Returns:
        str
            The ciphered text. 
    '''

    if not alphabets:
        alphabets = (string.ascii_lowercase, string.ascii_uppercase)

    in_table = ''
    out_table = ''

    for a in alphabets:
        in_table = in_table + a
        out_table = out_table + out_table_gen(n, a)
    
    translation_table = str.maketrans(in_table, out_table)

    return s.translate(translation_table)


def out_table_gen(n, alphabet):
    '''Shifts an alphabet forward by n characters. 

    Parameters:
        n : int
            The number of alphabet characters to shift forward by (default: 13).
        alphabet : str
            The alphabet to shift.

    Returns:
        str
            Alphabet shifted forward by n characters.
    '''
    shifted_alphabet = ''
    first_code_point = ord(alphabet[0])
    length = len(alphabet)
    for char in alphabet:
        shifted_code_point = (((ord(char) - first_code_point + n) % length) 
                             + first_code_point)
        shifted_alphabet = shifted_alphabet + chr(shifted_code_point)
    return shifted_alphabet
