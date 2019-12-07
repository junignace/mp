function [h k r D E F] = threePoint(x,y)

A = [ x(1) y(1) 1; x(2) y(2) 1; x(3) y(3) 1]
b1 = (x(1) ^2 + y(1) ^2) * -1
b2 = (x(2) ^2 + y(2) ^2) * -1
b3 = (x(3) ^2 + y(3) ^2) * -1
B = [b1;b2;b3]


temp1 = A;
temp2 = A;

Wr = det(A);
A(:,1) = B;
WA1 = det(A);
temp1(:,2) = B;
WA2 = det(temp1);
temp2(:,3) = B;
WA3 = det(temp2);

D = WA1/ Wr;
E = WA2/Wr;
F = WA3/Wr;

h = D/2;
h1 = (D/abs(D))*((D/2)^2);
k = E/2;
k1= (E/abs(E))*((E/2)^2);
r =double(sqrt((-1*F) + abs(h1) + abs(k1)));

fprintf('The value of D is %.2f\n', D)
fprintf('The value of E is %.2f\n', E)
fprintf('The value of F is %.2f\n', F)
fprintf('The value of h is %.2f\n', h)
fprintf('The value of k is %.2f\n', k)
fprintf('The value of r is %.2f\n', r)

end



