my_list_of_tuples = [(1, 2), (3, 4), (5, 2)]
my_list_of_lists = list(map(list, my_list_of_tuples))

just_list = sum(my_list_of_lists, [])

my_set = set(just_list)
my_list = list(my_set)
print(my_list)


i = 0
j = 1
last_list = []
for i in range(len(my_list)):
    j = i+1
    for j in range(j, len(my_list)):
                last_list.append((my_list[i], my_list[j]))

print(last_list)

