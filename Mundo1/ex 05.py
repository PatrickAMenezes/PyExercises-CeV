x = int(input('Type a number: '))
contour = '|'
delimiter = '-'*18

print('The times table of {} is: '.format(x))
print(delimiter)
for i in range(1, 11):
   res = x*i
   if res >= 100:
       print(f'{contour:<2} {x} x {i:2} = {res} {contour:<2}')
   else:
       print(f'{contour:<2} {x:<2} x {i:2} = {res:2} {contour:>2}')
print(delimiter)
