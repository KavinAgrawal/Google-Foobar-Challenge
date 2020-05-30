import math
def distance_cal(x,y):
    return math.sqrt(((x[0]-y[0])**2)+((x[1]-y[1])**2))

def sign(x):
    if(x%2==0):
        return -1
    else:
        return 1

def mirror_gen(distance, dimensions, your_position, guard_position):
    guardpos = []
    selfpos = []
    for x in range(-(distance//dimensions[0])-1,(distance//dimensions[0])+2):
        for y in range(-(distance//dimensions[1])-1,(distance//dimensions[1])+2):
            sgx = sign(x)
            sgy = sign(y)
            mx = (x+1)//2
            my = (y+1)//2
            gp = [mx*2*dimensions[0]-sgx*guard_position[0], my*2*dimensions[1]-sgy*guard_position[1]]
            sp = [mx*2*dimensions[0]-sgx*your_position[0], my*2*dimensions[1]-sgy*your_position[1]]

            gd=distance_cal(gp,your_position)
            gs=math.atan2(gp[1]- your_position[1],gp[0]- your_position[0])
            guardpos.append([gd,gs])
            
            sd=distance_cal(sp,your_position)
            ss=math.atan2(sp[1]- your_position[1],sp[0]- your_position[0])
            selfpos.append([sd,ss])

    return (guardpos,selfpos)

def solution(dimensions, your_position, guard_position, distance):
    guard_arr = []
    self_arr = []
    (guard_arr,self_arr) = mirror_gen(distance,dimensions, your_position, guard_position)

    righthit=set()
    dist_ang = {}
    
    for sel in self_arr:
        if(sel[0] != 0 and sel[0]<=distance):
            if(sel[1] not in dist_ang.keys() or (sel[1] in dist_ang.keys() and dist_ang[sel[1]]>sel[0])):
                dist_ang[sel[1]] = sel[0]
    for guard in guard_arr:
        if(guard[0] != 0 and guard[0]<=distance):
            if(guard[1] not in dist_ang.keys() or (guard[1] in dist_ang.keys() and dist_ang[guard[1]]>guard[0])):
                dist_ang[guard[1]] = guard[0]
                righthit.add(guard[1])

    return len(righthit)

print(solution([3,2], [2,1], [1,1], 4))
