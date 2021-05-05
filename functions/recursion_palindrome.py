def palindrome(word, index=0, other_end=-1):
    if index == len(word) // 2:
        return f"{word} is a palindrome"

    if word[index] == word[other_end]:
        return palindrome(word, index + 1, other_end - 1)
    else:
        return f"{word} is not a palindrome"


print(palindrome("abcba", 0))