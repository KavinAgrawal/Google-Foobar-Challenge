from copy import deepcopy

def dfs(map,wall,x,y,steps,used,min_Steps):
    w = len(map[0])-1
    h = len(map)-1
    if(x==h and y==w ):
        min_Steps[0] = min(steps,min_Steps[0])
        return
    if(steps<min_Steps[0]):
            pos = [[1,0],[0,1],[-1,0],[0,-1]]
            used = deepcopy(used)
            used[x][y]=0
            for i in range(4):
                t = x + pos[i][0]
                u = y + pos[i][1]
                if(0<= t<=h and 0<=u <=w):
                    if(used[t][u]==1):
                        if(map[t][u] == 1 and wall==1):
                            dfs(map,0,t,u,steps+1,used,min_Steps)
                        elif(map[t][u] == 0):
                            dfs(map,wall,t,u,steps+1,used,min_Steps)
            del used
    return
            
def solution(map):
    used = []
    for m in map:
        t = []
        for x in m:
            t.append(1)
        used.append(t)
    used[0][0]=0
    min_Steps= [len(map)*len(map[0])]
    dfs(map,1,0,0,1,used,min_Steps)
    return min_Steps[0]

maze = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]
print(solution(maze))
