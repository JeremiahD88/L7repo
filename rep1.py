""" print('I luv U')
print('a 1000 times!') """

#how_many_times = int(input('How many times do you love me?'))

""" print('I luv U')
print(f'{how_many_times} times') """

#fibofuck

""" first_number = 0
second_number = 1

print(first_number)
print(second_number) """
""" for i in range(0,10):
    new_number = first_number + second_number
    first_number = second_number
    second_number = new_number
    print(new_number)  """

""" i = 0
while i < 10:
    new_number = first_number + second_number
    first_number = second_number
    second_number = new_number
    print(new_number)
    i = i + 1 """
      
def recu_fibo(n):
    if n <= 1:
        return n
    else:
        return (recu_fibo(n - 1) + recu_fibo(n - 2))
    
def recu_fibo2(n):
    if n > 1:
        return (recu_fibo2(n - 1) + recu_fibo2(n - 2))
    else:
        return n
    
print('Please, enter a integer')

n_terms = int(input())
if n_terms <= 0:
    print('Please, enter a integer')
    #n_terms = int(input())
else:
    for i in range(n_terms):
        print(recu_fibo2(i)) 
""" 


def forLoop(n):
    if n == 9:
        return
    else:
        print(n)
        forLoop(n+2)
    
forLoop(0) """

    


