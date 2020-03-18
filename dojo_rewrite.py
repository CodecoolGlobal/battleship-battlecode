import random
import math

s = 0
d = {}
with open('100.txt') as f:
    for a in f:
        p = ''
        for b in a:
            a_s = a.strip()
            if b != ',':
                p += b
            else:
                if a_s not in d:
                    d[a_s] = int(p)
                else:
                    d[a_s] += int(p)
                p = ''
        if a_s not in d:
            d[a_s] = int(p)
        else:
            d[a_s] += int(p)

s += math.sqrt(d['23,21,5'])
s += math.sqrt(d['342,2,5'])
s += math.sqrt(d['32,1,777'])
s += math.sqrt(d['234,645,223'])
s += math.sqrt(d['243,646,2342'])
s += math.sqrt(d['6346,3434,222'])
s += math.sqrt(d['3,6,2'])

print(s)