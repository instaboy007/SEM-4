function fibonacci(n)
    x1 = 0;
    x2 = 1;
    while (x1<=n)
        number=sprintf('%d ', x1);
        disp(number)
        x3 = x1 + x2;
        x1 = x2;
        x2 = x3;
    end
end

%     fibonacci(8)
%     0 
%     1 
%     1 
%     2 
%     3 
%     5 
%     8 