def palindrom(word):
    if word[::1] == word[::-1]:
        print(f"{word} Это слово является полиндромам")
    elif word[::1] != word[::-1]:
        print(f"{word} Это слово не является полиндромом")


print(palindrom(input("Введите слово:\n")))
