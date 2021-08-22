def stars(n):
    for i in range (n):
        for j in range(i + 1):
            print(" ", end="")
            print("* ", end="")
        print()

def inverted(n):
    for i in range (n):
        print('\ ' * (i) + '* ' * (n - i) + '* ' * ((n - i)-1) + '/ ' * (i))

def triangle(n):
    x = n - 1
    y = 1
    for i in range (n):
        print("/ " * x + ('* ' * (2*y - 1)) + "\ " * x)
        x -=1
        y +=1

def base(l):
    p = l - 3
    r = 5
    for h in range (l):
        print("| " * p + "* " * r + "| " * p)


triangle(10)
base(10)
inverted(10)