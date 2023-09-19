""" car_dict = {
    'brand' : 'Ford',
    'model' : 'Mustang',
    'year'  :  1994
}

#print(car_dict)
#print(car_dict['year'])

car_dict['milage'] = 20000
#print(car_dict)

for key, value in car_dict.items():
    print(key,value) """

fuel_prices = {
    'Today'        : {'Diesel' : 21.84, 'E95' : 20.4, 'E85' : 14.99},
    'Yesterday'    : {'Diesel' : 22.0, 'E95' : 20.4, 'E85' : 15.0},
    'Two_days_ago' : {'Diesel' : 21.7, 'E95' : 20.2, 'E85' : 14.98}
}
sum = {'E95':0, 'Diesel':0, 'E85':0}
for price in fuel_prices.values():
    sum['E95'] += price['E95']
    sum['Diesel'] += price['Diesel']
    sum['E85'] += price['E85']

for type, price in sum.items():
   print(f'Average price is of {type}: {sum[type]/len(fuel_prices.values())}')
    