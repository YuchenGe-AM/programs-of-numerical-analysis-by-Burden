% Method of False position for a solution to f(x)=0
function output=Falseposition(f,p0,p1,TOL,N0)
% Calculate runtime of the program
tic;
% If TOL is missing，error is assumed to be the standard error 1E-3.
if(nargin==3)
    TOL=1.0e-3;
end 

% Initialize variable for iteration ordinal number 
i=2;
q0=subs(f,p0);
q0=double(q0);
q1=subs(f,p1);
q1=double(q1);
k=1;
J=zeros(1,100);
while (i<=N0)
    p=p1-q1*(p1-p0)/(q1-q0);
    J(k)=p; % show the process of iteration
    k=k+1;
    if (abs(p-p1)<TOL)
        disp(['The solution of the equation is ',num2str(p,15),'.']);
        disp(['The time of iteration is ',num2str(i),'.']);
        output=J;
        toc
        return;
    end
    i=i+1; %update p0,q0,p1,q1.
    q=subs(f,p);
    q=double(q);
    if (q*q1<0)
        p0=p1;
        q0=q1;
    end
    p1=p;  %update p1,q1.
    q1=q;
end
% the procedure was unsuccessful
disp(['Method failed after N0 iterations, N0=',num2str(N0)])
toc
