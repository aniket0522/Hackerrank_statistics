#Weighted_mean
def weighted_mean(u,v):
    wx=[]
    for i in range(N):
        c=u[i]*v[i]
        wx.append(c)
    wm=float(sum(wx)/sum(v)) 
    # wm=round(wm,1)
    return round(wm,1)  
    
if __name__ == '__main__':
    N=int(input())
    X=list(map(int, input().split()))
    W=list(map(int, input().split()))
    print(weighted_mean(X,W))


