
fr = open('file_numbers.txt', mode = 'r')
old_number = 0
for l in fr:
    new_number = int(l)
    print_number = new_number + old_number
    old_number = print_number
    print(print_number)
    
fr.close()



