import json
def bubbleSort(list,last):
    sorted = False
    current = 0
    com = 0
    while current <= last and sorted == False:
        walker = last
        sorted = True
        while walker > current:
            com += 1
            if list[walker] < list[walker-1]:
                sorted = False
                temp = list[walker]
                list[walker] = list[walker-1] # swap
                list[walker-1] = temp
            
            walker -= 1
        print(list)
        current += 1
    print(f"Comparison times: {com}")

def main():
    bubbleSort(json.loads(input()),int(input()))

main()