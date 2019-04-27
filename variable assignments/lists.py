my_list = [1,2,3]

my_list = ['STRING', 100, 23.2]

print(len(my_list))

mylist = ['one', 'two','three']
print(mylist[1:])

another_list = ['four', 'five']
print(mylist + another_list)
new_list =mylist + another_list
print(new_list)
new_list[0] = 'ONE ALL CAPS'
print(new_list)

new_list.append('six')
print(new_list)
new_list.append('seven')
print(new_list)

new_list.pop()
print(new_list)

popped_item = new_list.pop(0)
print(popped_item)
print(new_list)

new_list = ['a', 'e','x','b', 'c']
num_list = [4,1,8,3]

print(new_list.sort())
print(new_list)

print(num_list.sort())
print(num_list)

