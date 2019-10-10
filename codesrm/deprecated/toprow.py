def factors(n):
    """
    returns the number or factors for a positive integer n
    """
    nfactors = 0 # the number of factors of n
    for divisor in range(1, n+1): # divisors: {1,2,3,4...,n}
        if n%divisor == 0: # divides with no remainder
            nfactors += 1 # i.e. one new factor found
    return nfactors

def first(lst, val):
    w = -2
    for i in range(len(lst)):
        if lst[i] == val:
            w = i
            break
    return w+1

o = '{'

top = int(raw_input(""))
facs = map(factors, range(1,top+1))
print facs
mw = 0
mf = first(facs, max(facs))
while mw != mf:
    for i in range(1, mf+1):
        w = first(facs, i)
        if mw < w:
            mw = w
        if w != -1:
            ## w is first number to have i factors
            o += '{'+str(w)+','+str(i/float(w))+'}'+','
o = o[0:len(o)-1] + '}'
f = open('tops', 'w+') # this is the output file
f.write(o)





#m = 1
#for i in range(1, top):
#    w = factors(i)
#    if w >= m:
#        m = w
#        o += '{'+str(i)+','+str(w/float(i))+'}'+','
#o+='{'+str(top)+','+str(w/float(top))+'}'+'}'
f = open('tops', 'w+') # this is the output file
f.write(o)
