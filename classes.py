# Complete the functions below.

classes = {}
students = {}


class Course:
    def __init__(self, id, capacity, time):
        self.id = id
        self.capacity = capacity
        self.time = time
        self.students = []

    def __str__(self):
        return str(self.id)


class Student:
    def __init__(self, id, capacity, start, finish):
        self.id = id
        self.capacity = capacity
        self.start = start
        self.finish = finish
        self.courses = []

    def __str__(self):
        return str(self.id)


def addClass(id, capacity, time):
    if id in classes:
        return "Error adding class " + str(id)
    classes[id] = Course(id, capacity, time)
    return "Successfully added class " + str(id)


def removeClass(id):
    if id in classes:
        for student in classes[id].students:
            unenrollStudent(student.id, id)
        del classes[id]
        return "Successfully removed class " + str(id)
    return "Error removing class " + str(id)


def infoClass(id):
    if id not in classes:
        return "Class " + str(id) + " does not exist"
    elif len(classes[id].students) == 0:
        return "Class " + str(id) + " is empty"
    else:
        sorted_students = sorted(classes[id].students, key=lambda student:student.id)
        return "Class " + str(id) + " has the following students: "  + ",".join([str(student) for student in sorted_students])


def addStudent(id, capacity, start, end):
    if id in students:
        return "Error adding student " + str(id)
    students[id] = Student(id, capacity, start, end)
    return "Successfully added student " + str(id)


def removeStudent(id):
    if id in students:
        for course in students[id].courses:
            unenrollStudent(id, course.id)
        del students[id]
        return "Successfully removed student " + str(id)
    return "Error removing student " + str(id)


def infoStudent(id):
    if id not in students:
        return "Student " + str(id) + " does not exist"
    if len(students[id].courses) == 0:
        return "Student " + str(id) + " is not taking any classes"
    sorted_courses = sorted(students[id].courses, key=lambda course:course.id)
    return "Student " + str(id) + " is taking the following classes: " + ",".join([str(course) for course in sorted_courses])


def enrollStudent(studentId, classId):
    if studentId not in students:
        pass
    elif classId not in classes:
        pass
    elif classId in [course.id for course in students[studentId].courses]:
        pass
    elif len(students[studentId].courses) >= students[studentId].capacity:
        pass
    elif len(classes[classId].students) >= classes[classId].capacity:
        pass
    elif students[studentId].start > classes[classId].time or students[studentId].finish < classes[classId].time:
        pass
    elif classes[classId].time in [course.time for course in students[studentId].courses]:
        pass
    else:
        classes[classId].students.append(students[studentId])
        students[studentId].courses.append(classes[classId])
        return "Number of free spots left in class " + str(classId) + ": " + str(classes[classId].capacity - len(classes[classId].students))
    return "Enrollment of student " + str(studentId) + " in class " + str(classId) +" failed"


def unenrollStudent(studentId, classId):
    if studentId not in students:
        pass
    elif classId not in classes:
        pass
    elif classId not in [course.id for course in students[studentId].courses]:
        pass
    else:
        classes[classId].students.remove(students[studentId])
        students[studentId].courses.remove(classes[classId])
        return "Number of free spots left in class " + str(classId) + ": " + str(classes[classId].capacity - len(classes[classId].students))
    return "Unenrollment of student " + str(studentId) + " in class " + str(classId) +" failed"
