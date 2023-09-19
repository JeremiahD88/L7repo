def my_func(argument):
    print(argument)
    for i in range(0,len(argument)):
        argument[i] = 'a'
#Gör Tuples vid () i stället för []. Kan inte ändras
my_original_list = ('1','2','3')
#my_original_list = ['1','2','3']

#my_func(my_original_list)
print(my_original_list[1])