from classwork import Student,School,Teacher,bin
import pickle
flag = True
while flag:
    print("""
     ------------
        1.报名
        
        2.退出
     ------------  
        """)
    choose = input("输入你的选择:")
    if choose == "1":
        name = input("请输入你的姓名")
        print("""
            1.beijing
            2.shanghai""")
        dic = {"beijing":"bj","shanghai":"sh"}
        city = input("输入哪所学校：")
        with open(dic[city]+"course","rb") as f_read:
            for i in pickle.load(f_read):
                print(i.course_name)
        choose1 = input("请选择课程：")
        with open(dic[city]+"course","rb") as f_read:
            for i in pickle.load(f_read):
                if choose1 == i.course_name:
                    print("请交学费 %d 元"%i.price)
        with open(dic[city]+"class","rb") as f_read1:
            f_read1 = pickle.load(f_read1)
            for i in f_read1:
                if i.course.course_name == choose1:
                    print(i.class_num)
        choose2 = input("请选择班级：")
        with open(dic[city]+"class","rb") as f_read1:
            f_read1 = pickle.load(f_read1)
            for i in f_read1:
                if choose2 == i.class_num:
                    new_student = Student.Student(name,city,i)
                    i.teacher.student_list.append(new_student)

                    bin.serialize(dic[city]+"student",i.teacher.student_list,0)
                    print("操作成功！")

    if  choose == "2":
        break
print("谢谢使用！")