def to_bin(x):  #converts decimal to binary (16 bits)
    x = int(x)
    if(x<0):
        return two_comp(x)
    else:
        g = bin(x)
        g = g[2:]
        return '0'*(16-len(g)) + g        


def two_comp(x):   #converts negative decimal to 2's complement representation (16 bits)
    x = int(x)
    g = bin(x)
    g = g[3:]
    g = '0'*(16-len(g)) + g    
    l = []
    for i in g:
        l.append(i)
    l = l[::-1]
    m = []
    count = 0
    for i in l:
        count+=1
        if(i == '0'):
            m.append('0')
        else:
            m.append('1')
            break;
    for i in l[count:]:
        if(i == '0'):
            m.append('1')
        else:
            m.append('0')
    m = m[::-1]
    m = "".join(m)
    return m
    
    
            

def right_shift(x):   #arithmetic right shift
    l = []
    l.append(x[0])
    for i in x:
        l.append(i)
    l = l[:-1]
    l = "".join(l)
    return l


def bin_add(a, b):  #binary addition of a(16 bits) and b(16 bits)
    a = a[::-1]
    b = b[::-1]
    c = []
    carry = 0
    counter = 0
    while(counter<len(a)):
        i = a[counter]
        j = b[counter]
        if(i=='0' and j == '0' and carry == 0):
            c.append('0')
            carry = 0
        elif(i == '0' and j == '0' and carry == 1):
            c.append('1')
            carry = 0
        elif (i!=j and carry == 0):
            c.append('1')
            carry = 0
        elif(i!=j and carry == 1):
            c.append('0')
            carry = 1
        elif(i == '1' and j == '1' and carry == 0):
            c.append('0')
            carry = 1
        elif(i == '1' and j == '1' and carry == 1):
            c.append('1')
            carry = 1
        counter+=1
    c = c[::-1]
    c = "".join(c)
    return c
    

def bin_sub(a,b):  #binary subtraction of b(16 bits) from a(16 bits)
    a = a[::-1]
    b = b[::-1]
    c = []
    borrow = 0
    counter = 0
    while(counter<len(a)):
        i = a[counter]
        j = b[counter]
        if(i == '0' and j == '0' and borrow == 0):
            c.append('0')
            borrow = 0
        elif(i == '0' and j == '0' and borrow == 1):
            c.append('1')
            borrow = 1
        elif(i == '0' and j == '1' and borrow == 0):
            c.append('1')
            borrow = 1
        elif(i == '0' and j == '1' and borrow == 1):
            c.append('0')
            borrow = 1
        elif(i == '1' and j == '0' and borrow == 0):
            c.append('1')
            borrow = 0
        elif(i == '1' and j == '0' and borrow == 1):
            c.append('0')
            borrow = 0
        elif(i == '1' and j == '1' and borrow == 0):
            c.append('0')
            borrow = 0
        elif(i == '1' and j == '1' and borrow == 1):
            c.append('1')
            borrow = 1
        counter+=1
    c = c[::-1]
    c = "".join(c)
    return c         
    

    
multiplicand = input("Enter the multiplicand : ") #Input decimal multiplicand
multiplier = input("Enter the multiplier : ") #Input decimal multiplier
M = to_bin(multiplicand)
Q = to_bin(multiplier)
A = "0"*16
q0 = '0'
q1 = Q[-1]
numq0 = A+Q+q0
n = 16
while(n>0):
    if(q1 == q0):
        numq0 = right_shift(numq0)        
    elif(q1 == '0' and q0 == '1'):
        A = bin_add(A, M)
        numq0 = A+Q+q0
        numq0 = right_shift(numq0)
    elif(q1 == '1' and q0 == '0'):
        A = bin_sub(A, M)
        numq0 = A+Q+q0
        numq0 = right_shift(numq0)
    A = numq0[0:16]
    Q = numq0[16:-1]    
    q0 = numq0[-1]
    q1 = Q[-1]
    n=n-1

print(numq0[:-1]) #prints the 32 bit product
        
        

