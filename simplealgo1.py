def f(x):
    d=0
    while x>1:
        (x,d)=(x/2,d+1)
    return(d)

print(f(2))  
"""
tracing:
f(2)
2>1
2/2=1
d=1
x,d=1,1
return 1
"""