"""SSS"""
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

class ProbHash():
    def __init__(self,size:int):
        self.size = size
        self.hash_table = [None] * size #จองพท.

    def hash_code_table(self):
        pass
    
    def hash(self,key):
        return key%self.size

    def rehash(self,key):
        original_key = key
        while self.hash_table[key] is not None:
            key = (key + 1) % self.size
            if key == original_key:
                return None #Full
        return key

    def insert_data(self,std:Student):
        temp = self.hash(std.get_std_id()) #find index
        if self.hash_table[temp] is not None: #ถ้ามี data
            temp = self.rehash(temp)
            if temp is None:
                print(f"The list is full. {std.get_std_id()} could not be inserted.")
                return
        self.hash_table[temp] = (std.get_std_id(),std)
        print(f"Insert {std.get_std_id()} at index {temp}")

    def search_data(self,std_id):
        for i in range(self.size):
            if self.hash_table[i] is not None and self.hash_table[i][0] == std_id:
                print(f"Found {std_id} at index {i}")
                self.hash_table[i][1].print_details()
                return
        print(f"{std_id} does not exist.")
def main():
    import json
    size = int(input())
    hashtable = ProbHash(size)
    while True:
        finish = input()
        if finish == "Done":
            break
        condition, data = finish.split(" = ")
        if condition == "I":
            std_in = json.loads(data)
            std = Student(std_in["ID"], std_in["Name"], std_in["GPA"])
            hashtable.insert_data(std)
        elif condition == "S":
            print("------")
            student = hashtable.search_data(int(data))
            if student is not None:
                student.print_details()
            print("------")
        else:
            print("Invalid Condition!")
main()