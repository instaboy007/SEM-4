function sumofseries()
    sum=0;
    for i = 1:2:9999
    sum = sum+power(-1,i+1)*power(i,2);
    end
    disp(sum)
end

%   ans=1.6667e+11
