function sumofprime()
    sum=0;
    for i =2:999
        if isprime(i)==1
            sum=sum+i;
        end
    end
    disp(sum)
end

%   sumofprime()
%   76127