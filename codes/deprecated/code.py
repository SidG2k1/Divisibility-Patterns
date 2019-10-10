"""
Extended Essay point generator
"""
def factors(n):
    """
    returns the number or factors for a positive integer n
    """
    nfactors = 0 # the number of factors of n
    for divisor in range(1, n+1): # divisors: {1,2,3,4...,n}
        if n%divisor == 0: # divides with no remainder
            nfactors += 1 # i.e. one new factor found
    return nfactors


to = int(raw_input("How many data points do you want?\n"))
data = '{' # to conform to Mathematica format

for current_number in range(1, to): # current_number is {1,2,3...,to-1}
    # appending appropriate ratio to data
    data += str(factors(current_number)/float(current_number)) + ', '
data += str(factors(to)/float(to)) + '}' # last point: to; "}" to conform to Mathematica

f = open('out', 'w+') # this is the output file
f.write(data)
# f.close()?
