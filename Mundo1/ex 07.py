width = float(input('Wall width: '))
hight = float(input('Wall hight: '))
area = (hight*width)
print(f'The quantity of ink necessary to paint the wall, with measures {width}x{hight},\n'
      f'and area of {area}m² is {area/2:.2f}l')
