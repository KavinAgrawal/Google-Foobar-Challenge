sqrt_dec = 41421356237309504880168872420969807856967187537694807317667973799073247846210703885038753432764157273501
def series_sum(x):
    if(x == 1):
        return 1
    if(x<1):
        return 0
    first_t = x*(x+1)/2
    t2 = x*sqrt_dec//10**104
    second_t = x*t2
    third_t = t2*(t2+1)/2
    fourth_t = series_sum(t2)
    
    return first_t + second_t - third_t - fourth_t
    
def solution(s):
    x = long(s)
    return str(series_sum(x))
print(solution(77))