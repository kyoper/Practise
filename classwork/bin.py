from classwork import School,Class,Course,Teacher
import pickle
"""序列化函数"""
def serialize(flie_txt,list,k):
    with open(flie_txt, "rb") as f_read:
        try:
            f_read= pickle.load(f_read)
        except EOFError:
            with open(flie_txt,"wb+") as f_write:
                 pickle.dump(list,f_write)
        else:
            if k < len(list):
                 for i in list[k:]:
                     f_read.append(i)
            with open(flie_txt,"wb") as f_write:
                pickle.dump(f_read,f_write)

def bin():
    flag = True
    while flag:
        print("""请输入你的选项
            1.创建讲师
            2.创建课程
            3.创建班级
            4.退出""")

        choose = input("请输入你的选择：")
        if choose =="1":
                name = input("请输入姓名:")
                age = input("请输入年龄：")
                for i in School.School.getSchoolList():
                    print(i.city)
                choose = input("请输入城市：")
                for i in School.School.getSchoolList():
                    if choose == i.city:
                        for j in i.course_list:
                            print(j.course_name)
                        course = input("请输入课程:")
                        if choose == i.city:
                            for j in i.course_list:
                                if course == j.course_name:
                                    course = j
                        new_teacher = Teacher.Teacher(name,age,course,i)
                        i.teacher_list.append(new_teacher)


        if choose =="2":
                print("""
                1.beijing
                2.shanghai
                    """)
                choose = input("哪所学校创建课程：")
                for i in School.School.getSchoolList():
                    if choose == i.city:
                        course_name = input("输入课程名：")
                        duration = input("输入周期：")
                        price = int(input("输入费用："))
                        i.courseBuild(course_name,duration,price)

        if choose == "3":
                print("""
                    1.beijing
                    2.shanghai
                        """)
                choose = input("哪所学校创建班级：")
                for i in School.School.getSchoolList():
                    if choose == i.city:
                        class_num = input("输入班级号")
                        for j in i.course_list:
                            print(j.course_name)
                choose1 = input("输入本班的课程：")
                for i in School.School.getSchoolList():
                    if choose == i.city:
                        for j in i.course_list:
                            if choose1 ==j.course_name:
                                course = j
                for i in  School.School.getSchoolList():
                    if choose == i.city:
                        for j in i.teacher_list:
                            if j.course.course_name == choose1:
                                print(j.name)
                choose3 = input("输入谁来任教:")
                for i in School.School.getSchoolList():
                    if choose == i.city:
                        for j in i.teacher_list:
                            if choose3 == j.name:
                                teacher = j
                                i.classBuild(class_num,course,teacher)

        if choose =="4":
            flag =False
    """ 以下使用序列化函数 """
    serialize("bjcourse",School.bj_school.course_list,2)
    serialize("bjclass",School.bj_school.class_list,2)
    serialize("bjteacher",School.bj_school.teacher_list,2)
    serialize("shcourse",School.sh_school.course_list,1)
    serialize("shclass",School.sh_school.class_list,1)
    serialize("shteacher",School.sh_school.teacher_list,1)

    print("谢谢使用！")

if __name__ == "__main__":
    bin()
    #
    # with open("bjstudent","rb") as f:
    #     f = pickle.load(f)
    #     for i in f:
    #         if i.class_num.course.course_name == "linux" and i.name == "kyoper":
    #             print(i.score)