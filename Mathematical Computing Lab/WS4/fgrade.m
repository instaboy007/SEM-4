function [ g ] = fgrade( R )
    g = zeros(size(R, 1), 1);
    for r = 1:size(R,1)
        hw_grades = R(r, 1:6);
        drop = min(hw_grades);
        drop_index = find(hw_grades == drop);
        drop_index = drop_index(1);
        hw_grades = hw_grades([1:drop_index-1 drop_index+1:end]);
        hw_avg = mean(hw_grades);
        midterm_avg = mean(R(r, 7:9));
        final = R(r, 10);
        if midterm_avg > final
            g(r, 1) = 0.85*midterm_avg + 0.15*hw_avg;
        else
            g(r, 1) = 0.15*R(r, 7) + 0.15*R(r, 8) + 0.15*R(r, 9) + 0.15*midterm_avg + 0.15*hw_avg;
        end
    end
end

%21.a)fgrade([8, 9, 6, 10, 9, 7, 76, 86, 91, 80])
%     ans =72.9733
%21.b)fgrade([7, 10, 6, 9, 10, 9, 91, 71, 81, 88])
%     ans =49.9500
%     fgrade([5, 5, 6, 1, 8, 6, 59, 72, 66, 59])
%     ans =56.7167
%     fgrade([6, 8, 10, 4, 5, 9, 72, 78, 84 78])
%     ans =47.9400
%     fgrade([7, 7, 8, 8, 9, 8, 83, 82, 81 84])
%     ans =50.4000