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
            word_wa,num_wa= list[walker][0],int(list[walker][1:])
            word_wb,num_wb = list[walker-1][0],int(list[walker-1][1:])
            if word_wa < word_wb or (word_wa == word_wb and num_wa < num_wb):
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