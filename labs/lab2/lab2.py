import math
def valuerequest():
    n = eval(input('Enter the values to be entered: '))
    rm = 0
    hm = 0
    gm = 1
    for i in range(n):
        value = eval(input('Enter value: '))
        rm = rm + (value * value)
        hm = hm + (1/value)
        gm = gm * value
    rms = math.sqrt(rm / n)
    hm = n / hm
    gm = gm ** (1/n)
    print(round(rms, 3))
    print(round(hm, 3))
    print(round(gm, 3))

valuerequest()
