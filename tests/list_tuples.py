# count() method
my_list = [1, 2, 2, 3, 4, 2]
count_of_two = my_list.count(2)
print(count_of_two)  # Output: 3

# Indexing Elements
my_list = ['apple', 'banana', 'cherry', 'banana']
index_of_banana = my_list.index('banana')
print(index_of_banana)  # Output: 1

#  Reversing a List
my_list = [1, 2, 3, 4, 5]
my_list.reverse()
print(my_list)  # Output: [5, 4, 3, 2, 1]

#  Sorting a List
my_list = [5, 2, 8, 1, 9]
my_list.sort()
print(my_list)  # Output: [1, 2, 5, 8, 9]

# Descending order sorting:
my_list = [5, 2, 8, 1, 9]
my_list.sort(reverse=True)
print(my_list)  # Output: [9, 8, 5, 2, 1]

# append list
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)

# Tuples
# count() Method
my_tuple = (1, 2, 3, 2, 4, 2, 5)
count_of_2 = my_tuple.count(2)
print(count_of_2) # Output: Count of 2: 3

# index() Method
my_tuple = ("apple", "banana", "cherry", "banana")
index_of_banana = my_tuple.index("banana")
print(index_of_banana) # Output: Index of 'banana': 1