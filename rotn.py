# rot(n)
#
# Takes a string and substitutes each letter with the nth letter after it.
# 
# For more information, see: https://en.wikipedia.org/wiki/ROT13

import string 

def rotn(s, n=13, *alphabets):
    ''' Shifts characters ahead in the alphabet by a certain amount.
    
    Uses ord() to get the Unicode code point (in decimal) of characters, 
    determines the code point of the replacement, and uses chr() to get the 
    replacement. 
    For more information on Unicode code points, see:
    https://en.wikipedia.org/wiki/List_of_Unicode_characters#Basic_Latin

    The implementation of the translation table is taken from:
    https://www.tutorialspoint.com/python/string_maketrans.htm

    Args:
        s : str
            the characters to shift
        n : int, optional
            the number of alphabet letters to shift forward by (default: 13)
        *charsets : tuple(str)
            the character sets we are shifting (default is 
            ('abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    Returns:
        str
    '''

    if not alphabets:
        alphabets = (string.ascii_lowercase, string.ascii_uppercase)

    intab = ''
    outtab = ''
    
    for a in alphabets:
        intab = intab + a

    for a in alphabets:
        outtab = outtab + outtab_gen(n, cs)
    
    trantab = str.maketrans(intab, outtab)

    return s.translate(trantab)


def outtab_gen(n, alphabet):
    '''
    Uses modular arithmetic to determine the result of shifting the given 
    character set by n points.

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
    shifted_charset = ''
    floor = ord(charset[0]) # code point of the first character in the set
    length = len(charset)
    for c in charset:
        i = ((ord(c) - floor + n) % length) + floor
        shifted_charset = shifted_charset + chr(i)
    return shifted_charset
