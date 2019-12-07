import numpy as np
import matplotlib.pyplot as plt
a= []
n=0
temp=[]
for k in range(0,100):
    a.append(k)
    if n< 9:
        t = n**2 - 7
        n = n+1 
        temp.append(t)
    elif n == 9:
        t = np.NaN
        n=n+1
        temp.append(t)
    elif n > 9:
        n = n-10
        t= n**2 - 7
        temp.append(t)
        n = n +1



plt.stem(a,temp)

        
        