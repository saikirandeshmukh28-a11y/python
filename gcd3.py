#no list and for loop
def gcd(m,n):
    i=min(m,n)
    while i>0:
        if (m%i)==0 and (n%i)==0:
            return(i)
        else:
            i=i-1

print(gcd(12,16))

"""
tracing:
gcd(12,16)
i=12 ->> 12>0 returns false 
i=11->> 11>0 returns false 
i=10->> 10>0 returns false 
i=9->> 9>0 returns false 
i=8->> 8>0 returns false 
i=7->> 7>0 returns false 
i=6->> 6>0 returns false 
i=5->> 5>0 returns false 
i=4->> 4>0 returns true 
returns 4
"""