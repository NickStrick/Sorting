totalTimes = 0

def count_down(n):
    global totalTimes
    totalTimes += 1

    if n == 0:
        return

    count_down(n-1)


count_down(5)
print(totalTimes)