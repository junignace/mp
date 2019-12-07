function output = esti(xi,yi)

p1 = polyfit(xi,yi,1);
p2 = polyfit(xi,yi,2);
p3 = polyfit(xi,yi,3);
p4 = polyfit(xi,yi,4);
p5 = polyfit(xi,yi,5);
p6 = polyfit(xi,yi,6);
p7 = polyfit(xi,yi,7);
p8 = polyfit(xi,yi,8);
p9 = polyfit(xi, yi, 9);
p10=polyfit(xi,yi,10);
p1i = polyval(p1,xi);
p2i = polyval(p2,xi);
p3i = polyval(p3,xi);
p4i = polyval(p4,xi);
p5i = polyval(p5,xi);
p6i = polyval(p6,xi);
p7i = polyval(p7,xi);
p8i = polyval(p8,xi);
p9i = polyval(p9,xi);
p10i = polyval(p10,xi);
e1= yi - p1i;
e2= yi - p2i;
e3= yi - p3i;
e4= yi - p4i;
e5= yi - p5i;
e6= yi - p6i;
e7= yi - p7i;
e8= yi - p8i;
e9= yi - p9i;
e10= yi - p10i;

a= norm(e1);
b= norm(e2);
c= norm(e3);
d= norm(e4);
e= norm(e5);
f= norm(e6);
g= norm(e7);
h= norm(e8);
i= norm(e9);
j= norm(e10);

k = [a b c d e f g h i j];

if min(k) == a
    output = p1;
    
elseif min(k) == b
    output = p2;
elseif min(k) == c
    output = p3;
elseif min(k) == d
    output = p4;
elseif min(k) == e
    output = p5;
elseif min(k) == f
    output = p6;
elseif min(k) == g
    output = p7;
elseif min(k) == h
    output = p8;
elseif min(k) == i
    output = p9;
elseif min(k) == j
    output = p10;
end
disp(output)
end
