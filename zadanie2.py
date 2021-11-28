def palindrom(word):
    return f"{word} Это слово является полиндромам" if word[::1] == word[::-1] else f"{word} Это слово не является " \
                                                                                    f"полиндромом "


print(palindrom(input("Введите слово:\n")))
