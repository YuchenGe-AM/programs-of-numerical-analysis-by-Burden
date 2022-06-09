% Muller's method for a solution of f(x)=0
function output=Muller(f,x0,x1,x2,TOL,N0)
% Calculate runtime of the program
tic;
% If TOL is missing，error is assumed to be the standard one 1E-3.
if(nargin==4)
    TOL=1.0e-3;
end 
% Initialize variable for iteration ordinal number 
i=3;
h1=x1-x0;
h2=x2-x1;
fx0=subs(f,x0);
fx0=double(fx0);
fx1=subs(f,x1);
fx1=double(fx1);
fx2=subs(f,x2);
fx2=double(fx2);
d1=(fx1-fx0)/h1;
d2=(fx2-fx1)/h2;
d=(d2-d1)/(h2+h1);
k=1;
J=zeros(1,100);
while (i<=N0)
    b=d2+h2*d;
    D=(b^2-4*fx2*d)^(1/2);
    if (abs(b-D)<abs(b+D))
        E=b+D;
    else
        E=b-D;
    end
    h=-2*fx2/E;
    p=x2+h;
    J(k)=p; % show the process of iteration
    k=k+1;
    if (abs(h)<TOL)
        disp(['The solution of the equation is ',num2str(p),'.']);
        disp(['The time of iteration is ',num2str(i),'.']);
        output=J;
        toc
        return;
    end
    i=i+1;
    x0=x1;
    x1=x2;
    x2=p;
    h1=x1-x0;
    h2=x2-x1;
    fx0=subs(f,x0);
    fx0=double(fx0);
    fx1=subs(f,x1);
    fx1=double(fx1);
    fx2=subs(f,x2);
    fx2=double(fx2);
    d1=(fx1-fx0)/h1;
    d2=(fx2-fx1)/h2;
    d=(d2-d1)/(h2+h1);
end
% the procedure was unsuccessful
disp(['Method failed after N0 iterations, N0=',num2str(N0)])
toc
