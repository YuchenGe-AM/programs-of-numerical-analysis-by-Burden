% Newton's method for a solution to f(x)=0
function output=Newton(f,p0,TOL,N0)
% Calculate runtime of the program
tic;
% If TOL is missing，error is assumed to be the standard error 1E-3.
if(nargin==3)
    TOL=1.0e-3;
end 
% Initialize variable for iteration ordinal number 
i=1;
k=1;
J=zeros(1,100);
while (i<=N0)
    fx=subs(f,p0);
    fx=double(fx);
    df=diff(f);
    df=subs(df,p0);
    df=double(df);
    p=p0-fx/df;
    J(k)=p; % show the process of iteration
    k=k+1;
    if (abs(p-p0)<TOL)
        disp(['The solution of the equation is ',num2str(p,15),'.']);
        disp(['The time of iteration is ',num2str(i),'.']);
        output=J;
        toc
        return;
    end
    i=i+1;
    p0=p;
end
% the procedure was unsuccessful
disp(['Method failed after N0 iterations, N0=',num2str(N0)])
toc
