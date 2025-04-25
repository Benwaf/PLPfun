# an empty list
my_list = []
# appending elements to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
# Inserting an element at a specific index(Insert 15 at poeition 2)
my_list.insert(1, 15)  
# Estending the list with another list
my_list.extend([50, 60, 70])
# Removing an element from the list( the last element)
my_list.pop()
# sorting the list in ascending order
my_list.sort()
# Finding the index of an element in the list
index_of_30 = my_list.index(30)
print("The index of 30 is:", index_of_30)