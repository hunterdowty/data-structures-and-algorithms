# example of calling built-in sort function in Python
# takes the tuples generated in grades variable and sorts highest to lowest grade

def getGrade(studentTuple):
    return studentTuple[1]

grades = { "Hunter": 98, "Hannah": 95, "Mary": 90, "David": 93 }

print("\nAll keys and values sorted by value:")

for pair in sorted(grades.items(), key=getGrade, reverse=True):
    print("Name: " + pair[0] + ", grade: " + str(pair[1]))