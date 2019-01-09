# rot(n)
#
# Takes a string and substitutes each letter with the nth letter after it.
# 
# For more information, see: https://en.wikipedia.org/wiki/ROT13

import string 

def caesar_cipher(text, n=13, *alphabets):
    ''' Generalized Caesar cipher of some text.

    The "Caesar cipher" is a basic encryption method where each letter in a text
    is replaced by nth letter after it in the alphabet. (In another sense, this 
    "shifts" all the letters down the alphabet.) If there are fewer than n 
    letters left in the alphabet, the counting continues at the start of the 
    alphabet.

    The most popular form of the Caesar cipher, known as "ROT-13",
    replaces each letter with the 13th letter after it. So the ROT-13 of the 
    1st letter 'A' is the 14th letter 'N', the ROT-13 of 'B' is 'O', and so on.
    With fewer than 13 letters left in the alphabet, the counting continues 
    at 'A'. So the ROT-13 of the 25th letter 'Y' is the 12th letter 'L', and the
    ROT-13 of the 26th letter 'Z' is the 13th letter 'M'.

    This is a "generalized" Caesar cipher because it supports Unicode, instead 
    of just ASCII or the Latin alphabet.
    
    Uses ord() to get the Unicode code point (in decimal) of characters, 
    determines the code point of the replacement, and uses chr() to get the 
    replacement. 
    For more information on Unicode code points, see:
    https://en.wikipedia.org/wiki/List_of_Unicode_characters#Basic_Latin

    The implementation of the translation table is taken from:
    https://www.tutorialspoint.com/python/string_maketrans.htm

    Args:
        text : str
            the text to shift
        n : int, optional
            the number of alphabet characters to shift forward by (default: 13)
        *alphabets : tuple(str)
            the alphabets we are shifting (default is 
            ('abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    Returns:
        str
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
    '''Creates the  

    Each Unicode character has a corresponding "code point", given by ord(). 
    We use this code point and n to determine the resultant shifted character.

    For example, consider the charset 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'. 
    The code points of the first character 'A" and the last character 'Z' are 
    ord('A') == 65 and ord('Z') == 90. 
    To shift a character c by n places we must "loop back" to 65, the beginning 
    of the alphabet. This is accomplished by treating the code point of the
    first character as 0, 

    n: Integer, the number of characters to shift by
    charset: String, the character set to shift

    Integer, String -> String
    '''
    shifted_alphabet = ''
    first_code_point = ord(alphabet[0])
    length = len(alphabet)
    for char in alphabet:
        shifted_code_point = (((ord(char) - first_code_point + n) % length) 
                             + first_code_point)
        shifted_alphabet = shifted_alphabet + chr(shifted_code_point)
    return shifted_alphabet