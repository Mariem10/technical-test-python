
Dict_origine = {
    'Max': 17.5,
    'Michael': 10.23,
    'Peter': 09.56,
    'Mark': 09.56,
    'Alex': 12.00
}
student = ['Max', 'Micheal', 'Peter', 'Mark', 'Alex']
grades = [17.5, 10.23, 09.56, 09.56, 12.00]

dict_grade = dict
for i in range(len(grades)):
    if grades[i] < 10:
        grades[i] = 'Failed'

    elif 10 < grades[i] <= 12:
        grades[i] = 'Satisfactory'

    elif 12 < grades[i] <= 14:
        grades[i] = 'good'
    elif 14 < grades[i] <= 16:
        grades[i] = 'Very Good'
    else:
        if grades[i] > 16:
            grades[i] = 'Excellent'


dict_grade = dict(zip(student, grades))


dict_grades = {}
for k, v in dict_grade.items():
    if v not in dict_grades:
        dict_grades[v] = []
    dict_grades[v].append(k)

for k in sorted(dict_grades, reverse=True):
    for v in sorted(dict_grades[k]):
        print("{} : {}".format(v, k))

