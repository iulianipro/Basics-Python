#Fibonacci Numbers and Lines

def fibRic(n): #Exponential complexity
    print(n)
    if n<=3:
        return 1
    return fibRic(n-1)+fibRic(n-2)

def fibIte(n): #Linear complexity
    v=[0]*(n+1)
    v[1]=1
    for i in range(2,n):
        v[i]=v[i-1]+v[i-2]
    return v[n-1]

print(fibRic(9))
print(fibIte(9))
