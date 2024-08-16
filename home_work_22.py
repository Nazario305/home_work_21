number = int(input('Введіть 4-х значне число: '))

n1 = number // 10000
n2 = number // 1000 % 10
n3 = number // 100 % 10
n4 = number // 10 % 10
n5 = number % 10

print(f'{n5}{n4}{n3}{n2}{n1}')
