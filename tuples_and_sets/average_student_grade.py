def input_to_dict(num):
    res = {}
    for _ in range(num):
        student, grade = input().split()
        if student not in res:
            res[student] = []
        res[student].append(float(grade))
    return res


def average(value1, value2):
    return f"{value1 / value2:.2f}"


def print_result(collection):
    for student, grades in collection.items():
        student_average = average(sum(grades), len(grades))
        formatted_grades = ' '.join(map(lambda x: f"{x:.2f}", grades))
        print(f"{student} -> {formatted_grades} (avg: {student_average})")


students_grades = input_to_dict(int(input()))
print_result(students_grades)
