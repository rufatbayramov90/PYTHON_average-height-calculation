student_heights = input().split()

for n in range(0, len(student_heights)):
    student_heights[n]  = int(student_heights[n])

total_height = 0
for height in student_heights:
    total_height += height

number_student = 0
for student in student_heights:
    number_student += 1

average_height = round(total_height / number_student)
print(f"Average height - {average_height}")



