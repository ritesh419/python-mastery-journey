# Task-1 >>

num_int = 10                    #immutable
num_float = 11.33               #immutable
name_str = "Ritesh"             #immutable   (ordered collection)
is_bool = True                  
num_list = [1, 2, 3, 4]         #mutable    (ordered collection)
num_tuple = (1, 2, 3, 4)        #immutable  (ordered collection)
num_dic = {"a": 1, "b": 2}      #mutable  (key-value pair) (un-ordered collection)
num_set = {1, 2, 3, 4}          #mutable (unique)   (un-ordered collection)


print(type(num_int), id(num_int))
print(type(num_float), id(num_float))
print(type(name_str), id(name_str))
print(type(is_bool), id(is_bool))
print(type(num_list), id(num_list))
print(type(num_tuple), id(num_tuple))
print(type(num_dic), id(num_dic))
print(type(num_set), id(num_set))


# Task-2>>

x_list = [1, 2, 3]
y_list = x_list
y_list.append(3)
print(x_list)
print(id(x_list), id(y_list))

if x_list == y_list:
    print("true, they contains same values", x_list)

if x_list is y_list:
    print("Yes, same address", id(x_list))


# Task-3 >>

a_list = [10, 20, 30, 40, 50]

b_list = a_list     
c_list = a_list.copy()

b_list.append(60)
print(id(a_list))
print(id(b_list))
print(id(c_list))

print(a_list)
print(b_list)
print(c_list)