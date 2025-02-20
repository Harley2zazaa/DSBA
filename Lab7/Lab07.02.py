import json
def selectionSort(list,last):
    com = 0
    for current in range(0,last):
        smallest = current #index
        walker = current+1 #index
        while walker <= last:
            com += 1
            if list[walker] < list[smallest]:
                smallest = walker
            walker += 1
        temp = list[current]
        list[current] = list[smallest]
        list[smallest] = temp
        print(list)
    print(f"Comparison times: {com}")

def main():
    selectionSort(json.loads(input()),int(input()))

main()