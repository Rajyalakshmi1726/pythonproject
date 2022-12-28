t=1
def fact():
    b = int(input("enter a range"))
    for i in range(1,b):
        global t
        t=t*b
        b-=1
        print(t)



fact()