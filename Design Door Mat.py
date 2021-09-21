n, m = [int(x) for x in input().split()]

for i in range(1,n):
    if (i % 2 == 1):
        print((".|." *i).center(m, "-"))


print("WELCOME".center(m,"-"))

for i in range(1,n):
    if (i % 2 == 1):
        print((".|." *(n - i - 1)).center(m, "-"))
