a=2014
b=7
c=7
if a!=b:
    print("True")
else:
    print("False")

if b!=c:
    print("False")
else:
    print("True")

#Using strings
a="Hello"
b="Hello"
c="World"
if a!=b or b!=c:
    print("At least one of the conditions is false")
else:
    print("At least one of the conditions is true")

#Using new values
a=1
b=7
if (a==1) != (b==5):
    print("Hello")