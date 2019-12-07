a = 0:99;
n = 0;
for k = 1:100
    if n < 9
        f(k) = n^2 -7;
        n = n+1;
    elseif n == 9
        f(k) = NaN;
        n = n+1;
    elseif n > 9
        n = n-10;
        f(k) = n^2 -7;
        n = n+1;    
   
    end
    

end
stem(a,f)