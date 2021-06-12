function goodwalks = findwalks(best1, best2, best3, best4, best5, best6, best7, best8, best9, best10, range)
    
% finds walks in orig MP list that match with best MPs (in terms of size)
% and adds the indices of those walks to list 'goodwalks'

    goodwalks = [];
    for index = 1:range
        filename = strcat('origMP', num2str(index), '.mat');
        load(filename);
        checkingfile = fullMP;
        
        if size(checkingfile) == size(best1)
            goodwalks = horzcat(goodwalks, index);
        elseif size(checkingfile) == size(best2)
            goodwalks = horzcat(goodwalks, index);
        elseif size(checkingfile) == size(best3)
            goodwalks = horzcat(goodwalks, index);
        elseif size(checkingfile) == size(best4)
            goodwalks = horzcat(goodwalks, index);
        elseif size(checkingfile) == size(best5)
            goodwalks = horzcat(goodwalks, index);
        elseif size(checkingfile) == size(best6)
            goodwalks = horzcat(goodwalks, index);
        elseif size(checkingfile) == size(best7)
            goodwalks = horzcat(goodwalks, index);
        elseif size(checkingfile) == size(best8)
            goodwalks = horzcat(goodwalks, index);
        elseif size(checkingfile) == size(best9)
            goodwalks = horzcat(goodwalks, index);
        elseif size(checkingfile) == size(best10)
            goodwalks = horzcat(goodwalks, index);        
        end
    end
    
end