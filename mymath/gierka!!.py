import mymeth as m

guess = m.read_number()
computer_guess = m.generate_numer()


if guess==computer_guess:
    print('Wygrałeś!')
else:
    print(f'Przegrałeś, numer był: {computer_guess}')