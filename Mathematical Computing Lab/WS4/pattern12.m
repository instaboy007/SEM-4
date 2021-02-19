function pattern12()
for i = 1:3
    for j = 1:3-i
        fprintf(' ');
    end
    for j = 1:(2*i)-1
        fprintf('*');
    end
    fprintf('\n');
end
for i = 2:-1:1
    for j = 1:3-i
        fprintf(' ');
    end
    for j = 1:(2*i)-1
        fprintf('*');
    end
    fprintf('\n');
end
end

%   pattern12()
%       *
%      ***
%     *****
%      ***
%       *