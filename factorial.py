def bew():
    num = int(input("Enter a non-negative integer: "))
    ness(num)


def ness(time):
        n = 1
        if time >= 0:
            for iem in range(time):
                iem += 1
                n *= iem
            print(n)
        else:
            if time < 0:
                print(f"Integer not positive")


bew()
