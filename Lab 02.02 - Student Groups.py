"""Lab 02.02 - Student Groups"""
import math
class ArrayStack:
    def __init__(self) :
        self.size = 0
        self.data = list()

    def push(self, input_data):
        """Stack"""
        try:
            if input_data.isdigit():
                input_data = int(input_data)
            elif input_data.replace(".", "", 1).isdigit():
                input_data = float(input_data)
        except (TypeError, ValueError, ArithmeticError, AttributeError):
            pass
        finally:
            self.data.append(input_data)
            self.size += 1
    def pop(self):
        if self.size != 0:
            x = self.data.pop()
            self.size -= 1
            return x
        else:
            print("Underflow: Cannot pop data from an empty list")

    def print_stack(self):
        print(self.data)

def main():
    many_group = int(input())
    all_student = int(input())
    max_per_group = math.ceil(all_student/many_group)
    Temp = ArrayStack()
    for _ in range(all_student):
        Temp.push(input())
    
    groups = list(list() for _ in range(many_group))

    for i in range(max_per_group):
        for j , data in enumerate(groups):
            if Temp.size == 0:
                break
            data.append(Temp.pop())

    for index , now in enumerate(groups):
        print(f"Group {index+1}:", end=" ")
        for i, dataw in enumerate(now):
            if i == len(now) - 1:
                print(dataw, end="")
            else:
                print(dataw, end=", ")
        print()

main()