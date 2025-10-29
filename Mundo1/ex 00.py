name = str(input('Type your name: ')).strip().title()
day = int(input('Type the day you were born: '))
month = int(input('Type the month you were born: '))
year = int(input('Type the year you were born: '))
print(f'Hello {name}, be welcome!')
print('So, you born in {}/{}/{}, alright!'.format(month, day, year))

x = int(input('Type a number: '))
y = int(input('Another number: '))
z = x + y
print('The sum between {} and {} is {}.'.format(x, y, z))
print(type(z))
