# gcd ->greatest common divisor 
# to find one k such that it divides both m and n

def gcd(m,n):
    fm=[] #factors of m ->fm
    for i in range(1,m+1):
        if(m%i==0):
            fm.append(i)
    
    fn=[]#factors of n->fn
    for j in range(1,n+1):
        if(n%j==0):
            fn.append(j)

    cf=[]#common factors->cf
    for f in fm:
        if f in fn:
           cf.append(f)
    
    return(cf[-1])
print(gcd(12,16))

'''
tracing
gcd(12,16)
fm=[1,2,3,4,6,12]
fn=[1,2,4,8,16]
cf=[1,2,4]
returns 4
'''