# for names
studName = {}

# the loop (5 times)
for a in range(5):

    # name loop and initialization
    name = input(f"Student {a+1} name: ")
    classPartGrade = 0
    summativeGrade = 0
    finalExGrade = 0

    # class participation loop (5 times per student)
    for b in range(5):
        classPartGrade += float(input("Enter class participation {} grade: ".format(b+1)))

    # summative loop (3 times per student)
    for c in range(3):
        summativeGrade += float(input("Enter summative assessment {} grade: ".format(c+1)))

    # final exam loop (1 time per student)
    for d in range(1):
        finalExGrade = float(input("Enter final exam {} grade: ".format(d+1)))

    # calculation
    classPartGrade = (classPartGrade / 5) * 0.3
    summativeGrade = (summativeGrade / 3) * 0.3
    finalExGrade *= 0.4
    totalGrade = classPartGrade + summativeGrade + finalExGrade
    letterGrade = 'A'

    # grade letter if/else chain
    if totalGrade >= 90:
        letterGrade = "A"
    elif totalGrade >= 80:
        letterGrade = "B"
    elif totalGrade >= 70:
        letterGrade = "C"
    elif totalGrade >= 60:
        letterGrade = "D"
    else:
        letterGrade = "F"
    studName[name] = totalGrade, letterGrade

# result printing loop
print(f"{'Name':<15} {'Total Grade':<15} {'Letter Grade':<15}")
print()
for name, grades in studName.items():
    totalGrade, letterGrade = grades
    print(f"{name:<15} {totalGrade:<15.2f} {letterGrade:<15}")
    print()