#!/usr/bin/python
n,m=[int(x) for x in raw_input().split()]
sum1 = 0
for _ in range(m):
    a,b,k=[int(x) for x in raw_input().split() ]
    sum1+=(b-a+1)*k
print  (sum1/n)