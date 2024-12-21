from collections import namedtuple
import csv

student = namedtuple(
    'student', ['stuid', 'chinese', 'math', 'english', 'infomation'])

students = []
with open('scores.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        students.append(student(*row))

print('学号\t平均成绩')
for stu in students:
    avg = (int(stu.chinese) + int(stu.math) +
           int(stu.english) + int(stu.infomation)) / 4
    print(f'{stu.stuid}\t{avg}')
