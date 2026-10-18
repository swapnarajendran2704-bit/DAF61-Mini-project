
age_list = [24, 25, 26, 27, 28]

print(age_list)

name_list = ["Anu", "Meera", "Rahul", "Arun", "Priya"]

print(name_list)

name_list.append("Yazhini")
print(name_list)
age_list.insert(2, 30)
print(age_list)
name_list.remove("Yazhini")
print(name_list)
age_list.pop()
print(age_list)
age_list.extend([29, 30, 26])
print(age_list)
age_list.sort(reverse=True)
print(age_list)
print("Maximum age:", max(age_list))
print("Minimum age:", min(age_list))
print("Sum of ages:", sum(age_list))
print(name_list[0])
print(name_list[-1])
print(name_list[2:5])
print(name_list[::-1])

student_marks = {
    "Anu": 75,
    "Meera": 88,
    "Rahul": 65,
    "Arun": 92,
    "Priya": 78
}

print(student_marks)

print(student_marks["Rahul"])
student_marks["Janani"] = 80

print(student_marks)

student_marks["Anu"] = 82

print(student_marks)


print("Student names:", student_marks.keys())

print("Student marks:", student_marks.values())

print("Student name and marks:", student_marks.items())

my_set = set(['a', 'e', 'i', 'o', 'u', 'a', 'a', 'i'])

print(my_set)
my_set.remove('u')
my_set.add('s')

print(my_set)

set1 = {1, 3, 5, 7, 9}
set2 = {2, 3, 5, 8, 10}

print(set1)
print(set2)

print("Union:", set1.union(set2))
print("Intersection:", set1.intersection(set2))



score = int(input("Enter your score (0 to 10): "))

if score < 0 or score > 10:
    print("Invalid score! Please enter a score between 0 and 10.")

elif score > 7:
    print("Performance Category: Above Average")
    print("Excellent work! Keep up the good performance.")

elif score >= 4:
    print("Performance Category: Average")
    print("Good effort! Keep practising to improve your score.")

else:
    print("Performance Category: Below Average")
    print("Need to improve your performance. Consistent practice will lead to better results.")
