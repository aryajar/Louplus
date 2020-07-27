n = int(input("Enter the number of students: "))
data = {}      # dictionary to save data
subjects = ('Physics', 'Math', 'History')   # all the subjects

for i in range(0,n):
    name = input('Enter the name of the student {} :'.format(i + 1))
    marks = []
    for x in subjects:
        marks.append(int(input('Enter mark of {}:'.format(x))))
    data[name] = marks
for x, y in data.items():
    total = sum(y)
    print("{}'s total marks {}".format(x, total))
    if total > 120:
        print(x, "passed :)")
    else:
        print(x, "failed :(")