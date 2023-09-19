
""" while True:
    name = input('Tell me your name: ')
    fw = open('names.txt', mode = 'w')
    name = name.title()
    fw.write(name)
    fw.close() """

def is_prime(number):
    '''returns true if argument is a prime number'''
    if number == 1:
        return True
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

     
while True:
    number = int(input('Give me an integer: '))
    if number == 0:
        break
    if is_prime(number):
        print(f'{number} is a primenumber')
    else:
        print(f'{number} is NOT a primenumber')