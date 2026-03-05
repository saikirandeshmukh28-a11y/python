# euclids algorithm

def gcd(m,n):
    #assume m>=n
    if m<n:
        (m,n)=(n,m)
    if(m%n)==0:
        return(n)
    else:
        diff=m-n #diff>n?possible!
        return(gcd(max(n,diff),min(n,diff)))
    
print(gcd(12,16))

"""
tracing:
gcd(12,16)
12<16->16,12->16-12=4->
max(12,4),min(12,4)->max->12
min->4
gcd(max,min)
gcd(12,4)
again calls the m,n->the answer would be 4
"""