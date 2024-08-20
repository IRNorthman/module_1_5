immutable_var = tuple([1,2,True,'Alarm'])
print(immutable_var)
#immutable_var[0]=2
#Невозможно сделать операцию, так как кортеж не поддерживает изменение переменных внутри себя
mutable_list=['apple', 1, 5, False]
print(mutable_list)
mutable_list[0]='pigeon'
mutable_list.extend('LINE')
mutable_list.append('WOW')
mutable_list.remove(1)
mutable_list.remove('I')
print(mutable_list)