a="hello"
Name="Swapna"
b=", welcome to Python programming"
result = a+" "+Name + b
print(result)
print(a[0])
print(b[30])
print(Name[0:6])
print(result[26:40])
print(result[0:7])
print(result[::-1])
print(b[13:19])
strM = "Python beginner tutorial"
print(strM.upper())
print(strM.lower())
result = strM.capitalize()

print(result)
count_t = strM.count('t')

print(count_t)

new_string = strM.replace("Python", "Machine Learning")

print(new_string)

tuple1 = (10, 20, 30)
tuple2 = (40, 50, 60)

print(tuple1)
print(tuple2)
# a. Concatenate the two tuples
t_combine = tuple1 + tuple2
print("Combined tuple:", t_combine)

# b. Repeat the elements of t_combine 3 times
print("Repeated tuple:", t_combine * 3)

# c. Access the 3rd element
print("3rd element:", t_combine[2])

# d. Access the first three elements
print("First three elements:", t_combine[:3])

# e. Access the last three elements
print("Last three elements:", t_combine[-3:])
