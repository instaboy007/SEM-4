syms x y z
f1=sin(2*x)*cos(x);
f2=(1/(x^2+(5*x)+6));
f3=sqrt(9-(4*(x^2)));
f4=log10(tan(x));
f5=(1/(1+sqrt(cot(x))));
f6=sin(x)*(cos(x)^4);
f7=12*(x^2)*(y^3);
f8=x*exp(x*y);
f9=8*x*y*z;
f10=(x+y);
int(f1,x)
int(f2,x)
int(f3,x)
eval(int(f4,x,0,(pi/2)))
eval(int(f5,x,(pi/6),(pi/3)))
eval(int(f6,x,-1,1))
eval(int(int(f7,y,-1,0),x,1,2))
eval(int(int(f8,x,1,3),y,1,2))
eval(int(int(int(f9,x,0,1),y,0,2),z,0,3))
eval(int(int(int(f10,z,0,(4-x^2)),x,0,2),y,0,1))