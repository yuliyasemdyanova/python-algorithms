#9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

if a > b:
    if a < c:
        print(f'average = {a:.3f}')
    elif b>c:
        print(f'average = {b:.3f}')
    else:
        print(f'average = {c:.3f}')
else:
    if a > c:
        print(f'average = {a:.3f}')
    elif b>c:
        print(f'average = {c:.3f}')
    else:
        print(f'average = {b:.3f}')