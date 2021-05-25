def get_count_of_chars(word):
    char_count = {}
    for el in word:
        char_count[el] = word.count(el)
    return char_count


def format_result(iterable):
    return [f"{key}: {value} time/s" for key, value in iterable.items()]


line = input()
characters = get_count_of_chars(line)
sorted_characters = dict(sorted(characters.items(), key=lambda x: x))
print(*format_result(sorted_characters), sep='\n')
