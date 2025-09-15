from my_module import Array

fruits = Array()

fruits.append("mango")
fruits.append("banana")
fruits.append(5)
print(fruits)
fruits.append(3)
fruits.append(9)
print(fruits)
fruits.insert(2, "apple")
fruits.pop()
fruits.pop(0)
fruits.remove("apple")
print(fruits)