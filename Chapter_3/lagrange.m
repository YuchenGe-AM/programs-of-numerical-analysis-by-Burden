% lagrange polynomial for interpolation
% t is coordinate number (vector) to be evaluated
function output=lagrange(x,y,t)
% Calculate runtime of the program
tic;
% calculate the dimension of x
n=length(x);
syms p;
% calulate the lagrange polynomial
lapoly=0;
for i=1:n
    labase=y(i);
    for j=1:i-1
        labase=labase*(p-x(j))/(x(i)-x(j));
    end
    for j=i+1:n
        labase=labase*(p-x(j))/(x(i)-x(j));
    end
    lapoly=lapoly+labase;
end
lapoly=simplify(lapoly);
lapoly=vpa(lapoly,4);
% output the evaluted number
m=length(t);
% temporary value
temp=zeros(1,m);
for i=1:m
    temp(i)=subs(lapoly,'p',t(i));
end
disp(['The interpolation polynomial is ',char(lapoly),'.']);
disp(['The value of approximation is ',num2str(temp),'.']);
toc;