class person:

    def __init__(self,**op):
        self.fname = input("Enter first name:- ")
        self.mname = input("Enter middle name:- ")
        self.lname = input("Enter last name:- ")
        self.bday = input("Enter Birthdate:- ")
        self.mobile = int(input("Enter mobile no:- "))
        self.aadhar = int(input("Enter your aadhar number:- "))
        self.gender = input("Enter gender:- ")
        self.add = input("Enter address:- ")
        self.sym = "|"
        if (op.get('sym')):
            self.sym = op.get('sym')

    def __repr__(self):
        data = ""
        data += self.sym + ("-" * 47) + self.sym + "\n"
        data += self.sym + ("PERSON DETAILS".center(47)) + self.sym + "\n"
        data += self.sym + ("".center(47)) + self.sym + "\n"
        data += self.sym + ("FIRST NAME          : ".center(20) + str(self.fname).ljust(25) + self.sym ) + "\n"
        data += self.sym + ("MIDDLE NAME         : ".center(20) + str(self.mname).ljust(25) + self.sym) + "\n"
        data += self.sym + ("LAST NAME           : ".center(20) + str(self.lname).ljust(25) + self.sym) + "\n"
        data += self.sym + ("GENDER              : ".center(20) + str(self.gender).ljust(25) + self.sym) + "\n"
        data += self.sym + ("BIRHDATE            : ".center(20) + str(self.bday).ljust(25) + self.sym) + "\n"
        data += self.sym + ("MOBILE NO.          : ".center(20) + str(self.mobile).ljust(25) + self.sym) + "\n"
        data += self.sym + ("AADHAR NUMBER       : ".center(20) + str(self.aadhar).ljust(25) + self.sym) + "\n"
        data += self.sym + ("ADDRESS             : ".center(20) + str(self.add).ljust(25) + self.sym) + "\n"
        data += self.sym + ("-" * 47) + self.sym + "\n"
        return data

pr = person()
file = open("aadhar.txt","w")
file.write(str(pr))
file.close()
