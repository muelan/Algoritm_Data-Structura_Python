#7. По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника,
#   составленного из этих отрезков. Если такой треугольник существует, то определить,
#   является ли он разносторонним, равнобедренным или равносторонним.



a = float(input('Введите длину отрезка 1: '))
b = float(input('Введите длину отрезка 2: '))
c = float(input('Введите длину отрезка 3: '))

if a + b > c:
    if a + c > b:
        if b + c > a:
            print(f'Треугольник со сторонами a = {a}, b = {b} и c = {c} существует')
            if a == b and a == c:
                print(f'Треугольник равносторонний')
            elif a == b or a == c or b == c:
                print(f'Треугольник равнобедренный')
            else:
                print(f'Треугольник разносторонний')
else:
    print(f'Треугольник со сторонами a = {a}, b = {b} и c = {c} не существует')


