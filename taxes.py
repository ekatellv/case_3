# Part of a case-study #3: Taxes rate
# Developers: Loseva Ekaterina, Shcherbina Ekaterina, Nesterova Alexandra
#

import ru_local as ru

MAX_MONTH = 12

def free_tax():
    '''
    The function determines the annual tax-free amount.
    '''
    amount = 0
    for month in range(1, MAX_MONTH + 1):
        value = float(input(f'{ru.FREE_TAX} {ru.NAME[month]} [USD]: '))
        amount += value
    return amount

def annual_amount():
    '''
    The function determines the annual amount.
    '''
    amount = 0
    for month in range(1, MAX_MONTH + 1):
        value = float(input(f'{ru.INCOME} {ru.NAME [month]} [USD]: ' ))
        amount += value
    return amount

def one_subject(amount):
    percents = [0.1, 0.15, 0.25, 0.28, 0.33, 0.35, 0.396]
    thresholds = [0, 9075, 36900, 89350, 186350, 405100, 406750]
    max_threshold = 0
    while amount > thresholds[max_threshold + 1]:
        max_threshold += 1
    taxes = (amount - thresholds[max_threshold]) * percents[max_threshold]
    for i in range(0, max_threshold):
        taxes += percents[i] * (thresholds[i + 1] - thresholds[i])
    return taxes

def married_couple(amount):
    percents = [0.1, 0.15, 0.25, 0.28, 0.33, 0.35, 0.396]
    thresholds = [0, 18151, 73800, 148850, 226850, 405100, 457600]
    max_threshold = 0
    while amount > thresholds[max_threshold + 1]:
        max_threshold += 1
    taxes = (amount - thresholds[max_threshold]) * percents[max_threshold]
    for i in range(0, max_threshold):
        taxes += percents[i] * (thresholds[i + 1] - thresholds[i])
    return taxes

def single_parent(amount):
    percents = [0.1, 0.15, 0.25, 0.28, 0.33, 0.35, 0.396]
    thresholds = [0, 12950, 49400, 127550, 206600, 405100, 432200]
    max_threshold = 0
    while amount > thresholds[max_threshold + 1]:
        max_threshold += 1
    taxes = (amount - thresholds[max_threshold]) * percents[max_threshold]
    for i in range(0, max_threshold):
        taxes += percents[i] * (thresholds[i + 1] - thresholds[i])
    return taxes

print(f'{ru.TAX_PAYER}')
category = int(input(f'{ru.VALUES}'))
print(f'{ru.YEAR_INCOME}')
amount = annual_amount()
print(f'{ru.SUM_INCOME}', amount)
print(f'{ru.FREE_TAX2}')
free_amount = free_tax()
print(f'{ru.SUM_FREE_TAX}', free_amount)
amount -= free_amount
print(f'{ru.SUM_TAX}', amount)
match category:
    case 1:
        tax = one_subject(amount)
    case 2:
        tax = married_couple(amount)
    case 3:
        tax = single_parent(amount)
print(f'{ru.YEAR_TAX}', tax)
print(f'{ru.MONTH_TAX}', round(tax/12, 2))

if __name__ == '__main__':
    main()
