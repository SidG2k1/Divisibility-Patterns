"""
Contains functions used in extended essay code
"""
def sigma(num):
    """
    returns the number or factors for a positive integer n
    """
    nfactors = 0 # the number of factors of n
    for divisor in range(1, num+1): # divisors: {1,2,3,4...,n}
        if num%divisor == 0: # divides with no remainder
            nfactors += 1 # i.e. one new factor found
    return nfactors

# def first(lst, val):
#     """
#     Finds index of first instance of val in lst
#     """
#     loc = -2
#     #for i in range(len(lst)):
#     for i in enumerate(lst):
#         if lst[i[0]] == val:
#             loc = i[0]
#             break
#     return loc

def filewrite(filename, inp):
    """
    Writes 'filename' with 'inp'
    """
    fil = open(filename, 'w+')
    fil.write(inp)
    fil.close()
