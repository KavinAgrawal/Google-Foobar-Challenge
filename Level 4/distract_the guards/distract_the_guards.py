import math
def solution(banana_list):
    pair_dict = {}
    
    for i in range(len(banana_list)):
        pair_dict[i]=[]
        
    for i in range(len(banana_list)):
        for j in range(i+1,len(banana_list)):
            
            node = set()
            x = banana_list[i]
            y = banana_list[j]
            if(x!=y):            
                tem = x
                x = min(x,y)
                y = max(tem,y)
                if((x+y)%2!=0 or (x==0 and y!=0)):
                    pair_dict[i].append(j)
                    continue
                n = math.ceil(math.log((y+x)/(2*x),2))
                y = y - x*(math.pow(2,n)-1)
                x = x + x*(math.pow(2,n)-1)
                if(x!=y):
                    pair_dict[i].append(j)
          
    guard = []
    for i in range(len(banana_list)):
        for x in pair_dict[i]:
            inc = True
            for t in guard:
                if(i not in t and x not in t):
                    t.append(i)
                    t.append(x)
                    inc = False
            if(inc):
                guard.append([i,x])
        
    count = 0
    for t in guard:
        count = max(count,len(t))
    return len(banana_list)-count
print(solution([1, 1]))
