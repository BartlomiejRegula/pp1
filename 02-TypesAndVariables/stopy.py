height_cm=int(input('podaj wzrost'))

ft=round(height_cm/2.54,2)

stopy=ft//12

reszta=ft%12

print(f'Im {height_cm} i.e. {int(stopy)} feet and {int(reszta)} inches ')

