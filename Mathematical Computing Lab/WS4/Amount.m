amount = 5000;
years = 0; 
while amount < 1000000
 amount = (1.09)*amount + 5000;
 years = years + 1; 
end
disp(amount)
disp(years)

%   1.0786e+06
%   34
