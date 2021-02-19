function [Area]=triangle(a,b,c)
    s = (a+b+c)/2;
    Area= sqrt(s*(s-a)*(s-b)*(s-c));
    disp(Area)
end

%   triangle(3,8,10)
%   ans =9.9216
%   triangle(7,7,5)
%   ans =16.3459