# TODO: File description

# Default alphabets 
lowercase = 'abcdefghijklmnopqrstuvwxyz'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def cipher_file(input_file, output_file=None, shift=13, 
                alphabets=[lowercase, uppercase]):
    """

    Parameters:
        input_file: str
            The
        output_file : str
            The name of the file to save the ciphered text in. If no filename
            is given, no file is generated.
         shift : int, optional
            The number of alphabet characters to shift forward by (default: 13).
        *alphabets : tuple(str)
            The alphabets we are shifting (default: 
            ['abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']).
    """
    #TODO

def cipher_string(text, shift=13, alphabets=[lowercase, uppercase]):
    """Caesar cipher of some text, with user-customizeable shift and characters.

    Takes a string and replaces each character    

    If only  

    The implementation of the translation table is taken from:
    https://www.tutorialspoint.com/python/string_maketrans.htm
 
    Parameters:
        text : str
            The text to shift.
        shift : int, optional
            The number of alphabet characters to shift forward by (default: 13).
        alphabets : list[str], optional
            The alphabets we are shifting (default: 
            ['abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']).

    Returns:
        str
            The ciphered text. 
    """
    original_alphabet = ''
    shifted_alphabet = ''

    for a in alphabets:
        original_alphabet = original_alphabet + a
        shifted_alphabet = shifted_alphabet + shift_alphabet(shift, a)
    
    translation_table = str.maketrans(original_alphabet, shifted_alphabet)

    return text.translate(translation_table)


def shift_alphabet(shift, alphabet):
    """Shifts an alphabet forward by a given number of characters. 

    Parameters:
        shift : int
            The number of alphabet characters to shift forward by (default: 13).
        alphabet : str
            The alphabet to shift.

    Returns:
        str
            The given alphabet shifted forward by n characters.
    """
    shifted_alphabet = ''
    start_code_point = ord(alphabet[0])
    length = len(alphabet)
    for char in alphabet:
        shifted_code_point = (((ord(char) - start_code_point + shift) % length) 
                             + start_code_point)
        shifted_alphabet = shifted_alphabet + chr(shifted_code_point)
    return shifted_alphabet

