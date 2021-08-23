fname = input("Enter file name: ")
fhand = open(fname)
lst = list()

for line in fhand:
    line = line.rstrip()
    line = line.split()
    #reminder: need a 2nd "for" to go through the lines to catch the words
    for wrd in line:
        if wrd in lst:
            continue
        else:
            lst.append(wrd)
#reminder: the lst and print shall not nest under the above for, or would go over and over again
lst.sort()
print(lst)
