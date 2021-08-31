# Countdown

x = []
def countdown(number):
    for y in range(number,-1,-1):
        x.append(y)
    return x

countdown(5)

# Print and Return

def print_and_return(a,b):
    print(a)
    return b
print_and_return(1,2)

# First Plus Length

def first_plus_length(x):
    return x[0] + len(x)
first_plus_length([1,2,3,4,5])

# Values Greater than Second
def values_greater_than_second(x):
    y = []
    if (len(x)<2):
        return 'False'
    else:
        for i in range(0,len(x)):
            if (x[i]>x[1]):
                y.append(x[i])
    return y
values_greater_than_second([5,2,3,2,1,4])
values_greater_than_second([3])

# This Length, That Value

def length_and_value(x,y):
    arr=[]
    for i in range(0,x):
        arr.append(y)
    return arr
length_and_value(4,7)
length_and_value(6,2)