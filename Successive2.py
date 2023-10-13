x = int(input("enter a number : "))
a = 1
b = 0
print(a)
for i in range(1 , x) :
    c = a + b
    print(c)
    b = a
    a = c
