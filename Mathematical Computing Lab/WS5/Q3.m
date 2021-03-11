syms x
f1=(x^2-5)*(x^3 - 2*x + 3);
f2=sin(x)*cos(x);
f3=abs(x);
f4=x*abs(x);
f5=(sqrt(x)+(2*x))*(4*x^2 - 1);
f6=(x^2+1)/((5*x)-3);
derivative1=diff(f1,x);
eval(subs(derivative1,x,2.0))
derivative2=diff(f2,x);
eval(subs(derivative2,x,2.0))
derivative3=diff(f3,x);
eval(subs(derivative3,x,2.0))
derivative4=diff(f4,x);
eval(subs(derivative4,x,2.0))
derivative5=diff(f5,x);
eval(subs(derivative5,x,2.0))
derivative6=diff(f6,x);
eval(subs(derivative6,x,2.0))