"""Coin"""
import json
def coin_Exchange(amount = int,coin_list = dict):
    temp = amount
    amount_10,amount_5,amount_2,amount_1 = coin_list["10"],coin_list["5"],coin_list["2"],coin_list["1"]
    use_10,use_5,use_2,use_1 = 0,0,0,0
    while amount > 0:
        if amount >= 10 and amount_10 > 0:
            amount -= 10
            use_10 += 1
            amount_10 -= 1
        elif amount >= 5 and amount_5 > 0:
            amount -= 5
            use_5 += 1
            amount_5 -= 1
        elif amount >= 2 and amount_2 > 0:
            amount -= 2
            use_2 += 1
            amount_2 -= 1
        elif amount >= 1 and amount_1 > 0:
            amount -= 1
            use_1 += 1
            amount_1-= 1
        else:
            break
        
    if amount > 0:
        print(f"Amount: {temp}")
        print("Coins are not enough.")
        return
    print(f"Amount: {temp}")
    print("Coin exchange result:")
    print(f"  10 baht = {use_10} coins")
    print(f"  5 baht = {use_5} coins")
    print(f"  2 baht = {use_2} coins")
    print(f"  1 baht = {use_1} coins")
    print(f"Number of coins: {use_10+use_5+use_2+use_1}")

def main():

    coin_Exchange(int(input()),json.loads(input()))

main()