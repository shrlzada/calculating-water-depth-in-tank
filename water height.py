import math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#given values
pi=3.1416
V=30
R=3

# V=pi*h**2*((3*R-h)/(3)) general formula for volume 

# fixed point iteration method
fixedpointvalues=[]

def fixedpoint(h):
    for i in range(10):
        h[i+1]=math.sqrt(90/(3.1416*(9-h[i])))
        fixedpointvalues.append(h[i+1])
    return h
h=[0]*11
fixedpoint(h)

#relative error calculation

relative_error1=[]
def relative_error_point(h):
    for i in range(len(fixedpointvalues)):
        try:
            error = abs((h[i] - h[i-1]) / h[i]) * 100
            relative_error1.append(error)
        except ZeroDivisionError:
            relative_error1.append(None)
    return error
relative_error_point(h)

index = list(range(len(fixedpointvalues)))
#graphs 
plt.plot( index , fixedpointvalues, color='blue', marker='o')
plt.title("Simple fixed point iteration method")
plt.xlabel("Iterations")
plt.ylabel("Height")
plt.show()

plt.plot(index, relative_error1, color='green', marker='o')
plt.title("Simple fixed point iteration method relative error")
plt.xlabel("Iterations")
plt.ylabel("Relative error")
plt.show()

#table

df = pd.DataFrame({

    "h": fixedpointvalues,
    "PRE,%": relative_error1
})

print(df)

#newton-rapson method

#given function

def f(x):
    return (pi * x**2 * (3*R - x)) / 3 - V

#prime of that function

def prime(x):
    return (2*pi*R*x-pi*x**2)

newtonvalues=[]
relative_error2=[]
x0=1
x=x0
for i in range(10):
    try:
        next_x=x-f(x)/prime(x)
        newtonvalues.append(next_x)
    except ZeroDivisionError:
        newtonvalues.append(None)
    if i == 0:
        error = np.nan
    else:
        error = abs((next_x - x)/next_x) 
    relative_error2.append(error)
    x=next_x


index2=list(range(len(newtonvalues)))
index3=list(range(len(relative_error2)))
plt.plot(index2, newtonvalues, color='black', marker='o')
plt.title("Newton-Raphson method values")
plt.xlabel("Iterations")
plt.ylabel("Height")
plt.show()
plt.plot(index3, relative_error2, color='red', marker='o')
plt.title("Newton-Raphson method percent relative error")
plt.xlabel("Iterations")
plt.ylabel("PRE,%")
plt.show()

df = pd.DataFrame({

    "h": newtonvalues,
    "PRE,%": relative_error2
})

print(df)