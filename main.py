print("Калькулятор\n")

print("Сложение")
try:
    sum1 = float(input("Введите первое число: "))
    sum2 = float(input("Введите второе число: "))
    result1 = sum1 + sum2
except ValueError:
    print("Ошибка: введено не число!")
else:
    print(f"Сумма: {result1}")

print("\nВычитание")
try:
    sub1 = float(input("Введите первое число: "))
    sub2 = float(input("Введите второе число: "))
    result2 = sub1 - sub2
except ValueError:
    print("Ошибка: введено не число!")
else:
    print(f"Сумма: {result2}")

print("\nУмножение")
try:
    mult1 = float(input("Введите первое число: "))
    mult2 = float(input("Введите второе число: "))
    result3 = mult1 * mult2
except ValueError:
    print("Ошибка: введено не число!")
else:
    print(f"Сумма: {result3}")

print("\nДеление")
try:
    div1 = float(input("Введите первое число: "))
    div2 = float(input("Введите второе число: "))
    result4 = div1 / div2
except ValueError:
    print("Ошибка: введено не число!")
except ZeroDivisionError:
    print("Делить на ноль нельзя!")
else:
    print(f"Сумма: {result4}")

print("\nПрограмма завершена!")
