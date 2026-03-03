#refined gcd.py
def gcd(m,n):
    cf=[]#common factors->cf
    for i in range(1,min(m,n)+1):
        if ((m%i)==0) and ((n%i)==0):
            cf.append(i)
    return (cf[-1])

print(gcd(12,16))

"""
tracing:
gcd(12,16)
i->> (1,12+1)-->(1,13)
cf=[1,2,4]
reutrns 4
"""