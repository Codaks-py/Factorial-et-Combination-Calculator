# combination calculator
def combine():
    nn = 1
    rr = 1
    kk = 1
    print("A combination Calculator")
    print("n combination r")
    print("as in nCr")

    n = int(input("\tEnter value for n: "))
    if n >= 0:
        for i in range(n):
            i += 1
            nn *= i
    else:
        if n < 0:
            print(f"Integer not positive")

    r = int(input("\tEnter value for r: "))
    if r >= 0:
        for i in range(r):
            i += 1
            rr *= i
    else:
        if r < 0:
            print("Integer not positive")

    k = n-r
    if k >= 0:
        for i in range(k):
            i += 1
            kk *= i
    else:
        if k < 0:
            print("Not possible.....")

    com = rr * kk
    total = nn/com
    print(f"\nnCr = {total}")


combine()


