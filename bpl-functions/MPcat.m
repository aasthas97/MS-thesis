function fullMP = MPcat(OutputMP, typeMP)
    % create separate mat files for every motor program in the set
    % (original/best)
    % Parameters: outputMP- MP file that contains the motor component
    % typeMP: whether motor program is 'original' or 'best'
    for index = 1:size(OutputMP)
        if typeMP == 'best'
            filename = strcat('bestMP', num2str(index), '.mat');
        elseif typeMP == 'orig'
            filename = strcat('origMP', num2str(index), '.mat');
        end
        fullMP = [];
        motorcomponent = OutputMP{index, 1}.motor; % extract the motor component of the motor program
        for index = 1:size(motorcomponent)
            strokearray = motorcomponent{index, 1};
            if size(strokearray) == [1 1]
                fullMP = vertcat(fullMP, strokearray{1, 1});
            else
                for index = 1:size(strokearray)
                    fullMP = vertcat(fullMP, strokearray{index, 1});
                end
            end
            
        end
        save(filename, 'fullMP');
    end
    
end    