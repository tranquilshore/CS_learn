#from collections import defaultdict
from operator import itemgetter
import operator

#dctnry = defaultdict(int)
lst = [5,2,2,8,5,6,8,8]
   
#freq = sorted(dctnry.items(), key=operator.itemgetter(1), reverse=True)

indx = sorted(range(len(lst)), key= lambda k: lst[k])

tup_freq = ()

for i in range(len(lst)):
    tup_freq += ((indx[i], lst[indx[i]]),)

a = list()
a.append(tup_freq[0][0])
c = list()
count = 1
if len(tup_freq) >= 2:
    for i in range(1,len(tup_freq)):
        if tup_freq[i][1] != tup_freq[i-1][1]:
            a.append(tup_freq[i][0])
            c.append(count)
            count = 1
        else:
            count += 1
    c.append(count)
            
new_tup = ()
for i in range(len(a)):
    new_tup += ((a[i], c[i]),)
new_tup = list(new_tup)
print new_tup
pp = sorted(new_tup,key=itemgetter(0))
print sorted(pp, key = itemgetter(1), reverse = True)

#print final_tup
