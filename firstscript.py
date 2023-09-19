import time

def check_if_retired(retirement_age = 65, a = 1):
    if a > retirement_age:
        return True
    else:
        return False


""" for i in range(0, 11):
    print(i, end='\r')
    time.sleep(0.5)

age = 35
print(f'Jeremiah is {age}') 
     """

""" age = int(input('Tell me your age!\n'))

while age !=0:
    if check_if_retired(a = age):
        print('You are retired')
    else:
        print("You are in working age")
    age = int(input('Tell me your age!\n'))
 """
    
my_int = 123
print(my_int, 'hej med dig')

#first_var = 123
#second_var = 'My name is Jeremiah'
#print(first_var, second_var, end = '-')

#print("Detta är en apostrof '")
#print ('"Detta" är en sträng"')
#hello_var = 'Hello'
#world_var = 'world'
#print(hello_var, world_var)

for i in range(0,10):
    print(i)