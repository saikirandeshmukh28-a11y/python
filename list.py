list1=[1,2,3,4,6]
x=1
if x in list1:
    list1.remove(x)

list2=list1
list1[2:]=[7,8]
print(list2)
list2.append(12)
print(list2)
list1.extend([13,14])
list1.remove(2)
print(list1)


"""an example of list:"""

def factors(n):
    fact_list=[]
    for i in range(1,n+1):
        if n%i==0:
            fact_list.append(i)
    return(fact_list)
    
"n=12"
print(factors(12))

"search value in list"

def findpos(l,v):
    (found,i)=(False,0)
    while i < len(l):
        if not found and l[i] == v:
            found = True
            pos = i
        i += 1 
    if not found:
        pos=-1
    return pos

print(findpos([1,2,3,4,5,6],1))

"arrays vs lists:"
"the unsorted case:"
def search(l,v):
    for i in l:
        if i==v:
            return True
    return False

print(search([1,2,3,4,5],3))
