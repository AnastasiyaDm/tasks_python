right = {'m': 4, 'q': 3, 'd': 2, 'z': 1, 'y': 3}
left = {'w': 4, 'p': 3, 'b': 2, 's': 1, 'y': 1}
center = {letter: 1 for letter in "aeuioy"}


def fight(text):
    letters = {}
    for char in text:
        if char in letters:
            letters[char] += 1
        else:
            letters[char] = 1

    counters = {'Right': 0,
                'Left': 0,
                'Center': 0}

    for letter, frequency in letters.items():
        if letter in right:
            counters['Right'] += frequency * right[letter]
        if letter in left:
            counters['Left'] += frequency * left[letter]
        if letter in center:
            counters['Center'] += frequency * center[letter]

    new_counters = [(frequency, letter) for letter, frequency in counters.items()]
    sorted_counters = sorted(new_counters, reverse=True)
    first, second = sorted_counters[:2]
    first_score, first_team = first
    second_score, _ = second
    if first_score != second_score:
        return '{} side wins!'.format(first_team)
    else:
        return "Let's fight again!"


print(fight('abracadabra'))

