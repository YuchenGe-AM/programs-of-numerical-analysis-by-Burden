function f=hermite2(x,y,dy,x0)
%定义符号变量
syms s 
f=0.0; 
n=length(x);
for i=1:n
    la=1;
    lp=0.0; 
    for j=1:n 
        if(j~=i)
            la=la*(s-x(j))/(x(i)-x(j));
            lp=lp+1/(x(i)-x(j));
        end 
    end
    temp1=1-2*(s-x(i))*lp;
    temp2=y(i)*temp1*la^2;
    temp3=dy(i)*(s-x(i))*la^2;
    f=f+temp2+temp3;
end
f=simplify(f);
f=subs(f,s,x0);