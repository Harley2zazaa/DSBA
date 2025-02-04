"""SSSSS"""
def main(num):
    Press_Count = 0
    if num == 1:
        print('1')
        return
    for i in range(1, num+1,1):
        Press_Count += len(str(i))+1 # number(count ตน.) and  operator (1)
    print(Press_Count)
main(int(input()))
