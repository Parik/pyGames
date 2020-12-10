a = int(input ("Введите первое число "))
b = int(input ("Введите второе число "))
c = int(input ("Введите третье число "))
d = int(input ("Введите четвертое число "))

def min(a, b):
    if (a<b):
        return a
    else:
        return b

min1 = min(a, b)
min2 = min(c, d)

if (min1 < min2):
    out = min1
else:
    out = min2

print(f"Минимальное число из введенных: {out}")