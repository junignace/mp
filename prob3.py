import numpy as np
def esti(xi,yi):
    p1= np.polyfit(xi,yi,1)
    p2= np.polyfit(xi,yi,2)
    p3= np.polyfit(xi,yi,3)
    p4= np.polyfit(xi,yi,4)
    p5= np.polyfit(xi,yi,5)
    p6= np.polyfit(xi,yi,6)
    p7= np.polyfit(xi,yi,7)
    p8= np.polyfit(xi,yi,8)
    p9= np.polyfit(xi,yi,9)
    p10= np.polyfit(xi,yi,10)
    p1i= np.polyval(p1,xi)
    p2i= np.polyval(p2,xi)
    p3i= np.polyval(p3,xi)
    p4i= np.polyval(p4,xi)
    p5i= np.polyval(p5,xi)
    p6i= np.polyval(p6,xi)
    p7i= np.polyval(p7,xi)
    p8i= np.polyval(p8,xi)
    p9i= np.polyval(p9,xi)
    p10i= np.polyval(p10,xi)
    
    vecyi = np.array([(yi)])
    
    
    e1 = vecyi - p1i
    e2 = vecyi - p2i
    e3 = vecyi - p3i
    e4 = vecyi - p4i
    e5 = vecyi - p5i
    e6 = vecyi - p6i
    e7 = vecyi - p7i
    e8 = vecyi - p8i
    e9 = vecyi - p9i
    e10 = vecyi - p10i
    
    a = np.linalg.norm(e1)
    b = np.linalg.norm(e2)
    c = np.linalg.norm(e3)
    d = np.linalg.norm(e4)
    e = np.linalg.norm(e5)
    f = np.linalg.norm(e6)
    g = np.linalg.norm(e7)
    h = np.linalg.norm(e8)
    i = np.linalg.norm(e9)
    j = np.linalg.norm(e10)
    
    k = np.array([(a,b,c,d,e,f,g,h,i,j)])
    
    if k.min() == a:
        print(p1)
    elif k.min() == b:
        print(p2)
    elif k.min() == c:
        print(p3)
    elif k.min() == d:
        print(p4)
    elif k.min() == e:
        print(p5)
    elif k.min() == f:
        print(p6)
    elif k.min() == g:
        print(p7)
    elif k.min() == h:
        print(p8)
    elif k.min() ==i:
        print(p9)
    elif k.min() == j:
        print(p10)
        
    
     
    
    
    
     
    
    