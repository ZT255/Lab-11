import os
import matplotlib.pyplot as plt

print("1. Student grade")
print("2. Assignment statistics")
print("3. Assignment graph")

selection = int(input("Enter your selection: "))

if selection == 1:
    student = input("What is the student's name: ")
    student_id = None
    with open('data/students.txt', 'r') as file:
        for line in file:
            if student in line:
                student_id = line.replace(student + '\n', "")
                break
    if student_id is None:
        print("Student not found")
    else:
        grades = []
        for dir_name, sub_dirs, files in os.walk("data/submissions"):
            for file_name in files:
                with open(f"data/submissions/{file_name}", 'r') as file:
                    content = file.read()
                    if content.startswith(student_id + '|'):
                        content_split = content.split('|')
                        with open(f"data/assignments.txt", 'r') as file2:
                            found = False
                            for line in file2:
                                if found:
                                    points = int(line.strip())
                                found = True if content_split[1] in line else False
                        grades.append(int(content_split[2]) * points)
        print(f'{round(sum(grades) / 1000)}%')



elif selection == 2:
    assignment = input("What is the assignment name: ")
    assignment_id = None
    assignment_points = None
    with open(f"data/assignments.txt", 'r') as file:
        found = False
        i = 0
        for line in file:
            if found:
                assignment_id = line.strip()
                i += 1
            if i == 1:
                assignment_points = line.strip()
                break
            found = True if assignment in line else False

    if assignment_id is None:
        print("Assignment not found")
    else:
        grades = []
        for dir_name, sub_dirs, files in os.walk("data/submissions"):
            for file_name in files:
                with open(f"data/submissions/{file_name}", 'r') as file:
                    content = file.read()
                    if ('|' + assignment_id + '|') in content:
                        content_split = content.split('|')
                        grades.append(int(content_split[2]))
        print(f"Min: {min(grades)}%")
        print(f"Avg: {round(sum(grades)/len(grades))}%")
        print(f"Max: {max(grades)}%")


else:
    assignment = input("What is the assignment name: ")
    assignment_id = None
    with open(f"data/assignments.txt", 'r') as file:
        found = False
        i = 0
        for line in file:
            if found:
                assignment_id = line.strip()
            found = True if assignment in line else False

    if assignment_id is None:
        print("Assignment not found")
    else:
        grades = []
        for dir_name, sub_dirs, files in os.walk("data/submissions"):
            for file_name in files:
                with open(f"data/submissions/{file_name}", 'r') as file:
                    content = file.read()
                    if ('|' + assignment_id + '|') in content:
                        content_split = content.split('|')
                        grades.append(int(content_split[2]))
        plt.hist(grades, bins=[50, 60, 70, 80, 90, 100])
        plt.show()
