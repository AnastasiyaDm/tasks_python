import doctest
from collections import Counter


def sort_letters(text):
    """
    Return a string of the same letters where all the letters are sorted by
    its frequency in descending order. In case of equal frequency letters
    should go in the order they were met in the original string.
    >>> sort_letters('aaabccccdeefffff')
    'fffffccccaaaeebd'
    >>> sort_letters('abcdefghijklmnop')
    'abcdefghijklmnop'
    >>> sort_letters('')
    ''
    >>> sort_letters('aba')
    'aab'
    >>> sort_letters('abcabccba')
    'aaabbbccc'
    """
    letters = Counter(text)
    sorted_letters = sorted(letters.items(), key=lambda x: x[1], reverse=True)
    result = []
    for letter in sorted_letters:
        result.append(letter[0]*letter[1])
    return ''.join(result)


if __name__ == "__main__":
    doctest.testmod()
