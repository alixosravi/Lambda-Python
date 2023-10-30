my_list = ["aaa", "abbaa", "a", "aa", "aaaaa"]
# map
# filter
# sorted

new_list1 = map(lambda x: x * 3, my_list)
new_list2 = filter(lambda x: x > 5, my_list)

new_list3 = sorted(my_list, key=lambda x: len(x))

print(new_list1, new_list2, new_list3)

#we added print