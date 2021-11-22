def credit(namber):

    if len(namber) == 16:
        print("*"*12 + namber[12:16])
    else:
        print("Номер карты составляет 16 цифр")

print(credit(input("Введите номер карты: ")))