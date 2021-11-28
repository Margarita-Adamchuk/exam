def credit(namber):
    return (len(namber)-4) * "*" + namber[-4:]

print(credit(input("Введите номер карты: ")))