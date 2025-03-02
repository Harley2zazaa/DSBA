
import json

def findStations(all_city,number_radio):
    use = []
    must = []
    for i in range(number_radio):
        use.append(json.loads(input()))

    while all_city:
        use.sort(key=lambda x: (len(set(x["Cities"]).intersection(set(all_city)))), reverse=True)
        if not use:
            break

        find = use[0] # most macth
        count = set(find["Cities"]).intersection(set(all_city))

        if count:
            must.append(find["Name"])
            all_city = list(set(all_city).difference(count))
        
        use = use[1:] #del seclected
    must.sort()
    print(must)

def main():
    findStations(json.loads(input()),int(input()))

main()
