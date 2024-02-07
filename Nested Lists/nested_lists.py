if __name__ == '__main__':
    name=[]
    score=[]
    for _ in range(int(input())):
        name.append(input())
        score.append(float(input()))
        
    arr=[]
    for i in range(len(name)):
        arr.append([name[i], score[i]])
    sorted_arr = sorted(arr, key=lambda x: x[1])
    k=sorted_arr[0][1]
    la=0
    sort=[]
    for i in sorted_arr:
        if i[1]==k:
            continue
        elif la==0 or la==i[1]:
            la = i[1]
            sort.append(i[0])
    sort=sorted(sort)
    for i in sort:
        print(i)
