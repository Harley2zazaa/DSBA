"""Student Id"""
def main():
    """SS"""
    all = []
    for _ in range(3):
        name = input()
        gender = input()
        age = input()
        id = input()
        gpa = f'{float(input()):.2f}'
        lisa = [name,gender,age,id,gpa]
        all.extend([lisa])
    need = input()
    your_name =''
    for i in range(3):
        if all[i][3] == need:
            if all[i][1] == 'Male':
                your_name = f'Mr {all[i][0]} ({all[i][2]}) ID: {all[i][3]} GPA {all[i][4]}'
            else:
                your_name = f'Miss {all[i][0]} ({all[i][2]}) ID: {all[i][3]} GPA {all[i][4]}'
    if your_name == '':
        your_name = "Student not found"
    print(your_name)

main()
