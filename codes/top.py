"""
finds toprow points and outputs to 'toprow' file
"""
from functions import filewrite, sigma
# first; sigma; filewrite

TOP = int(raw_input("How many toprow points do you want to go through?\n"))

faclst = map(sigma, range(1, TOP+1))
found = []
nfl = [] # in the format [number, ratio]
for r in range(len(faclst)):
    i=[r,faclst[r]]
    if i[1] not in found:
        found.append(i[1])
        nfl.append([i[0]+1, float(i[1])/(i[0]+1)])
del faclst
del found

out = '{'
for i in nfl:
    out += '{'+str(i[0])+','+str(i[1])+'},'
out = out[0:len(out)-1]
out += '}'
filewrite('toprow', out)
