def Mean(l):               #function to return mean
    mean=sum(l)/len(l)
    mean=round(mean,1)
    return mean

def Median(l):             #fuction to return median
    N=len(l)
    p=sorted(l)
    if(N%2==0):
        k=int((N-1)/2)
        s=int((N+1)/2)
        median=(p[k]+p[s])/2.0
        median=round(median,1)
    
    else:
        median=l[int(N/2)]
        median=round(median,1)
    return median

def Mode(l):               #function to return mode
    p=sorted(l)
    q=[]
    d={}
    for i in range(len(l)):
        d[p[i]]=p.count(p[i])
    #     print(d)    
    for x in d.values():
        q.append(x)
    #     print(q)
    if(len(d)==len(p)):
        mode = p[0]
    else:
        for key,value in d.items():
            if(value==max(q)):
                mode=key
                break
    return mode    

if __name__=="__main__":
    N= int(input())
    X=list(map(int, input().split()))
    print(Mean(X))
    print(Median(X))
    print(Mode(X))


