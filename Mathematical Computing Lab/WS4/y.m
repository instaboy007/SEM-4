function[answer]=y(x)
n=length(x);
for i = 1:n
    answer(i)=power((-0.2*x(i)),4) + (exp(-0.5*x(i)))*power(x(i),3) + 7*power(x(i),2);
    disp(answer(i))
end

%3.a)y(-2.5)
%    ans = -10.7241
%    y(3)
%    ans = 69.1541
%3.b)x=-3:0.01:4;
%    plot(x,y(x))
