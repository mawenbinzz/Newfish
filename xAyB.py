#!/usr/bin/env python3

from collection import Counter


def sameNum(fst,sec):
    """
    calculate same and different nums 
    """
    length = min(len(fst),len(sec))
    
    x = 0
    for index in range(length):
        if fst[index] == sec[index]:
            x += 1
            
    z = sum((Counter(fst) & Counter(sec)).values())
    
    return ("{}A{}B".format(x,(z-x)))

if __name__ == "__main__":
    fst_num = input().strip().split()
    sec_num = input().strip().split()
    print(sameNum(fst_num,sec_num))