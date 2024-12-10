"""SSS"""
class Information:
    def __init__(self,name:str,gender:str,age:int,student_id:str,gpa:float): # XXX:___ typehint
        """main"""
        self.name = name
        self.gender = gender
        self.age = int(age)
        self.student_id = student_id
        self.gpa = float(gpa)

    def __str__(self):
        return self.display()

    def display(self):
        if self.gender == "Male":
            return f"Mr {self.name} ({self.age}) ID: {self.student_id} GPA {self.gpa:.2f}"
        else:
            return f"Miss {self.name} ({self.age}) ID: {self.student_id} GPA {self.gpa:.2f}"
        
def main():
    """SSS"""
    list_name = []
    for _ in range(3):
        student = Information(input(),input(),input(),input(),input())
        list_name.append(student)
    needed  = input()
    for student in list_name:
        if student.student_id == needed:
            print(student)
            return
    print("Student not found")
main()
# Panavat Thamcharoen
# Male
# 22
# 66070113
# 2.21