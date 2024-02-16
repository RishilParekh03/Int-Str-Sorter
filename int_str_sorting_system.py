def sorter(ls):
    intList = []
    strList = []

    for j in range(len(ls)):
        if ls[j].isdigit():
            intList.append(int(ls[j]))
        else:
            strList.append(ls[j])
    
    print(f"\nInt List={intList}\nMin Value={min(intList)}\nMax Value={max(intList)}")
    
    return intList, strList

def strOpeartion(strList):
    for k in range(len(strList)):
        if strList[k].isupper():
            temp = strList[k].lower()
            strList.pop(k)
            strList.insert(k,temp)
    
    print(f"\nStr List={strList}")
    return strList


ls = []
num = int(input("Enter the number of elements: "))

for i in range(num):
    ls.append(input(f"Enter the element at {i}: "))

print(f"\nList={ls}")

intList, strList = sorter(ls)
strOpeartion(strList)