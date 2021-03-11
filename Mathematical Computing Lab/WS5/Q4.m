syms x y
f=cos(2*x)-(x^2*exp(5*y))+(3*y^2);
ans1=diff(f,x);
vpa(subs(ans1,[x,y],[2,3]))
ans2=diff(f,y);
vpa(subs(ans2,[x,y],[2,3]))
ans3=diff(f,x,2);
vpa(subs(ans3,[x,y],[2,3]))
ans4=diff(f,y,2);
vpa(subs(ans4,[x,y],[2,3]))
ans5=diff(ans2,x);
vpa(subs(ans5,[x,y],[2,3]))
ans6=diff(ans1,y);
vpa(subs(ans6,[x,y],[2,3]))
ans7=diff(diff(ans1,y),x);
vpa(subs(ans7,[x,y],[2,3]))