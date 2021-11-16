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
    index_by_letter = {}
    for i, letter in enumerate(text):
        if letter not in index_by_letter:
            index_by_letter[letter] = i * -1

    letters = Counter(text)
    pairs = [(frequency, index_by_letter[letter], letter) for letter, frequency in letters.items()]
    sorted_pairs = sorted(pairs, reverse=True)

    result = []
    for freq, _, letter in sorted_pairs:
        result.append(letter * freq)
    return ''.join(result)


if __name__ == "__main__":
    doctest.testmod()
