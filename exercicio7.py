"""
Check the documentation for tuples, create as many collections (tuples, lists)
as needed, and use the following tuple functions:

is operator
len(tuple)
max(tuple)
min(tuple)
tuple(seq)

"""

my_tuple = (5, 8, 3, 9, 1, 10)

print("This is my tuple:", my_tuple)

same_tuple = my_tuple

is_same_tuple_bool = my_tuple is same_tuple

print("Are my_tuple and same_tuple referencing the same object?", is_same_tuple_bool)
print("Length of the tuple:", len(my_tuple))
print("Maximum value in the tuple:", max(my_tuple))
print("Minimum value in the tuple:", min(my_tuple))

print("==============================================")

my_list = [5, 8, 3, 9, 1, 10]

print("This is my list :", my_list)

same_list = my_list

is_same_list_bool = my_tuple is same_list

print("Are my_list and my_list referencing the same object?", is_same_list_bool)
print("Length of the my_list:", len(my_tuple))
print("Maximum value in the my_list:", max(my_tuple))
print("Minimum value in the my_list:", min(my_tuple))

print("==============================================")

my_list = [1, 2, 3, 4, 5]
my_string = "hello"

tuple_from_list = tuple(my_list)
tuple_from_string = tuple(my_string)

print("Tuple from list:", tuple_from_list)
print("Tuple from string:", tuple_from_string)

