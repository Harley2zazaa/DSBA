"""SSS"""
import json
def main():
    x = json.loads(input())
    y = json.loads(input())
    z = json.loads(input())
    have_2 = False

    for j in z:
        if j in x and j in y:
            have_2 = True
            break
    if have_2:
        print("True")
        return
    print("False")
main()