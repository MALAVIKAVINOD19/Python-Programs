# USING SIMPLE LISTS 

attendance = []

n = int(input("Enter number of students: "))

for i in range(n):
    id = input("Enter student ID: ")
    name = input("Enter student name: ")
    status = input("Enter attendance (P/A): ")

    attendance.append([id, name, status])

print("\nAttendance List:")

for student in attendance:
    print(student)

### USING DICTIONARIES

attendance = { "101" : "Lisa",
               "102" : "Hiya",
               "103" : "Anna"
}

studAtt={ "2026-10-1" : {
    "101": "P",
    "102": "A",
    "103": "P"
}}
