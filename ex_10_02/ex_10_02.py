name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

count = dict()
for line in handle:
    line = line.rstrip()
    if line.startswith("From ") and not line.startswith("From:"):
        words = line.split()
        time = words[5]
        #print("Time", time)
        hrs = time.split(':')[0]
        #print("Hour", hrs)
        count[hrs] = count.get(hrs,0) + 1

#print("Count of hour", count)

tmp = list()
for k,v in count.items():
    newt = (k,v)
    tmp.append(newt)

tmp = sorted(tmp)
for k,v in tmp:
    print(k,v)
