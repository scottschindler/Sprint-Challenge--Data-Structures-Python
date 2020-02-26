import time
from binary_search_tree import BinarySearchTree


start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

names_bst = BinarySearchTree(names_1[0])
duplicates = []

# do two for loops

# second loop will append identical names to the duplicates array
for name_1 in names_1[1:]:
    # use the insert method from bst to add name_1
    names_bst.insert(name_1)

for name_2 in names_2:
    # if name_2 == to a name_1 insert the name with the bst method append!
    if names_bst.contains(name_2): 
        duplicates.append(name_2)
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?

# original run time was 8 seconds with o(n^2)
# new run time is --  runtime: 0.14606523513793945 seconds o (n)