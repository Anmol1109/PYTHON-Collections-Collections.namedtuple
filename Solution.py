# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
n = int(input())
field = input().split()

total_marks = 0
for i in range(n):
    students = namedtuple("student",field)
    MARKS, CLASS, NAME, ID = input().split()
    student = students(MARKS, CLASS,NAME,ID)
    total_marks += int(student.MARKS)

print('{:.2f}'.format(total_marks / n))
