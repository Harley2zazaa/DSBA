"""Max…Min…Avg"""
import json
def main():
    """SSSS"""
    listt = json.loads(input())
    long = len(listt)
    hightest = 0
    lowest = float(listt[0])
    avg = 0
    for i in range(long):
        if float(listt[i]) > hightest:
            hightest = float(listt[i])
    for j in range(long):
        if float(listt[j]) < lowest:
            lowest = float(listt[j])
    for z in range(long):
        avg += listt[z]
    print(f'({hightest:.2f}, {lowest:.2f}, {(avg/long):.2f})')
main()
