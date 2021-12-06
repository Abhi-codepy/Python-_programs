import os
files = os.walk(r"C:\Users\ABHISHEK SINGH\PycharmProjects\Project2\Result")
length = 0
for(root,d,file) in files:
    length = len(file)
    break
try:
    f = open(r"Result/student_ "+str(length+1)+".txt","w")
    s_name = input("Enter Student name : ")
    s_roll = input("Enter Student Roll no : ")
    s_add = input("Enter Student address: ")
    s_gen = input("Enter Gender: ")
    s_fa = input("Enter Father's name: ")
    s_mo = input("Enter Mother's name: ")
    subj = ["C++", "SQl", "PYTHON", "PHP"]
    subj[0] = int(input("Enter C++ marks: "))
    subj[1] = int(input("Enter SQL marks: "))
    subj[2] = int(input("Enter PYTHON marks: "))
    subj[3] = int(input("Enter PHP marks: "))
    sub1 = input("Enter C++ Grade: ")
    sub2 = input("Enter SQL Grade: ")
    sub3 = input("Enter PYTHON Grade: ")
    sub4 = input("Enter PHP Grade: ")
    add = subj[0] + subj[1] + subj[2] + subj[3]
    per = (add * 100) / 400
    def marks(**op):
        sym = "|"
        if (op.get("sym")):
            sym = op.get("sym")
        f.write("_" * 80+"\n")
        f.write(sym + "STUDENT REPORT CARD".center(78) + sym+"\n")
        f.write(sym + "".center(78) + sym+"\n")
        f.write(sym + "Name of Student     : ".center(20) + str(s_name).ljust(25) + "Roll No         :".center(20) + str(s_roll).ljust(11) + sym+"\n")
        f.write(sym + "Mother's Name       : ".center(19) + str(s_mo).ljust(25) + "Gender          :".center(20) + str(s_gen).ljust(11) + sym+"\n")
        f.write(sym + "father's Name       : ".center(20) + str(s_fa).ljust(27) + "                             " + sym+"\n")
        f.write(sym + "Address             : ".center(20) + str(s_add).ljust(27) + "                             " + sym+"\n")
        f.write("_" * 80+"\n")
        f.write(sym + "SUBJECT CODE".center(20) + sym + "SUBJECT NAME".center(20) + sym + "MARKS".center(18) + sym + "GRADE".center(17) + sym+"\n")
        f.write("-" * 80+"\n")
        f.write(sym + "333301".center(20) + sym + "C++".center(20) + sym + str(subj[0]).center(18) + sym + sub1.center(17) + sym+"\n")
        f.write(sym + "333302".center(20) + sym + "SQL".center(20) + sym + str(subj[1]).center(18) + sym + sub2.center(17) + sym+"\n")
        f.write(sym + "333303".center(20) + sym + "PYTHON".center(20) + sym + str(subj[2]).center(18) + sym + sub3.center(17) + sym+"\n")
        f.write(sym + "333304".center(20) + sym + "PHP".center(20) + sym + str(subj[3]).center(18) + sym + sub4.center(17) + sym+"\n")
        f.write("-" * 80+"\n")
        f.write(sym + "TOTAL MARKS".center(20) + ":" + str(add).center(20) + sym + "PERCENTAGE".center(18) + ":" + str(per).center(17) + sym+"\n")
        f.write("-" * 80+"\n")
    marks()
except Exception as e:
    print(e)