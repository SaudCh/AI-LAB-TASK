class student:
    def __init__(self, name, regdNo,dept,cgpa,gender):
        self.name = name
        self.regdNo = regdNo
        self.dept = dept
        self.cgpa = cgpa
        self.gender = gender

#return true if found
def search(std,regd):
    for obj in std:
            if(regd==obj.regdNo):
                return True
    return False

std = []

choice = 1
while(choice!=0):

    choice = input("Press \n1 for add Student\n2 for view Student \n3 for view by regd N0 \n4 for Update Student \n5 for delete Student \nEnter Your choice: ")
    choice = int(choice)

    if(choice==1):
        regdNo = input("Enter regdNo: ")
        if(search(std,regdNo)):
            print("\n\nStudent Already exist\n\n")
        else:        
            name = input("Enter Name: ")
            dept = input("Enter Dept: ")
            cgpa = input("Enter Cgpa: ")
            gender = input("Enter gender: ")
            
            std.append( student(name,regdNo,dept,cgpa,gender) )

    elif(choice==2):
        for obj in std:
            print("Name: "+obj.name+" Regd No: "+obj.regdNo+" Dept: "+obj.dept+" CGPA: "+obj.cgpa+" Gender: "+gender)
    elif(choice==3):
        regd = input("Enter the Regd No: ")
        for obj in std:
            if(regd==obj.regdNo):
                print("Name: "+obj.name+" Regd No: "+obj.regdNo+" Dept: "+obj.dept+" CGPA: "+obj.cgpa+" Gender: "+gender)

    elif(choice==4):
        regd = input("Enter the Regd No: ")
        for obj in std:
            if(regd==obj.regdNo):
                obj.name = input("Enter Name: ")
                obj.regdNo = input("Enter regdNo: ")
                obj.dept = input("Enter Dept: ")
                obj.cgpa = input("Enter Cgpa: ")
                obj.gender = input("Enter gender: ")

    elif(choice==5):
        regd = input("Enter the Regd No: ")
        for idx, obj in enumerate(std):
            if(regd==obj.regdNo):
                del std[idx]