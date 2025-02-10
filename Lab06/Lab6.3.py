"""SSS"""
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
    temp = json.loads(input())
    Data = []
    for i in range(len(temp)):
        x = Student(temp[i]["id"], temp[i]["name"], temp[i]["gpa"])
        Data.append(x)
    Need = input()
    begin = 0
    end = len(Data)-1
    compare = 0
    while begin <= end:
        mid = (begin+end)//2
        compare += 1
        if Need > Data[mid].get_name():
            begin = mid +1
        elif Need < Data[mid].get_name():
            end = mid -1
        else:
            begin = end +1
    if Need == Data[mid].get_name():
        print(f"Found {Need} at index {mid}")
        Data[mid].print_details()
        print(f"Comparisons times: {compare}")
    else:
        print(f"{Need} does not exists.")
        print(f"Comparisons times: {compare}")
main()
