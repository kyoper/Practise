# import pickle
# class Course:
#     def __init__(self,duration,price):
#         self.duration = duration
#         self.price = price
#
#
# class School:
#     def __init__(self,city):
#         self.city = city
#         self.course_list = []
#
#
#     def courseBuild(self,duration,price):
#         courseObj = Course(duration,price)
#         self.course_list.append(courseObj)
#         return self.course_list
#
# schoola = School("北京")
# schoola.courseBuild("6months",5000)
# print(schoola.course_list)
#
# with open("course","wb") as f:
#     pickle.dump(schoola.course_list,f)

def f(a):
    for i in range(7):
        a+=7

a = 1
f(a)
for i in range(1,4):
    print(i)
print(a)
