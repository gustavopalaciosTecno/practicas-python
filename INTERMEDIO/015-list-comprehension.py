"""
List comprehension
"""
# tipiando las listas

my_original_list = [0,1,2,3,4,5,6,7]
print(my_original_list)
# lo que hace es transformar una lista en otra lista
my_list = [i for i in range(8)]
print(my_list)

def sum_five(number):
    return number + 5
    

my_range = [sum_five(i) for i in range(8)]
print(list(my_range))


