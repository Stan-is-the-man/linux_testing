command = input()
students = {}

while ":" in command:
    split = command.split(':')
    name = split[0]
    points = int(split[1])
    course = split[2]
    students[name] = [points, course]
    
    command = input()

for name, points in students.items():
    if command == students[name][1]:
        print(f"{name} - {points[0]}")

print(students)
