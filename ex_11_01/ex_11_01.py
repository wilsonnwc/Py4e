import re
numlist = list()
hand = open('regex_sum_1313951.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('[0-9]+', line)
    if len(x) > 0:
        numlist = numlist + x
        #as some lines contain multiple x,
        #numlist would then contain x (string) and
        #also lists of x (string); have to use this
        #instead of "sum" to combine the x

#converting strings x into integers
numlist = [int(i) for i in numlist]

print(sum(numlist))
