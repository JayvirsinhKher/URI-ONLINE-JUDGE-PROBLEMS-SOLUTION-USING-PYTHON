A = None
B = None
X = None

def read_integer():
    try:
        #read for python 2.x
        return int(raw_input())
    except NameError:
        #read for python 3.x
        return int(input())

A = read_integer()
B = read_integer()
X = A + B
print(str("X = ") + str(X))
