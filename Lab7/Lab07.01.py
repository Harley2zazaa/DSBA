import json
def insertionSort(list,last):
    compare_time = 0
    for i in range(1,last+1):
        ####
        hold = list[i]
        walker = i-1
        while walker >= 0: #compare
            compare_time += 1 # add compare time
            if hold < list[walker]:
                list[walker+1] = list[walker] # move walker
                walker -= 1 ## desrement walker
            else:
                break
        list[walker+1] = hold # move hold -> walker+1
        print(list)
    print(f"Comparison times: {compare_time}") # Big O = O(n^2)
def main():
    insertionSort(json.loads(input()),int(input()))
    
main()

























