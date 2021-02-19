function squareroot()
n=input('ENTER THE NUMBER: ');
    for i = 1:n
        if mod(i,2)==0
            sprintf('THE SQUARE ROOT OF %d IS %.3f ',i,sqrt(i))
        end
    end
end

%   squareroot()
%   ENTER THE NUMBER: 5
%   ans =THE SQUARE ROOT OF 2 IS 1.414 
%   ans =THE SQUARE ROOT OF 4 IS 2.000 