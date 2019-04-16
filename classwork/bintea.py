from classwork import Student,School,Teacher,bin
import pickle

def openclass():
    with open(dir[choice1] + "class", "rb") as f_read:
        f_read = pickle.load(f_read)
        for i in f_read:
            if choice2 == i.course.course_name:
                print(i.class_num)

def check():
    with open(dir[choice1] + "student", "rb") as f_read:
        f_read = pickle.load(f_read)
    for i in f_read:
        if class_choice == i.class_num.class_num:
            print(i.name)

for i in School.School.getSchoolList():
    print(i.city)
dir = {"beijing": "bj", "shanghai": "sh"}
choice1 = input("请输入你任教学校：")
with open(dir[choice1] + "course", "rb") as f_read:
        f_read = pickle.load(f_read)
        for i in f_read:
            print(i.course_name)
choice2 = input("请选择任教课程:")

flag =True
while flag:
    print("""
            1.选择上课班级
            2.查看学生列表
            3.修改成绩
            4.退出
            """)
    choice = input("请输入你的选择：")
    if choice == "1":
        openclass()
        class_choice = input("请选择上课班级：")
        print("选择完成！")
    if choice == "2":
        openclass()
        class_choice = input("请输入要查看的班级：")
        print("以下为该班级成员：")
        check()
    if choice == "3":
        openclass()
        class_choice = input("请输入修改同学的班级：")
        print("以下为该班级成员：")
        check()
        student_name = input("修改学生的姓名：")
        with open(dir[choice1] + "student", "rb") as f_read:
            f_read = pickle.load(f_read)
        new_score = input("输入修改的成绩：")
        for i in f_read:
            if student_name == i.name:
                i.score = new_score
        with open(dir[choice1] + "student", "wb") as f_write:
             pickle.dump(f_read,f_write)
             print("修改完成！")
    if choice == "4":
        flag = False
print("操作完成！")