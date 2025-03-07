""""SS"""
import json
class Item():
    def __init__(self,name,price,weight):
        self.name = name
        self.price = int(price)
        self.weight = float(weight) 
    
    def get_name(self):
        return self.name
    
    def get_price(self):
        return self.price
    
    def get_weight(self):
        if self.weight % 1 == 0:
            return int(self.weight)
        return self.weight

    def get_cost(self):
        return self.get_price()/self.get_weight()
    
    def get_detail(self):
        return self.get_name()+" -> "+str(self.get_weight())+" kg -> "+str(self.get_price())+" THB"
    
def knapsack(itemList,amount): #ให้ได้มูลค่ารวมมากที่สุด
        total_money = 0
        item = []
        for i in range(0,len(itemList)):
            item.append([itemList[i],itemList[i].get_cost()])

        item.sort(key=lambda x:x[1],reverse=True)
        print(f"Knapsack Size: {amount} kg")
        print("===============================")
        for j in range(len(item)):
            if item[j][0].get_weight() <= amount:
                print(item[j][0].get_detail())
                total_money += item[j][0].get_price()
                amount -= item[j][0].get_weight()
        print(f"Total: {int(total_money)} THB")

def main():
    items = []
    num_items = int(input())
    while num_items != 0:
        item_in = json.loads(input())
        items.append(Item(item_in['name'], item_in['price'], item_in['weight']))
        num_items -= 1
    knapsack_capacity = float(input())
    knapsack(items, knapsack_capacity)
main()
