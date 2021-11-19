def pos(x):
    #This is a one-to-one function that associates a number between 0 and (2 ^ k) -1 to the key x
    #Typically pos (x) is the integer equivalent to the binary byte representation of x
    #In this example there is a table of 2 ^ 16 Boolean values to store a set of integers between 0 and 2 ^ 16
     return x & 0x0000ffff

def insert(a, x):
    a[pos(x)]=True

def search(a, x):
    return a[pos(x)]

tab = 2**16 * [False]
insert(tab,10)
insert(tab,100)
insert(tab,35)
print(tab)
print(100, search(tab, 100))
print(101, search(tab, 101))
