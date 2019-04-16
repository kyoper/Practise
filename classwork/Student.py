from classwork import School
class Student:
    def __init__(self,name,city,class_num):
        self.city = city
        self.name = name
        self.score = 0
        self.is_tuition =False
        self.class_num = class_num

    def test(self,score):
        self.score = score
        return self.score

    def tuition(self):
        self.is_tuition = True


