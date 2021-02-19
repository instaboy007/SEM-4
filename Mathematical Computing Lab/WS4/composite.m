function composite()
    sum=0;
    for i = 2:50
        if isprime(i)==0
            sum=sum+i;
        end
    end
    disp(sum)
end

%   composite()
%   946