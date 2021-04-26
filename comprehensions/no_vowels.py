def vowels():
    lower = {'a', 'o', 'u', 'e', 'i'}
    upper = {vowel.upper() for vowel in lower}
    return lower.union(upper)


def string_without_vowels(text, iterable):
    result = [x for x in text if x not in iterable]
    return ''.join(result)


string = string_without_vowels(input(), vowels())

print(string)
