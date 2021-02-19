function[y]=eval(x)
n=length(x);
for i=1:n
y(i)=(power(x(i),4)*(sqrt((3*x(i))+5)))/power((power(x(i),2)+1),2);
%disp(y(i))
end

%1.a)x=6
%    eval(x)
%    ans=4.5401
%1.b)x=[1:2:11]
%    eval(x)
%    ans=0.7071    3.0307    4.1347    4.8971    5.5197    6.0638