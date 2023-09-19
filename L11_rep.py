int_list = []
#bara loope igenom(i får inte värdet i elementerna i listen): for i in range(0, len(int_list))
def calc_func(int_list):
    sum = 0
    for value in int_list:
        sum += value
    print(sum / len(int_list))   



def ave_func():
    user_input = (input('Give me a integer: '))
    if user_input == 'Q':
        calc_func(int_list)
    else:
        int_list.append(int(user_input))



while True:
    ave_func() 


    