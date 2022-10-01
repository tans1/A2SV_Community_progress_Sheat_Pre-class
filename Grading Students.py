def gradingStudents(grades):
    if len(grades) == 0:
        return 
    for i in range(len(grades)):
        if grades[i] >= 38 and ((((grades[i] // 5) * 5) + 5) - grades[i]) < 3:
            grades[i] = (((grades[i] // 5) * 5) + 5)
    return grades
