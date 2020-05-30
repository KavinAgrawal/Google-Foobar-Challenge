def solution(l):
    arr = []
    count = []
    for i in range(len(l)):
        c = 0
        a = []
        for j in range(i+1,len(l)):
            if(l[j]%l[i] == 0):
                c += 1
                a.append(j)
        arr.append(a)
        count.append(c)

    val = 0
    for i in range(len(l)):
        for j in arr[i]:
            val += len(arr[j])
    return val
print(solution([1, 2,4,8,12]))
