"""SS"""
import json
class Student():
    def __init__(self,std_id:int,name:str,gpa:float):
        self.stu_id = std_id
        self.name = name
        self.gpa = gpa

    def get_std_id(self):
        return self.stu_id
    
    def get_name(self):
        return self.name
    
    def get_gpa(self):
        return f"{self.gpa:.2f}"
    
    def print_details(self):
        print(f"ID: {self.get_std_id()}")
        print(f"Name: {self.get_name()}")
        print(f"GPA: {self.get_gpa()}")

def main():
    x = json.loads(input())
    y = Student(x["ID"],x["Name"],x["GPA"])
    y.print_details()
main()