a=10
b=20
c=30
d=40
e=50

#AND
print('AND')
if a+b < c+d and e/a > b*a:
    print("True")
else:
    print("False")

if c*d == e/a and b+d > c-e:
    print("True")
else:
    print("False")

if a/c != c*d and d+b == e/c:
    print("True")
else:
    print("False")
print(80*'-')
print()

#OR
print('OR')
if c+d > a/e or b-c != d*a:
    print("True")
else:
    print("False")

if e*b == a/c or b-d > c+d:
    print("True")
else:
    print("False")

if c%a > d*e or a-e < b/a:
    print("True")
else:
    print("False")
print(80*'-')
print()

#NOT
print('NOT')
if not(c+d != a*b and e/c > d%a):
    print("True")
else:
    print("False")

if not(a/c > e-b or d*a <e/c):
    print("True")
else:
    print("False")
