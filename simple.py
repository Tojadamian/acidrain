import numpy as np

while True:
    concentration= input("Podaj stężenie molowe w postacji liczba^(x): ")
    try:
        concentration = float(concentration)
    except ValueError:
        if '^' in concentration:
            base, exponent = concentration.split('^')
            base = float(base)
            exponent = float(exponent.replace('(', '').replace(')', ''))
            concentration = base ** exponent

    # funkcja zwracające pH na podstawie stężenia molowego i sprawdz czy pH mieści się w zakresie 0-14
    def ph_from_concentration(concentration):
        ph = -np.log10(concentration)
        if ph < 0 or ph > 14:
            raise ValueError('pH musi być w zakresie 0-14')
        return ph

    # jeśli pH jest poza zakresem to zacznij pętle od nowa
    try:
        ph_from_concentration(concentration)
    except ValueError as e:
        print(e)
        continue

    print('pH:', ph_from_concentration(concentration))
    # sprawdzenie czy pH jest zasadowe, kwaśne czy obojętne
    if ph_from_concentration(concentration) > 7:
        print('Roztwór jest zasadowy')
    elif ph_from_concentration(concentration) < 7:
        print('Roztwór jest kwaśny')
    else: print('Roztwór jest obojętny')
    print('Aby zakończyć wciśnij control + c')
