# caesar-cipher
Python script to encrypt text via a Caesar cipher using arbitrary Unicode blocks.  
*Warning: It should go without saying that this is NOT a secure encryption method.*

# Introduction
The Caesar cipher<sup>[[1]](#ref-caesar-cipher)</sup> 
is a basic encryption method where each letter in a text is replaced by the nth letter 
after it in the alphabet.
If there are fewer than n letters left in the alphabet, 
the counting continues at the start of the alphabet (see [Examples](#examples)).

# Usage
This implementation supports using *any* 
Unicode block<sup>[[2]](#ref-unicode-block)</sup>
as the "alphabet" (see [Unicode Support](#unicode-support)).

# Implementation
The cipher is done using
modular arithmetic<sup>[[3]](#ref-modular-arithmetic)</sup>,
where we set A = 0, B = 1, ... Y = 25, and Z = 25.
Then the Caesar cipher of a character with position `i` shifted by `n`
is given by:
`(i + n) mod 26`

<a name="unicode-support"></a>
## Unicode Support
This is most easily explained with an [example](#unicode-support-example). 

Each Unicode character<sup>[[4]](#ref-unicode-character)</sup> has a 
corresponding code point<sup>[[5]](#ref-code-point)</sup>, given by
[`ord()`](https://docs.python.org/3/library/functions.html#ord).
We use this code point and n to determine the resultant shifted character.
Given a Unicode block with some `length`, starting at `first_code_point`,

[`translate()`](https://docs.python.org/2/library/string.html#string.translate) 
function to replace each character with its corresponding shifted character.

Python functions [`ord()`](https://docs.python.org/3/library/functions.html#ord) and 
[`chr()`](https://docs.python.org/3/library/functions.html#chr).

<a name="examples"></a>
# Examples 

### ROT13
ROT13<sup>[[6]](#ref-rot)</sup> is the most popular Caesar cipher. 
ROT13 replaces each letter with the 13th letter after it. 
With fewer than 13 letters left in the alphabet, the counting continues at A.
For example:

| Letter | Position | ROT13 | Position |
| :----: | :------: | :---: | :------: |
| A      | 0        | N     | 13       |
| B      | 1        | O     | 14       |
| ...    | ...      | ...   | ...      |
| Y      | 25       | L     | 12       |
| Z      | 26       | M     | 13       |

Using Unicode code points:

| Letter | Code point | ROT13 | Code Point |
| :----: | :--------: | :---- | :--------: |
| A      | 65         | N     | 78         |
| B      | 66         | O     | 79         |
| ...    | ...        | ...   | ...        |
| Y      | 89         | L     | 76         |
| Z      | 90         | M     | 77         |
|        |            |       |            |
| a      | 97         | n     | 110        |
| b      | 98         | o     | 111        |
| ...    | ...        | ...   | ...        |
| y      | 121        | l     | 108        |
| z      | 122        | m     | 109        |

<a name="unicode-support-example"></a>
### Unicode Support
Assume we want to shift all capital letters in a text by 10.
We use the Unicode block from A to Z as our starting alphabet.

```python
>>> shift = 10
>>> alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
>>> length = len(alphabet)
>>> length
26
```

We use `ord()` to get the code point of the first character in the block (in this case A).

```python 
>>> alphabet[0]
'A'
>>> start_code_point = ord(alphabet[0])
>>> start_code_point
65
```

For each character `char` from A to Z, we subtract the start code point
from that character's code point.

```python
ord(char) - start_code_point
```

Examples: 

```python
>>> ord('A') - start_code_point
0
>>> ord('N') - start_code_point
13
>>> ord('Z') - start_code_point
25
```

This gives us numbers from 0 to 25, or more generally, from 0 to `length - 1`,
and allows us to treat the characters by their position in the alphabet (e.g. A is 0, B is 1, ..., Z is 25).
Now we can shift the code point by the given amount. 
Recall that we use modular arithmetic, so if the shift reaches the end of the 
alphabet we loop back to the start.

```python
(ord(char) - start_code_point + shift) % length
```

Examples:

```python
>>> (ord('A') - start_code_point + shift) % length
10
>>> (ord('N') - start_code_point + shift) % length
23
>>> (ord('Z') - start_code_point + shift) % length
9
```

Now that we have each character's new position in the alphabet,
we add the start_code_point to obtain their new shifted_code_point,
and then use `chr()` to find the corresponding character for this 
code point.

```python
chr(((ord(char) - start_code_point + shift) % length) + start_code_point)
```
Examples:
```python
>>> ((ord('A') - start_code_point + shift) % length) + start_code_point
75
>>> chr(75)
'K'
>>> ((ord('N') - start_code_point + shift) % length) + start_code_point
88
>>> chr(88)
'X'
>>> ((ord('Z') - start_code_point + shift) % length) + start_code_point
74
>>> chr(74)
'J'
```

So, given our original alphabet 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' and a shift of 10,
we get the shifted alphabet 'KLMNOPQRSTUVWXYZABCDEFGHIJ'. 
We make a translation table mapping the original alphabet to the shifted alphabet.

```python
translation_table = str.maketrans(original_alphabet, shifted_alphabet)
```

We finally translate the original text string to get the ciphered string.

```python
text.translate(translation_table)
```

# References
[1] https://en.wikipedia.org/wiki/Caesar_cipher <a name="ref-caesar-cipher"></a>   
[2] https://en.wikipedia.org/wiki/Unicode_block <a name="ref-unicode-block"></a>  
[3] https://en.wikipedia.org/wiki/Modular_arithmetic <a name="ref-modular-arithmetic"></a>  
[4] https://en.wikipedia.org/wiki/List_of_Unicode_characters#Basic_Latin <a name="ref-unicode-character"></a>  
[5] https://en.wikipedia.org/wiki/Code_point <a name="ref-code-point"></a>  
[6] https://en.wikipedia.org/wiki/ROT13 <a name="ref-rot13"></a>
