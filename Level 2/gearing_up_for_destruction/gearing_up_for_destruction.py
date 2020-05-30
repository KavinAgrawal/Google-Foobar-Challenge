def solution(pegs):
    count=-1
    x = 0
    for i in range(len(pegs)):
        if(i==0 or i==len(pegs)-1):
            x = x + count*pegs[i]
        else:
            x = x + 2*count*pegs[i]

        count = count*-1
    if(len(pegs)%2==0):
        t=2*x/3
    else:
        t=2*x
    if(t<1):
        return [-1,-1]
    r=t
    for i in range(len(pegs)-1):
        r = pegs[i+1]-pegs[i]-r
        if(r<1):
            return [-1,-1]
        else:
            continue;
    if(x%3==0 and len(pegs)%2==0):
        return [2*x/3,1]
    elif(x%3!=0 and len(pegs)%2==0):
        return [2*x,3]
    else:
        return [2*x,1]

print(solution([4,30,50]))
