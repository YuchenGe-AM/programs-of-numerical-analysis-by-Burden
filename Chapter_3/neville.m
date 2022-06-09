% neville's iterated interpolation 
% t is coordinate number to be evaluated
function output=neville(x,y,t)
n=length(x);
% Calculate runtime of the program
tic;
% initialize the table
Q=zeros(n,n);
for i=1:n
    Q(i,1)=y(i);
end
for i=2:n
    for k=2:i
        Q(i,k)=((t-x(i-k+1))*Q(i,k-1)-(t-x(i))*Q(i-1,k-1))/(x(i)-x(i-k+1));
    end
end
toc
output=Q;
