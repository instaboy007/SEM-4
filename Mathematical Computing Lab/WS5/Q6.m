syms y(x)
ode1=diff(y,x)== (exp(3*x)+sin(x));
answ1(x)=dsolve(ode1)
ode2=diff(y,x,2)==(2+x);
answ2(x)=dsolve(ode2)
ode3=diff(y,x,10)==0;
answ3(x)=dsolve(ode3)
ode4=diff(y,x,3)==(x^2);
answ4(x)=dsolve(ode4)
ode5=diff(y,x)+(cos(x)*y)==sin(x)*cos(x);
answ5(x)=dsolve(ode5)