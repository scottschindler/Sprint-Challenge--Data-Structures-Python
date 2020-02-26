import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

def answer_1(names_1, names_2):
    duplicates = []
    for name in names_1:
        if name in names_2:
            duplicates.append(name)
    return duplicates


class HashMap():
    def __init__(self):
        self.storage = {}

    def create_set(self, items):
        i = 0
        for item in items:
            self.storage[item] = i
            i += 1

    def add_items(self, items):
        i = len(self.storage)
        duplicates = []
        for item in items:
            if item in self.storage:
                duplicates.append(item)
            else:
                self.storage[item] = i
                i += 1
        return duplicates


def answer_1b(names_1, names_2):
    map_1 = HashMap()
    map_1.create_set(names_1)
    duplicates = map_1.add_items((names_2))
    return duplicates

end_time = time.time()
# print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")