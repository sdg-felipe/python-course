def calculate_homework(grades):
    sum_of_grades = 0
    for homework in grades.values():
        sum_of_grades += homework

    final_grade = sum_of_grades / len(grades)
    return round(final_grade,2)