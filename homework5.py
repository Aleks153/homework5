immutable_var = 'sun', 'beach', 'sea', 256
print('Immutable tuple: ', immutable_var)
# immutable_var[0] = 123 - нельзя заменить первый элемент кортежа 'sun' на 123 (свойство кортежа)
mutable_list = ['sun', 'beach', 'sea', 256, ['one', 'two']]
print('Initial list: ', mutable_list)
mutable_list [2] = 'moon'
mutable_list [4][0] = 'zero'
x = mutable_list [0].upper()
mutable_list [0] = x
mutable_list [3] = mutable_list [3] / 5
print('Second Mutable list: ', mutable_list)
