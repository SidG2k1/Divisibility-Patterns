"""
outputs factor data for all numbers up to specified amount to the 'alldata' file
"""
from functions import sigma, filewrite

max_num = int(raw_input("How many data points do you want?\n"))
data = '{' # to conform to Mathematica format

for current_number in range(1, max_num): # current_number is {1,2,3...,to-1}
    # appending appropriate ratio to data
    data += str(sigma(current_number)/float(current_number)) + ', '
data += str(sigma(max_num)/float(max_num)) + '}' # last point: to; "}" to conform to Mathematica
filewrite('alldata', data)
