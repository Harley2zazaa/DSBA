import json
def selectionSort(list,last):
    com = 0
    for current in range(0,last):
        smallest = current #index
        walker = current+1 #index
        while walker <= last:
            com += 1
            word_w,num_w = list[walker][0],list[walker][1:]
            word_sm,num_sm = list[smallest][0],list[smallest][1:]
            if word_w < word_sm or (word_w == word_sm and int(num_w) < int(num_sm)):
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