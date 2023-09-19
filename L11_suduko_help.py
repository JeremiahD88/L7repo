f = open('csv_numbers.csv', mode = 'r')

num = []

for line in f:
    num.append(line.split(','))
#print(num)

""" int_list = []
for outer_element in num:
    new_inner_list = []
    for inner_element in outer_element:
        new_inner_list.append(int(inner_element))
    int_list.append(new_inner_list)
#print(int_list) """
int_list = []
for outer_element in num:
    int_list.append([int(i) for i in outer_element])
    
print(int_list)
f.close()
