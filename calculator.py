number_1 = int(input('Enter your first number: '))
number_2 = int(input('Enter your second number: '))
operation = input('Do you want to add, subtract, multiply or divide your numbers? ')

if operation == 'add':
    total = number_1 + number_2
    print(f'{number_1} + {number_2} = {total}')
elif operation == 'subtract':
    total = number_1 - number_2
    print(f'{number_1} - {number_2} = {total}')
elif operation == 'multiply':
    total = number_1 * number_2
    print(f'{number_1} * {number_2} = {total}')
elif operation == 'divide':
    total = number_1 / number_2
    print(f'{number_1} / {number_2} = {total}')
else:
    print('Invalid operation')
