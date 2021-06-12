function [anglecentres, pointcentres] = centres(angleslist, pointslist)
    foo = size(angleslist);
    ns = foo(1);
    anglecentres = cell(ns, 1);
    pointcentres = cell(ns, 1);
    for index = 1:ns
        foo2 = size(angleslist{index, 1});
        strokesize = foo2(1);
        % compute angle-based centre
        anglecentre = sum(cell2mat(angleslist{index,1}))/strokesize;
        anglecentres{index} = anglecentre;
        % compute point-based centre
        x_sum = 0;
        y_sum = 0;
        for idx2 = 1:strokesize
            x_sum = x_sum + pointslist{index, 1}{idx2}(1);
            y_sum = y_sum + pointslist{index, 1}{idx2}(2);
            x_average = x_sum/strokesize;
            y_average = y_sum/strokesize;
            pointcentres{index} = [x_average, y_average];
        end
    end    
end