from classwork import Course,Class,Teacher

class School:
    __school_list = []
    def __init__(self,city):
        self.city = city
        self.course_list = []
        self.class_list = []
        self.teacher_list = []

    @staticmethod
    def getSchoolList():
        return School.__school_list

    def courseBuild(self,course_name,duration,price):
        new_course = Course.Course(course_name,duration,price)
        self.course_list.append(new_course)
        return new_course

    def classBuild(self,class_num,course,teacher):
        new_class = Class.Class(class_num,course,teacher)
        self.class_list.append(new_class)
        return new_class

bj_school = School("beijing")
School.getSchoolList().append(bj_school)
sh_school = School("shanghai")
School.getSchoolList().append(sh_school)

linux = bj_school.courseBuild("linux","6months",4000)
python = bj_school.courseBuild("python","6months",5000)
go = sh_school.courseBuild("go","6months",4500)

teacher1 = Teacher.Teacher("wang",40,linux,bj_school)
teacher2 = Teacher.Teacher("li",35,python,bj_school)
teacher3 = Teacher.Teacher("qi",33,go,sh_school)
bj_school.teacher_list.append(teacher1)
bj_school.teacher_list.append(teacher2)
sh_school.teacher_list.append(teacher3)

class1 = bj_school.classBuild("class1",linux,teacher1)
class2 = bj_school.classBuild("class2",python,teacher2)
class3 = sh_school.classBuild("class3",go,teacher3)





