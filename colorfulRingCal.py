##################################################################
# use Bumside's Lemma and Brute Force Method to count the number #
# of different bracelets with n beads painted in m colors        #
##################################################################

# r = n / k * c = n / (gcd * k') * c
m = 3
n = 6

def gcd(a,b):
    return gcd(b, a%b) if b else a

def Bumside(m, n):
    G = n*2
    sg = 0
    for i in range(n):
        d = gcd(n, i)
        sg += m**d # rotation
    if n&1:
        sg += n * (m**((n+1)//2)) # only side-vertex flip type
    else:
        sg += n//2 * (m**(n//2)) # side flip
        sg += n//2 * (m**(n//2+1)) # vertex flip
    return sg // G
    
print(Bumside(m, n))
print(m**n, Bumside(m, n), m**n/Bumside(m, n))

# A ganerator to ganerate all possible bracelets
def ganerate(m, n):
    l = ""
    def _ganerate(m, n, l):
        if not n:
            yield l
            return  
        else:
            for i in range(m):
                yield from _ganerate(m, n-1, l+chr(48+i)) # ascii 33-126 94
    return _ganerate(m, n, l)

# Find the minimum representation
def minimum_representation(s):
    ss = s+s
    i, j, k = 0, 1, 0
    while i<len(s) and j < len(s) and k < len(s):
        t = ord(ss[i+k]) - ord(ss[j+k])
        if not t:
            k += 1
        else:
            if t > 0:
                i += k + 1
            else:
                j += k + 1
            if i == j:
                j += 1
            k = 0
    i = min(i,j)
    return i
    
# O(n*m^n)
def check_minimum(s):
    x = minimum_representation(s)
    if x:
        return False
    rs = s[::-1]
    rx = minimum_representation(rs)
    l = len(s)
    s = s + s
    rs = rs + rs
    for i in range(l):
        t = ord(s[i+x]) - ord(rs[i+rx])
        if t>0:
            return False
        if t<0:
            return True
    return True

def BruteForce(m, n):
    num = 0
    for s in ganerate(m, n):
        if check_minimum(s):
            print(s)
            num += 1
    return num
    
print(BruteForce(m, n))