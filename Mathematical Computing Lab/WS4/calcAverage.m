function[avg,SD]= calcAverage(grades)
n=length(grades);
avg=sum(grades)/n;
SD=std(grades);
end 

%2.)grades=[80 75 91 60 79 89 65 80 95 50 81]
%   [avg,SD]=calcAverage(grades)
%   avg =76.8182
%   SD =13.6661
