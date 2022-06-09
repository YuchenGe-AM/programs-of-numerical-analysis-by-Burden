% Bisection method for a solution of f(x)=0
function output=Erfen(f,a,b,TOL,N0)
% Calculate runtime of the program
tic;
% If TOL is missing，error is assumed to be the standard one 1E-3.
if(nargin==4)
    TOL=1.0e-3;
end 
% Initialize variable for iteration ordinal number 
i=1;
FA=subs(f,a);
k=1;
J=zeros(1,100);
while (i<=N0)
    p=a+(b-a)/2;
    FP=subs(f,p);
    J(k)=p; % show the process of iteration
    k=k+1;
    if ((FP==0)||((b-a)/2<TOL))
        disp(['The solution of the equation is ',num2str(p,15),'.']);
        disp(['The time of iteration is ',num2str(i),'.']);
        output=J;
        toc
        return;
    end
    i=i+1;
    if(FA*FP>0)
        a=p; 
        FA=FP;
    else 
        b=p;
    end
end
% the procedure was unsuccessful
disp(['Method failed after N0 iterations, N0=',num2str(N0)])
toc
