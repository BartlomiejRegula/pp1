ilosc = input("Podaj ilość pieniędzy: ")
amount=int(ilosc)
a = amount//5
amount%=5
b = amount//2
amount%=2
print(f'The amount of PLN {ilosc} in coins::\n5zł - {a}\n2zł - {b}\n1zł - {amount}')