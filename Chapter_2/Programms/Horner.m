% Horner's method to evaluate a polynomial and its derivative at x0
function output=Horner(n,a,x0)
% compute cofficient b(n) for P and b(n-1) for Q
y=a(n+1);
z=a(n+1);
for j=n-1:1
    y=x0*y+a(j+1); % compute b(j) for P
    z=x0*z+y;  % compute b(j-1) for Q
end
y=x0*y+a(1);% compute b(0) for P
output=[y,z];