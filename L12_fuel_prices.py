fuel_prices = [[21.84,22.0,21.7],[20.4,20.4,20.2],[14.99,15.0,14.98]]

print('Diesel:',fuel_prices[0])
sum = 0
for fueltype in range(0,3):
    sum = 0
    for price in fuel_prices[fueltype]:
        sum += price

    print(f'Diesel avg price: {sum/len(fuel_prices[0])}')