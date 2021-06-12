function [automate] = automate(MPname, bestMPname)
    MPfile = strcat(MPname, '.mat');
    bestMPfile = strcat(bestMPname, '.mat');
    load(MPfile);
    range = size(MP);
    MPcat(MP, 'orig');
    load(bestMPfile);
    MPcat(bestM_pass2, 'best'); % extract separate MP files for all best MPs
    % load each bestMP file and assign it to a variable
    load('bestMP1.mat')
    best1 = fullMP;
    load('bestMP2.mat')
    best2 = fullMP;
    load('bestMP3.mat')
    best3 = fullMP;
    load('bestMP4.mat')
    best4 = fullMP;
    load('bestMP5.mat')
    best5 = fullMP;
    load('bestMP6.mat')
    best6 = fullMP;
    load('bestMP7.mat')
    best7 = fullMP;
    load('bestMP8.mat')
    best8 = fullMP;
    load('bestMP9.mat')
    best9 = fullMP;
    load('bestMP10.mat')
    best10 = fullMP;
    
    for bestwalks = {best1, best2, best3, best4, best5, best6, best7, best8, best9, best10}
        bestwalk = bestwalks{1, 1};
        fprintf('new walk\n'); % fix idx
%         keySet = containers.Map('KeyType','double', 'ValueType','any'); % dict for each best walk
        for candidatewalknumber = findwalks(best1, best2, best3, best4, best5, best6, best7, best8, best9, best10, range)
            candidatewalkname = strcat('origMP', num2str(candidatewalknumber), '.mat');
            load(candidatewalkname);   
            candidatewalk = fullMP;
            if size(bestwalk) == size(fullMP)
                fprintf('\nWalk number:%d\n', candidatewalknumber);
                score = matchscore(bestwalk, fullMP);
                averagedistance = avdist(bestwalk, fullMP);
                fprintf('\nMatches best walk with score %d\n',score);
                fprintf('\nAverage distance: %d\n', averagedistance);
%                 keySet(candidatewalknumber) = [score, averagedistance]
                
            elseif size(bestwalk) ~= size(candidatewalk)
                % do nothing
           
            end
           
        end
    end
end