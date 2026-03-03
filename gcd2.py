#no list
def gcd(m,n):
    for i in range(1,min(m,n)+1):
        if ((m%i)==0) and ((n%i)==0):
            k=i
    return k

print(gcd(12,16))

"""
tracing:
gcd(12,16)
i->> (1,12+1)-->(1,13)
k=4
reutrns 4
""" 