a = int(input())
b = int(input())
c = int(input())

p = a+b+c/2

from math import sqrt
S = sqrt(p*(p-a)*(p-b)*(p-c))

h = a/2*S

print(h)

