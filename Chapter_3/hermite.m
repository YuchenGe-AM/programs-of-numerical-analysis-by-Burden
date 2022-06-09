% Hermite interpolation
% t is coordinate number to be evaluated
function output=hermite (x,y,dy,t)
% Calculate runtime of the program
tic;
% compute the dimension of x
n=length(x);
syms s;
z=zeros(2*n,1);
Q=zeros(2*n,2*n);
for i=1:n
    z(2*i-1)=x(i);
    z(2*i)=x(i);
    Q(2*i-1,1)=y(i);
    Q(2*i,1)=y(i);
    Q(2*i,2)=dy(i);
    if(i~=1)
        Q(2*i-1,2)=(Q(2*i-1,1)-Q(2*i-2,1))/(z(2*i-1)-z(2*i-2));
    end
end
for i=3:(2*n)
    for j=3:i
        Q(i,j)=(Q(i,j-1)-Q(i-1,j-1))/(z(i)-z(i-j+1));
    end
end

% compute the hermite poynomial
temp=1;
hermitepoly=Q(1,1);
for i=1:n-1
    temp=temp*(s-x(i));
    hermitepoly=hermitepoly+Q(2*i,2*i)*temp;
    temp=temp*(s-x(i));
    hermitepoly=hermitepoly+Q(2*i+1,2*i+1)*temp;
end
hermitepoly=hermitepoly+temp*(s-x(n));
hermitepoly=simplify(hermitepoly);
hermitepoly=vpa(hermitepoly,10);
% output the evaluted number
m=length(t);
% temporary value
temp=zeros(1,m);
for i=1:m
    temp(i)=subs(hermitepoly,'s',t(i));
end
Q
disp(['The interpolation polynomial is ',char(hermitepoly),'.']);
disp(['The value of approximation is ',num2str(temp),'.']);
toc;
