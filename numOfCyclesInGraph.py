n,m=[int(x) for x in input().split()]

adj=[[]for _ in range(n)]

for i in range(m):
    u,v=[int(x) for x in input().split()]
    adj[u].append(v)
    adj[v].append(u)
    
def numcycles(adj,n):
    visited=[False]*n
    pathVisited=[False]*n
    dist=[0]*n
    ans=[0,0]
    for i in range(n):
        if not visited[i]:
            dfs(i,-1,adj,visited,pathVisited,dist,ans)
            
    return ans[1]
            
            
            
def dfs(start,par,adj,visited,pathVisited,dist,ans):
        visited[start]=True
        pathVisited[start]=True
        for neighbour in adj[start]:
            if not visited[neighbour]:
                dist[neighbour]=dist[start]+1
                dfs(neighbour,start,adj,visited,pathVisited,dist,ans)
            elif neighbour!=par and pathVisited[neighbour]:
                ans[0]=max(ans[0],dist[start]+1-dist[neighbour])
                # print(neighbour,start,par)
                ans[1]+=1
                
        pathVisited[start]=False
                
print(numcycles(adj,n))
