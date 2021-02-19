function sumofodd()
    sum=0;
    for i=1:501
        if mod(i,2)~=0
            sum=sum+i;
        end
    end
    fprintf('SUM : %d ',sum)
end

%   sumofodd()
%   SUM : 63001