x = 38

print('дратути!')
if x < 0:
    print('меньше нуля')
print('дотвидания!')

print('-' * 20, 'Следующий блок тестов', '-' * 20, end='\n')

a, b = 10, 5

if a > b:
    print('a > b')

if a > b and a > 0:
    print('успех')

if (a > b) and (a > 0 or b < 1000):
    print('успех')

if 5 < b and b < 10:
    print('успех')

print('-' * 20, 'Следующий блок тестов', '-' * 20, end='\n')

if '34' > '123':
    print('успех')

if '123' > '12':
    print('успех')

if [1, 2] > [1, 1]:
    print('успех')

print('-' * 20, 'Следующий блок тестов', '-' * 20, end='\n')

try:
    if '6' > 5:
        print('успех')
except TypeError as e:
    print(e)

try:
    if [5, 6] > 5:
        print('успех')
except TypeError as e:
    print(e)

if '6' != 5:
    print('успех')
