from socket import INADDR_ALLHOSTS_GROUP


amount = input('Enter the amount in PLN:')
intamount = int(amount)

a = intamount // 5
intamount = a % 5 

b = intamount // 2
intamount = b % 2

print(f'The amount of PLN {amount} in coins')
print(f'5zl - {a} ')
print(f'2zl - {b} ')
print(f'1zl - {intamount} ')
