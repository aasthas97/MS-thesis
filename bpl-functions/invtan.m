function [angleslist, pointslist] = invtan(controlpoints)
% transform control points: x2, y2 relative to x1, y1
% for all (x2, y2), find angle relative to origin (x1, y1)

    foo = size(controlpoints);
    ns = foo(1); % number of strokes
    angleslist = cell(ns, 1); 
    pointslist = cell(ns, 1);
    for idx1 = 1:ns
        foo2 = size(controlpoints{idx1, 1});
        strokesize = foo2(1);
        anglesperstroke = cell(strokesize, 1);
        pointsperstroke = cell(strokesize, 1);
        set = controlpoints{idx1, 1};
%         fprintf('%d\n', strokesize);
        for idx2 = 0:strokesize-1
            if idx2 == 0 %if first pair of x,y coordinates, set x1, y1 to 0, 0
                x = set(1, 1);
                y = set(1, 2);
                angle = atan2(y,x);
                anglesperstroke{idx2+1} = angle;
                pointsperstroke{idx2+1} = [x y];
            elseif idx2 > 0
                x1 = set(idx2, 1);
                y1 = set(idx2, 2);
                x2 = set(idx2 +1 , 1);
                y2 = set(idx2 +1, 2);
                x = x2 - x1;
                y = y2 - y1;
                angle = atan2(y,x);
                anglesperstroke{idx2+1} = angle;
                pointsperstroke{idx2+1} = [x y];
            end
        end
        angleslist{idx1} = anglesperstroke;
        pointslist{idx1} = pointsperstroke;
    end
end