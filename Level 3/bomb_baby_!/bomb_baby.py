def solution(x,y):
    m = max(int (x), int (y))
    f = min(int (x), int (y))
    count = 0
    while(True):
        if( f<1):
            return "impossible"
        elif ( f == 1 ):
            count += (m/f) -1
            return str(int(count))
        d = m//f
        q = m%f
        m = f
        f = q
        count += d
    return
print(solution('4', '7'))
