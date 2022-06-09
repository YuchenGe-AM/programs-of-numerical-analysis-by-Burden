% Newton's interpolatory divided difference fomula
% t is coordinate number to be evaluated
function output=newton(x,y,t)
% Calculate runtime of the program
tic;
% initialize
newpoly=y(1);
syms s;
% compute the dimension of x
n=length(x);
coeff=zeros(1,n);
temp1=zeros(1,n);
dxs=1;
for i=1:n-1
    for j=i+1:n
        coeff(j)=(y(j)-y(i))/(x(j)-x(i));
    end
    temp1(i)=coeff(i+1);    % tempoary variable
    dxs=dxs*(s-x(i));
    newpoly=newpoly+temp1(i)*dxs;
    y=coeff;
end
% simplify the polynomial
newpoly=simplify(newpoly);
newpoly=vpa(newpoly,4);
% output the evaluted number
m=length(t);
% temporary value
temp=zeros(1,m);
for i=1:m
    temp(i)=subs(newpoly,'s',t(i));
end
disp(['The interpolation polynomial is ',char(newpoly),'.']);
disp(['The value of approximation is ',num2str(temp),'.']);
toc;