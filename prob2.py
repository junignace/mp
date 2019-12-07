import numpy as np
def threePoint(x,y):
    A = np.array([(x[0],y[0],1), (x[1],y[1],1), (x[2], y[2], 1)])
    temp1 = (x[0]**2 + y[0] **2) * -1
    temp2 = (x[1]**2 + y[1]**2) * -1
    temp3 = (x[2]**2 + y[2] **2) * -1
    B = np.array([(temp1),(temp2),(temp3)])
    B.resize(3,1)
    
    W= np.linalg.det(A) 
    
    tempA1 = np.array([(temp1,y[0],1), (temp2,y[1],1), (temp3, y[2], 1)])
    Wa= np.linalg.det(tempA1)
    
    tempA2 = np.array([(x[0],temp1,1), (x[1],temp2,1), (x[2], temp3, 1)])
    Wb= np.linalg.det(tempA2)
    
    tempA3= np.array([(x[0],y[0],temp1), (x[1],y[1],temp2), (x[2], y[2], temp3)])
    Wc = np.linalg.det(tempA3)
    
    D = Wa/W
    E = Wb/W
    F = Wc/W
    
    h = (D/2)
    h1 =(D/2)**2
    k = (E/2)
    k1 =(E/2) **2
    r = ((-1*F) + abs(h1) + abs(k1))**(1/2)
    
    
    print('The Value of D is ',D)
    print('The Value of E is ',E)
    print('The Value of F is ',F)
    print('The Value of h is ',h)
    print('The Value of k is ',k)
    print('The Value of r is ',r)
    
    

    

    
    
    