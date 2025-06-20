def commonSlot(a, b, d):
        
        arr=[]
        
        for i,j in a:
            if j-i<d:
                continue
            arr.append((i,j))
            
        for i,j in b:
            if j-i<d:
                continue
            arr.append((i,j))
            
        
        arr.sort()
        
        n=len(arr)
        
        for i in range(n-1):
            s1,e1=arr[i]
            s2,e2=arr[i+1]
            
            if s2<=e1 and e1<=e2:
                # overlapping=(s2,e1)
                if e1-s2>=d:
                    return [s2,s2+d]
                    
            if s2<=e1 and e1>=e2:
                #overlapping=(s2,e2)
                if e2-s2>=d:
                    return [s2,s2+d]
                
            
        return []
                
            
